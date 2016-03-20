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

打印Commit，-p打印跟上一次commit之间的变化，-num（数字）commit数。

	$ git log -p -10

打印状态

	$ git log --stat

打印一行信息

	$ git log --pretty=oneline
    $ git log --oneline #打印一行内容（缩短了哈希字符长度）

格式化输出

	$ git log --pretty=format::"%h - %an, %ar : %s"

打印branch和commit的信息

    $ git log --oneline --decorate

打印整个commit和branch关系图

    $ git log --oneline --decorate --graph --all

## git checkout

如果修改了某个文件，他会被git标记为`modified`，如果你想要放弃这个修改。那么可以使用`checkout` 命令

	$ git checkout -- filename

对于分支来说，checkout命令可以跳转到任意分支

    $ git checkout [branchname]

可以使用`checkout`命令创建一个新的分支，根据当前的commit。

    $ git checkout -b [branchname]

在Clone一个新项目时，git会自动创建一个名为master的分支，用来表示远程仓库中的主分支。如果远程仓库中还有其他分支，在clone的时候他并不会将其他分支拉取到本地，所以如果你需要拉取远程仓库中其他分支的代码。可以使用如下命令：

    $ git checkout -b [branchname] origin/[remotename]
    $ git checkout --track origin/[remotename]

## git remote

一个新建的项目初始化后并没有远程仓库的地址，需要我们手动添加。命令如下：git remote add <shortname> <url>，也可以用此命令增加一个远程仓库地址

	$ git remote add origin git@github.com/useremail/username

使用git remote show [remote-name]命令显示远程仓库中的分支详情

	$ git remote show origin

使用-v来打印Git储存的远程仓库地址

	$ git remote -v

使用`ls-remote`打印远程分支信息

    $ git ls-remote origin

## git fetch

	$ git fetch [remote-name]

fetch命令会从下载远程仓库中的所有分支。使用`fetch`命令仅仅是下载数据至仓库中。并不会和当前仓库代码进行合并。

如果需要你可以创建一个全新的分支来管理`fetch`到的仓库

    $ git fetch origin
    $ git checkout -b developer origin/developer

也可以使用如下方式

    $ git checkout --track origin/developer



## git push

	$ git psuh [remote-name] [remote-brance]

使用push命令将当前仓库代码更新到远程仓库中去。

    $ git push origin master

上述命令是push本地master代码到远程仓库。

    $ git push origin developer

如上命令是将developer分支代码提交到远程仓库

    $ git push origin developer:dev

如果你不想用当前分支的名字作为远程仓库中分支的名字的话，可以使用上述命令更改远程仓库分支名称

    $ git push origin --delete [branchname]

使用上述方法可以删除远程分支。

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

## git branch

创建分支

    $ git branch testing #创建一个名为testing的分支

跳转分支

    $ git checkout testing # 创建完分支后HEAD并不会自动指向该分支需要手动跳转到该分支

创建并跳转分支,使用的是checkout命令

    $ git checkout -b testing

删除分支命令

    $ git brance -d [branchname]

查看已经合并过的分支

    $ git branch --merged

查看还没合并过的分支

    $ git branch --no-merged

## git merge

合并分支操作:以从`testing`分支到`master`分支为例

    $ git branch testing # 首先创建一个分支
    $ git checkout testing # 跳转到该分支
    # do something
    $ git commit -a -m 'testing' # 提交

    $ git checkout master # 如果需要合并分支，首先要跳转回原分支。
    $ git merge testing # 合并操作

* 如果`test`分支只是新添加了一些文件或者没有和`master`分支改变同一个文件，并且主动合并分支落后于被合并分支，合并的时候就会显示`Fast-forward`
* 如果`test`分支和`master`分支都改变了一些文件，但不是同一个文件。那么当merge的时候会显示`Merge made by the 'recursive' strategy`。
* 如果`test`分支和`master`分支都改变了同一个文件，那么就很可能发生冲突，这时候merge会显示`Conflict`。

如果发生冲突可以使用`mergetool`来解决冲突。

    $ git mergetool

# git rebase

`rebase`是合并分支时用到的第二个方法，试想一下，如果当前有两个分支（dev，master)，都修改了不同的文件并提交。那么当你想把dev中的修改合并到master时就需要两步：
1. 切换到master分支
2. 合并dev分支到master分支

而使用`rebase`命令就会重新走一遍master的commit过程。这样也就是dev分支现在最顶端，并且有了master的代码。所以只需切换回master然后合并dev分支的代码即可(`fast-forward`合并。
1. 使用`$ git rebase master`
2. 切换到master分支
3. 合并dev分支代码

所以使用`rebase`提交的commit就会是一条直线。

还有一种情况是，当有三条分支时，如果将最外层分支的代码合并到`master`分支而不影响他们之间的分支。可以使用如下命令

    $ git rebase --onto master branch1 branch2

它和merge是不同的，由于branch2是基于branch1的分支，如果是将branch2合并到master上的话，会将branch1中的commit合并到master中。












