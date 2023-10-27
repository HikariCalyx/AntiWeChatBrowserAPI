# 反微信浏览器 API 后端
这是基于 Python + Flask 的反微信浏览器 API。

## 检测原理
检查用户访问请求中的 User-Agent 中是否包含以下字符：
```
WindowsWechat     # Windows 版微信浏览器
MacWechat         # macOS 版微信浏览器
MicroMessenger    # 所有平台的微信浏览器
```
一旦检测到 User-Agent 中包含以上关键字，则会弹出拒绝让用户访问并指导让用户通过正常浏览器访问的提示。

## 为什么要做这个东西
我们注意到，中国国内用户极度依赖微信的使用。

微信浏览器存在很多问题，主要问题就是下载文件不会显示进度从而导致大文件非常容易损坏。

此外，我们还希望阻止用户从移动端下载文件。

## 关于 main.py
这是一套简单的基于 Flask 的实现构建示例。
如果您的后端是使用其它语言实现的（例如 PHP），您也可以参考这一套判断逻辑。

使用 main.py 前，您必须要修改里面的 SSL 证书私钥路径。这里假定您使用 certbot 从 Let's Encrypt 获取指向 yourdomain.com 的证书。
如果您打算通过其它负载均衡器（例如 Nginx）来加载 SSL 证书，则请删除相关参数且不能使用 443 端口。

在本例中，我们从奶牛快传提供文件下载，但同时需要防止用户从移动端下载，因此我们提供了形如这样的链接：
https://api.hikaricalyx.com/FileDownload/CTWorks?id=20edf136f7ba47

运行 Python 3.9 或以上版本的 VPS 环境在安装了 requirements.txt 提到的依赖项之后就可以正常运行。条件原因，我们未能测试在 Serverless 云函数环境的运行表现。

## TO-DO
防移动端下载的多语言界面自适应功能，以确保非中文用户从移动端下载文件时，能够在不借助浏览器自动翻译的前提下看懂网站提示。

## License
MIT

web/static 目录内的 CSS/JS 代码[引用自 bootstrap](https://github.com/twbs/bootstrap)。
