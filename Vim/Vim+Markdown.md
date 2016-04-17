# Vim+Markdownd

使用vim将近两年时间了（当然还是处于基本功能的使用阶段），所以只要是有文字输入的地方就会想：“要是支持Vim就好了”。
好在大多数开发工具都有vim模式，但大多数笔记软件和markdown工具都不支持vim模式，这对于我来说是很不爽的，因为我不能继续使用
hjkl了。     

**于是解决方案来了：Vim+markdown插件vim-instant-markdown**
使用vim打开`.md`后缀的文件时，它会自动打开你的浏览器对该markdown文件进行试试预览，这样就完美解决了markdown笔记软件不支持vim
的尴尬局面。

首先感谢作者：suan    
Github仓库地址: https://github.com/suan/vim-instant-markdown

这个markdown插件安装起来比较简单：

1. 首先确保你已经安装了node环境和它的包管理工具npm（因为要使用它安装instant-markdown-d）
2. 安装`suan/vim-instant-markdown`这个vim插件
3. 确保在你的`.vimrc`文件中有开启了插件功能，也就是这句`filetype plugin on`

以上三步完成后就成功了，你可以试着创建或者打开一个markdown文件,enjoy！
