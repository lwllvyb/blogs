---
title: linux io 多路复用
date: 2017-05-20 22:26:49
tags: linux io epoll select poll
---
# linux io 模型

## select、poll 和 epoll

## 为什么不使用多线程或者多进程？

## C 10k 问题


## 使用Linuxepoll模型，水平触发模式；当socket可写时，会不停的触发socket可写的事件，如何处理？

解答：正如我们上面说的，LT模式下不需要读写的文件描述符仍会不停地返回就绪，这样就会影响我们监测需要关心的文件描述符的效率。
所以这题的解决方法就是：平时不要把该描述符放进eventpoll结构体中，当需要写该fd的时候，调用epoll_ctl把fd加入eventpoll里监听，可写的时候就往里写，写完再次调用epoll_ctl把fd移出eventpoll，这种方法在发送很少数据的时候仍要执行两次epoll_ctl操作，有一定的操作代价 
改进一下就是：平时不要把该描述符放进eventpoll结构体中，需要写的时候调用write或者send写数据，如果返回值是EAGAIN（写缓冲区满了），那么这时候才执行第一种方法的步骤。 

## 为什么 epoll 需要设置 socket 为 non block 模式 ?





http://www.voidcn.com/blog/drdairen/article/p-6357891.html