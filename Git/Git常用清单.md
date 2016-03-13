## git config

Git的全局配置在`.gitconfig`文件中 。

    $ vim .gitconfig

也可以使用命令

	$ git config --global key.name

还可以使用list命令打印所有config属性

	$ git config --list

## git clone

创建一个Git Repository(仓库)有多种方式，第一种是使用`init`命令

	$ git init

第二种是从一个项目上克隆，命令如下:

	$ Git clone https://github.com/libgit2/libgit2

这条命令会在根目录上创建一个libgit2目录，然后将github上面的项目完整的clone的该目录上.


	$ Git clone https://github.com/libgit2/libgit2 mydirectory/dir

如果想要Clone到一个自定目录只需在上一条命令的基础上增加目录名即可。

## .gitignore

在项目目录中创建一个.gitignore文件，可以在这个文件中写一些正则表达式来使Git忽略一些文件。

```
# no .a filet
*.a

# but do track lib.a, even though you're ignoring .a file above
 !lib.a
 
# only ignore the TODO file in the current directory, no subdir/TODO
 /TODO

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory
doc/**/*.pdf
```

## git diff

* `git diff` : 参看更改内容的命令，其中git diff 命令查看的是还没有加入暂缓存区域文件的不同。
* `git diff --staged` ：查看的是已经加入暂缓存区域文件与上一次commit之间的比较。
* `git diff --cached` ：同上

## git commit

* `git commit -m 'some message'` ：提交暂缓存区域中的文件，并且使用`-m`后的字符串作为提交说明。
* `git commit -a -m 'some message'` : 先将目录中没有暂缓存的文件放入暂缓存区域，然后使用`-m`后的`message`字符串提交变更。
* `git commit --amend` ：如果一次提交后还有忘了提交的文件，可以使用`--amend`命令合并提交。

## git rm

删除命令，比如已经在暂缓存区域中的文件被删除，那么该文件的状态由modified变为delete，然后可以使用git rm file_name 删除对该文件的跟踪。使用git rm 同样可以将暂缓存区域中的文件删除至未跟踪状态。

	$ rm file1
	$ git rm file1

## git mv

重命名命令，使用该命令的文件必须是已跟踪文件。它等价于先重命名->删除前文件->添加重命名后的文件到暂缓存区域。

	$ mv file1 file2
	$ git rm file1
	$ git add file2

## git log

打印Commit，-p打印跟上一次commit之间的变化，-num（数字）打印变化的行数。

	$ git log -p -10
	$ git log --stat #  打印状态
	$ git log --pretty=oneline #打印一行
	$ git log --pretty=format::"%h - %an, %ar : %s" # 按指定格式打印

## git checkout

如果修改了某个文件，他会被git标记为`modified`，如果你想要放弃这个修改。那么可以使用`checkout` 命令

	$ git checkout -- filename

对于分支来说，checkout命令可以跳转到任意分支

    $ git checkout [branchname]


## git remote

一个新建的项目初始化后并没有远程仓库的地址，需要我们手动添加。命令如下：git remote add <shortname> <url>

	$ git remote add origin git@github.com/useremail/username

使用git remote show [remote-name]命令显示远程仓库中的分支详情

	$ git remote show origin

使用-v来打印Git储存的远程仓库地址

	$ git remote -v

使用-v来打印Git储存的远程仓库地址


## git fetch

	$ git fetch [remote-name]

fetch命令会从下载远程仓库中的所有分支。使用`fetch`命令仅仅是下载数据至仓库中。并不会和当前仓库代码进行合并。

## git push

	$ git psuh [remote-name] [remote-brance]

使用push命令将当前仓库代码更新到远程仓库中去。

## git tag

使用git可以为一个特殊的时间点创建一个`tag`，通常我们用它来标记版本。

	$ git tag # list tags
	$ git tag -l "v1.*" # list tags use pattern

创建一个`tag`有两种方式：

* 第一种是轻量方式，它仅仅是指向某个节点的指针，不包含任何其他信息。
* 第二种是有注释方式，它是被推荐使用的方式，因为可以携带更多关于tag的信息


	$ git tag v1.0 # create a tag
	$ git tag -a v1.0 -m "my version 1.0" # create a tag


轻量`tag`创建方式不需要 `-a -m` 命令。它类似一个`commit`。
其中的m命令需要给tag一个描述信息，如果没有传这个命令它会自动开启默认编辑器要求填写相关信息。

如果想标记历史中的某个commit也非常简单，只需要在创建后添加commit的哈希字符串即可。

	$ git tag -a v1.2 9fceb02

默认情况下tag并不会上传到远程仓库中去，你需要显式的将本地仓库中的tag推送到远程仓库中。方法就和推送commit一样。

	$ git push origin v1.0
	$ git push origin --tags


如果你需要创建一个特殊版本的分支可以使用 `git checkout -b [branchname] [tagname]`

	$ git checkout -b version1.0 v1.0


## git aliases

可以为Git命令创建一些别名，方法如下：

	$ git config --local alias.s status
	$ git config --global alias.s status

还可以是一组命令

    $ git config --local alias.last 'log -l HEAD'

