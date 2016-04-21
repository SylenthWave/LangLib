# Vim+中文输入法切换解决方案

在中文输入法下使用Vim是一个难题，因为在Input模式转换到Normal模式时输入法并没有自动转换，所以无法使用Normal模式下的命令
所以不得不一遍一遍的切换输入法。这是非常不友好的行为。好在现在有了`fcitx-remote-for-osx`。

解决方案：

 1. 首先我们需要Vim插件`fcitx-vim-osx`
 2. 需要安装`https://github.com/CodeFalling/fcitx-remote-for-osx`
 3. 安装fcitx需要注意的是直接使用Xcode编译

然后有个小问题需要注意，你需要把你键盘设置的默认ABC的英文输入更换成US（美式英文）才能正常使用
