# 配置SSH

SSH是Git中一种特殊的协议，通过SSH协议可以生成公钥私钥进行认证。这样就免去了每次提交或者拉取代码时的密码输入。

## 生成SSH公钥

首先需要查看.ssh/目录下是否已经存在了公钥私钥文件。

    $ cd .ssh/ #如果没有这个目录就创建一个
    $ ls -l

查看是否存在类似id_rsa/id_rsa.pub文件，如果没有或者没有ssh目录。那么可以重新生成一个新的SSH公钥。

    $ ssh-keygen #第一种方式，以本机用户名生成ssh key
    $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com" 生成一个ssh key 使用特定邮箱作为标签 -t：指标签，-b：指文件大小， -C：指commit

随后会要求你输入一个文件名来保存ssh key

    Enter a file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]

之后要求你输入密码和确认密码（如果不需要密码直接回车）

    Enter passphrase (empty for no passphrase): [Type a passphrase]
    Enter same passphrase again: [Type passphrase again]


## 添加秘钥到ssh-agent

确保 ssh-agent 是可用的。ssh-agent是一种控制用来保存公钥身份验证所使用的私钥的程序，其实ssh-agent就是一个密钥管理器，运行ssh-agent以后，使用ssh-add将私钥交给ssh-agent保管，其他程序需要身份验证的时候可以将验证申请交给ssh-agent来完成整个认证过程。

首先要确保ssh-agent启用

    eval "$(ssh-agent -s)"

添加上一步中生成的私钥存进ssh中

    $ ssh-add ~/.ssh/id_rsa


最后可以将公钥储存进托管网站（github、bitbucket)或者自己的git服务器中。

## 验证

如果使用github可以使用一下命令验证是否授权成功

    ssh -T git@github.com

    Hi username! You've successfully authenticated, but GitHub does not
    provide shell access. #成功后返回


