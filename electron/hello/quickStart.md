#Quick Start

* Electron提供了丰富的原生（操作系统）API接口，可以让你只用JavaScript就能创建桌面应用；
* Electron实际上就是将Node.js运行环境从后台服务迁移到桌面应用；
* Electron并没有用JavaScript绑定任何GUI框架，而只是将网页作为GUI，它就是一个轻量化的Chromium浏览器；

##主进程（main process）

`package.json`文件里的`main`脚本的进程被称为`main process`，运行在主进程里的脚本可以控制网页上GUI界面显示。

##渲染进程（renderer process）

每个网页（web page）拥有自己的渲染进程，浏览器中网页运行在沙箱环境中，禁止访问本地资源，但在Electron中，网页可以用Node.js的API和操作系统底层交互。

##主进程和渲染进程的区别

主进程通过创建`BrowerWindow`实例来创建网页，每个`BrowerWindow`实例在它们各自的渲染进程中运行网页，当`BrowerWindow`实例被销毁，相应的渲染进程也会终止。
网页的渲染进程要操作API需要向主进程发送请求，可以用`ipcRenderer`和`ipcMain`模块发送消息，用`remote`模块进行IPC通信。
IPC通信，Inter-process communication，进程间通信。
RPC, Remote procedure call，远程调用，不同机器上的进程间通信。

##The hard parts made easy

* Automatic updates
>Main Process
**autoUpdater**

* Native menus & notifications
>Create native application menus and context menus

* App crash reporting

* Debugging & profiling

* Windows installers
