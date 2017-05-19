---
title: tcp 三次握手 accpet
date: 2017-05-18 17:22:41
tags: tcp 三次握手 accpet
---

# tcp 三次握手与accpet之间的关系

## tcp 三次握手

```

 client             server
   +                   +
   |                   |
   |    syn k          |
   +------------------->
   |                   |
   |    syn j, ack+1 |
   <-------------------+
   |                   |
   |    ack j+1        |
   +------------------->
   |                   |
```

## tcp 四次挥手

```
 client             server
   +                  +
   |     FIN m        |
   +------------------>
   |     ACK m+1      |
   <------------------+
   |     FIN n        |
   <------------------+
   |     ACK n+1      |
   +------------------>
   |                  |
   |                  |

```

## linux 下 tcp 编程过程

```
server

socket();
bind();
listen();
accept();   // server 端会阻塞，直到有连接成功。
recv();
close();


client 端

socket()
bind();
connect();  // client 端会阻塞，直到连接成功
close();    // 四次挥手开始

```

## linux 下 tcp 过程与 三次握手、四次挥手之前的关系

![linux_tcp.jpg](http://onjwbz75c.bkt.clouddn.com/linux_tcp.jpg)


### tcp 三次握手与 tcp accpet 之间的关系

1. 要 accept需要三次握手完成, 连接请求入tp->accept_queue队列(新为客户端分析的 sk, 也在其中), 其才能出队
2. 为 accept分配一个sokcet结构, 并将其与新的sock关联
3. 如果调用时,需要获取客户端地址,即第二个参数不为 NULL,则从新的 sock 中获取；
4. 将新的 socket 结构与文件系统挂钩；

* 总结：
    accpet 与三次握手的关系是：accpet 必须等待三次握手成功之后，才可以返回。如果没有调用 accept函数，并不会影响 tcp 三次握手。
    如果没有调用 connect函数，不会触发 tcp 三次握手

### tcp 四次挥手 与 tcp 关系

client 调用 close()函数，触发四次挥手。


## 参考

http://blog.chinaunix.net/uid-26971437-id-3949232.html


http://blog.sae.sina.com.cn/archives/2254