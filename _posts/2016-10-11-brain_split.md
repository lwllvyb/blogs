---
title: brain split
date: 2017-04-02 10:35:00
tags: brain distribute
---
# brain split

## 概念

分裂是一个计算机术语,基于与医学分裂-大脑综合症的类比.它表示由于网络设计中的服务器或基于服务器不能相互通信和同步数据的故障条件而导致的数据或可用性不一致。最后一个案例通常也称为网络分区。

## 发生场景

the split-brain syndrome may occur when all of the private links go down simultaneously, but the cluster nodes are still running, each one believing they are the only one running. The data sets of each cluster may then randomly serve clients by their own "idiosyncratic" data set updates, without any coordination with the other data sets.

## 处理方法

### wiki 提供的方法

* 乐观方法

1. 当出现 split-brain 场景时，被隔离的所有节点都正常对外提供服务，这样就可以提供更高的可用性，但是会牺牲掉一些正确性。

1. 当 split-brain 场景结束时，需要手动或者自动等手段来恢复集群中数据的一致性。

* 悲观方法

悲观的方法是以牺牲可用性来保证一致性的。当出现 split-brain 场景时，限制被隔离网络访问来保证一致性。

典型的方案："quorum-consensus", 被隔离的网络只有获取到多数人的投票，才可以提供正常的服务；而获取不到多数人投票的子网络会被自动隔离。

### 常见的方法

1. Quorums

1. 採用Redundant communications。冗余通信的方式，集群中採用多种通信方式，防止一种通信方式失效导致集群中的节点无法通信。

1. Fencing, 共享资源的方式，比方能看到共享资源就表示在集群中，可以获得共享资源的锁的就是Leader。看不到共享资源的，就不在集群中

## zookeeper 处理 brain split

避免这种情况其实也很简单，在slaver切换的时候不在检查到老的master出现问题后马上切换，而是在休眠一段足够的时间，确保老的master已经获知变更并且做了相关的shutdown清理工作了然后再注册成为master就能避免这类问题了，这个休眠时间一般定义为与zookeeper定义的超时时间就够了，但是这段时间内系统可能是不可用的，但是相对于数据不一致的后果我想还是值得的。

## 参考原文：

1. [Split-brain (computing)](https://www.wikiwand.com/en/Split-brain_(computing))

1. **待读** [Split-Brain Consensus](http://www.scs.stanford.edu/14au-cs244b/labs/projects/rygaard.pdf)

1. **待读** [ZooKeeper internal behavior on split brain scenario](http://stackoverflow.com/questions/21380664/zookeeper-internal-behavior-on-split-brain-scenario)

1. **待读** [一种集群脑裂后仲裁处理方法、仲裁存储装置以及系统](https://www.google.com/patents/WO2016107173A1?cl=zh-CN)

1. [Zookeeper和分布式环境中的假死脑裂问题](http://backend.blog.163.com/blog/static/20229412620128911939110/)