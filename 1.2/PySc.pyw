import socket
import time
import sys
import os
import urllib.parse
from win32comext.shell import shell as winshell
import pythoncom
from past.builtins import execfile


def info(message=''):
    if debug:
        global log_name
        t = time.time()
        t = time.strftime("%Y-%m-%d %H:%M:%S.", time.localtime(t)) + str(int(t * 1000 % 1000))
        t = f"[{t}:INFO ] {message}"
        print(t)
        log = open(log_name, 'a')
        log.write(t + '\n')


def ac():
    global v_ret, v_status, v_err, v_shell, shells
    v_ret = None
    v_status = True
    v_err = 0
    v_shell = 0
    shells.clear()


def get_shell():
    global shells, local, v_status
    if len(shells) >= 256:
        v_status = False
        return -1
    n = min(set(range(1, 256)) - set(shells.keys()))
    shells[n] = local.copy()
    return n


def del_shell(num):
    global shells
    try:
        del shells[int(num)]
    except KeyError or ValueError:
        pass


def exp(arg):
    global v_status, v_ret, v_err, local
    shell, arg = arg.split('/')
    shell = int(shell)
    if shell == 0:
        v_status = True
        try:
            v_ret = eval(arg, local, local)
        except BaseException as e:
            v_err = e.args[0]
            v_status = False
    elif shell not in shells.keys():
        v_err = '未知的环境'
        v_status = False
        return
    v_status = True
    try:
        v_ret = eval(arg, shells[shell], shells[shell])
    except BaseException as e:
        v_err = e.args[0]
        v_status = False


def run(arg):
    global v_status, v_err, shells
    shell, arg = arg.split('/')
    shell = int(shell)
    if shell == 0:
        v_status = True
        try:
            exec(arg, local, local)
        except BaseException as e:
            v_err = e.args[0]
            v_status = False
    elif shell not in shells.keys():
        v_err = '未知的环境'
        v_status = False
        return
    v_status = True
    try:
        exec(arg, shells[shell], shells[shell])
    except BaseException as e:
        v_err = e.args[0]
        v_status = False


def imp(arg):
    run('%s/import %s' % arg.split('/'))


def run_file(arg):
    global v_status, v_err, shells
    shell, arg = arg.split('/')
    shell = int(shell)
    if shell == 0:
        v_status = True
        try:
            execfile(arg, local, local)
        except BaseException as e:
            v_err = e.args[0]
            v_status = False
    elif shell not in shells.keys():
        v_err = '未知的环境'
        v_status = False
        return
    v_status = True
    try:
        execfile(arg, shells[shell], shells[shell])
    except BaseException as e:
        v_err = e.args[0]
        v_status = False


def main():
    global PORT, v_ret, v_status, v_err, v_shell

    info(f'Serving on port {PORT} ...')
    while True:
        try:
            s.listen(5)
            conn, addr = s.accept()
            request = urllib.parse.unquote(conn.recv(1024).decode('UTF-8')).strip()
        except OSError:
            continue
        info("==========")
        info("Connected from IP: %s Port: %s" % addr)
        if request == '':
            info('Request: (None)')
        else:
            try:
                if request.split('\r\n')[1] == 'Referer: app:/Scratch.swf' and request.split(' ')[0] == 'GET':
                    # scratch's request
                    request = request.split('\r\n')[0].split(' HTTP/1.1')[0].split(' ', 1)[1]
                    info("Request: %s" % request)
                    if request == '/poll':
                        ret_all = ''
                        ret_all += f'v_err {v_err}\n'
                        ret_all += f'v_status {"true" if v_status else "false"}\n' 
                        ret_all += f'v_ret {str(v_ret)}\n'
                        ret_all += f'v_shell {v_shell}\n'
                        info('Return:')
                        for r in ret_all.split('\n')[:-1]:
                            info(' ' * 4 + r)
                        try:
                            conn.sendall(ret_all.encode('UTF-8'))
                        except OSError:
                            pass
                    elif request == '/reset_all':
                        ac()
                        info('Return: (None)')
                    else:
                        pro = request.split('/')[1]
                        try:
                            res = request.split('/', 2)[2]
                        except IndexError:
                            res = ''
                        if pro == 'exp':
                            exp(res)
                        elif pro == 'run':
                            run(res)
                        elif pro == 'imp':
                            imp(res)
                        elif pro == 'runfile':
                            run_file(res)
                        elif pro == 'ac':
                            ac()
                        elif pro == 'getshell':
                            v_shell = get_shell()
                        elif pro == 'delshell':
                            del_shell(res)
                        info('Return: (None)')
                else:
                    info(f"Request: {request}")
            except IndexError:
                pass
        conn.close()
        time.sleep(0.03)


if __name__ == '__main__':
    PORT = 8507

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('', PORT))
    except OSError:
        s.close()
        sys.exit(-1)

    if len(sys.argv) == 2 and sys.argv[1] == 'debug':
        debug = True
    else:
        debug = False
    if debug:
        log_name = time.strftime('logs\\%Y-%m-%d-%H-%M-%S.log', time.localtime(time.time()))
        try:
            os.mkdir("logs")
        except FileExistsError:
            pass
        fp = open(log_name, 'w')
        fp.close()
        del fp

    shortcut = pythoncom.CoCreateInstance(
        winshell.CLSID_ShellLink, None, pythoncom.CLSCTX_INPROC_SERVER, winshell.IID_IShellLink)
    shortcut.SetPath(sys.argv[0])
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(
        os.environ['APPDATA'] + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\PySc.lnk', 0)

    v_ret = None
    v_status = True
    v_err = 0
    v_shell = 0

    shells = {}
    shell_n = 0
    local = {'__name__': '__main__', '__doc__': None, '__package__': None, '__spec__': None,
             '__annotations__': {}, '__builtins__': locals()['__builtins__']}

    main()
