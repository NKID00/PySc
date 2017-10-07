# **PySc &nbsp; - &nbsp; 在Scratch里和Python愉快地玩耍**
- 目前**仅支持** Microsoft®**Windows**® 和 **Scratch *2.0* Offline Editor**
## 示例
![](http://ww1.sinaimg.cn/large/0060lm7Tly1fk7pdi04rvj30gn0a4mxv.jpg)
## 优点
- **无需使用改版**Scratch
- 只需一次运行，**自动开机启动**
- **几乎不耗性能**
- 项目以GPL**开源**
## 目标
- 无需安装Python
- 支持 `time.sleep()`
- 可以在Scratch上执行.py(.pyw/.pyc/.pyo)文件
- 移植到Linux和MacOSX上
## 教程
### · 如何安装PySc
**首先,安装Python 3和Scratch 2.0 Offline Editor(自己度娘教程)。然后打开PySc.pyw和Scratch。**

![](http://ww2.sinaimg.cn/large/0060lm7Tly1fk8a5ict0xj30910aemxk.jpg)
![](http://ww2.sinaimg.cn/large/0060lm7Tly1fk8abjwqauj30r30g2n0d.jpg)
![](http://ww2.sinaimg.cn/large/0060lm7Tly1fk8w6x0y8pj305k07amx9.jpg)

**然后就可以像示例一样在Scratch里和Python愉快地玩耍啦~**
### · 如何使用PySc
![](http://ww1.sinaimg.cn/large/0060lm7Tly1fk9z03e2ipj305k09gjrl.jpg)

- ① &nbsp; 重置一切信息和状态以及删除一切申请的Python环境。**建议在开始运行和退出时执行"重置全部"块。**
- ② &nbsp; 向PySc申请一个Python环境，**最多可以申请256个环境**，编号为1-256。同一个环境中的Python变量、函数或包可以通用。**0号环境为一次性环境**，无需申请即可使用，但无法储存Python变量。
- ③ &nbsp; 删除一个申请的Python环境。
- ④ &nbsp; 获取上一次申请的Python环境的编号。**建议将编号储存在Scratch的变量中。**
- ⑤ &nbsp; 在指定编号的Python环境中执行给予的Python表达式，**并返回数据或抛出错误**。
- ⑥ &nbsp; 获取上一次执行的表达式的返回值。执行"重置全部"块或每次执行表达式时都会重置。**建议将返回值储存在Scratch的变量中再进一步处理。**
- ⑦ &nbsp; 在指定编号的Python环境中执行给予的Python语句，**可能会抛出错误**。
- ⑧ &nbsp; 在指定编号的Python环境中导入指定的Python包，**可能会抛出错误**。
- ⑨ &nbsp; 获取上一次执行表达式、执行语句或导入包时的状态。如果抛出错误为-1，正常则为0。执行"重置全部"块或每次执行表达式、执行语句或导入包都会重置。**建议在导入包或执行重要语句后检查状态是否正常再进一步运行。**
- ⑩ &nbsp; 获取上一次执行表达式、执行语句或导入包时抛出的错误信息。执行"重置全部"块或每次执行表达式、执行语句或导入包抛出错误时才会重置。建议将错误信息储存在Scratch的变量中再进一步处理。