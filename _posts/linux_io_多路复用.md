---
title: linux io 多路复用
date: 2017-05-20 22:26:49
tags: linux io epoll select poll
---
# linux io 模型

## select、poll 和 epoll

### select、poll

* 基本流程

int select(int maxfdp1,fd_set *readset,fd_set *writeset,fd_set *exceptset,const struct timeval *timeout)

int poll ( struct pollfd * fds, unsigned int nfds, int timeout);

* 特点

1. 监视的fds 有限制，1024个。
1. 每次调用的时候，需要将所有监视的 socket fds 从用户态拷贝至内核态
1. 事件发生，需要遍历所有的 socket fds ，来确定对应的 fd 是否发生
1. 需要监听的事件较少，且同时 发生事件的情况

### epoll

* 基本流程

epoll_create()
epoll_ctl()
epoll_wait()

* 特点

1. 监视的 fds 有限制，cat /proc/sys/fs/file-max
1. 只有在调用 epoll_ctl 增加 socket fd 时，才会从用户态将 fd 拷贝至内核态。
1. epoll_wait 只会返回有事件发生的 socket fds
1. 监听的事件较多，同时只有少量事件

* 触发方式

1. LT(Level Triggered) 水平触发

只要对应的 socket fd 中有对应事件，epoll_wait 就会返回。

因为LT 的特性，只要对应的事件还有数据，就会触发epoll_wait, 因此是否设置对应的socket fd 为 NonBlock都可以。

1. ET(Edged Triggered) 边缘触发

对应的socket fd 中有对应的事件，只会触发一次epoll_wait，随后只有新的事件，epoll_wait 才会返回。

因为ET 的特性，所欲在触发epoll_wait 之后，需要将所有消息读取出来，就需要使用while循环，如果是 Block ，recv 接收到最后，没有数据就会被阻塞，因此需要设置为 non block

## 为什么不使用多线程或者多进程？

多进程或者多线程，会耗费大量资源，可扩展性差。

## C 10k 问题


## 使用Linuxepoll模型，水平触发模式；当socket可写时，会不停的触发socket可写的事件，如何处理？

解答：正如我们上面说的，LT模式下不需要读写的文件描述符仍会不停地返回就绪，这样就会影响我们监测需要关心的文件描述符的效率。
所以这题的解决方法就是：平时不要把该描述符放进eventpoll结构体中，当需要写该fd的时候，调用epoll_ctl把fd加入eventpoll里监听，可写的时候就往里写，写完再次调用epoll_ctl把fd移出eventpoll，这种方法在发送很少数据的时候仍要执行两次epoll_ctl操作，有一定的操作代价 
改进一下就是：平时不要把该描述符放进eventpoll结构体中，需要写的时候调用write或者send写数据，如果返回值是EAGAIN（写缓冲区满了），那么这时候才执行第一种方法的步骤。

## 为什么 epoll 需要设置 socket 为 non block 模式 ?

因为LT 的特性，只要对应的事件还有数据，就会触发epoll_wait, 因此是否设置对应的socket fd 为 NonBlock都可以。

因为ET 的特性，所欲在触发epoll_wait 之后，需要将所有消息读取出来，就需要使用while循环，如果是 Block ，recv 接收到最后，没有数据就会被阻塞，因此需要设置为 non block




http://www.voidcn.com/blog/drdairen/article/p-6357891.html
http://www.cnblogs.com/yuuyuu/p/5103744.html