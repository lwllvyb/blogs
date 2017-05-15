---
title: page cache vs buffers cache
date: 2017-05-15 20:48:13
tags: page cache buffers cache
---
http://blog.csdn.net/delacroix_xu/article/details/5434770
buffers是指用来给块设备做的缓冲大小，他只记录文件系统的metadata以及 tracking in-flight pages.

　　cached是用来给文件做缓冲。

　　那就是说：buffers是用来存储，目录里面有什么内容，权限等等。而cached直接用来记忆我们打开的文件，如果你想知道他是不是真的生效，你可以试一下，先后执行两次命令#man X ,你就可以明显的感觉到第二次的开打的速度快很多。
