# Git撤销命令

## git reset

`git reset`命令可以将当前状态撤销到某个commit节点，此节点之前的commit都会被撤销。**特别注意：尽量在本地分支上使用reset命令，因为如果在线上分支使用reset命令会导致commit消失，会对使用当前分支的其他开发者造成困惑**

 `git reset`使用场景

1. 通常如果我们将未跟踪文件（Untracked files）添加到暂缓存（staged）中后，如果想要将其从暂缓存中撤销即可使用`git reest`命令。
    ```
    git reset HEAD filename
    ```
2. 如果要撤销某个commit可以使用该命令
    ```
    git reset HEAD
    ```

## git checkout

`checkout`命令用于切换commit和branch。但如果对已跟踪的文件进行了修改(Modified)可以使用`checkout`命令进行撤销。
```
git checkout filename
```

## git revert

`git revert`命令是将某个commit恢复，也就是将某个commit撤销。它不会删除之前已经存在的commit，它会从新让你提交一个revert后的commit。所以对于撤销操作来说这个命令是安全的。

```
git revert HEAD
```
