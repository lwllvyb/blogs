---
title: brain split
date: 2017-04-02 10:35:00
tags: brain distribute
---

## 参考原文：

1. [Split-brain (computing)](https://www.wikiwand.com/en/Split-brain_(computing))

1. **待读** [Split-Brain Consensus](http://www.scs.stanford.edu/14au-cs244b/labs/projects/rygaard.pdf)

# brain split

## 概念

分裂是一个计算机术语,基于与医学分裂-大脑综合症的类比.它表示由于网络设计中的服务器或基于服务器不能相互通信和同步数据的故障条件而导致的数据或可用性不一致。最后一个案例通常也称为网络分区。

## 发生场景

the split-brain syndrome may occur when all of the private links go down simultaneously, but the cluster nodes are still running, each one believing they are the only one running. The data sets of each cluster may then randomly serve clients by their own "idiosyncratic" data set updates, without any coordination with the other data sets.

## 处理方法

* 乐观方法

1. 当出现 split-brain 场景时，被隔离的所有节点都正常对外提供服务，这样就可以提供更高的可用性，但是会牺牲掉一些正确性。

1. 当 split-brain 场景结束时，需要手动或者自动等手段来恢复集群中数据的一致性。

* 悲观方法

悲观的方法是以牺牲可用性来保证一致性的。当出现 split-brain 场景时，限制被隔离网络访问来保证一致性。

典型的方案："quorum-consensus", 被隔离的网络只有获取到多数人的投票，才可以提供正常的服务；而获取不到多数人投票的子网络会被自动隔离。