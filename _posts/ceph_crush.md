---
title: ceph crush
date: 2017-04-11 10:51:12
tags: ceph crush
---
# ceph crush

## ceph crush 分成两步

### 逻辑层

> Ceph为了保存一个对象，对上构建了一个逻辑层，也就是池(pool)，用于保存对象，这个池的翻译很好的解释了pool的特征，如果把pool比喻成一个中国象棋棋盘，那么保存一个对象的过程就类似于把一粒芝麻放置到棋盘上。

> Pool再一次进行了细分，即将一个pool划分为若干的PG(归置组 Placement Group)，这类似于棋盘上的方格，所有的方格构成了整个棋盘，也就是说所有的PG构成了一个pool。

### 1. 计算PG(obj'name -> pg_id)

> 对于对象名分别为bar和foo的两个对象，对他们的对象名进行计算即:
HASH(‘bar’) = 0x3E0A4162

> PG的实际编号是由pool_id+.+PG_id
0x3E0A4162 % 0xFF ===> 0x62
如果bar、foo 保存在pool=0中，则对应的pg 为 0.62 这个 PG 里

### 2. 计算OSD(pg_id -> bucket_id)

## 使用HASH代替CRUSH？

> 在讨论CRUSH算法之前，我们来做一点思考，可以发现，上面两个计算公式有点类似，为何我们不把

> CRUSH(PG_ID) ===> OSD
改为
HASH(PG_ID) %OSD_num ===> OSD
我可以如下几个由此假设带来的副作用：

> 如果挂掉一个OSD，OSD_num-1，于是所有的PG % OSD_num的余数都会变化，也就是说这个PG保存的磁盘发生了变化，对这最简单的解释就是，这个PG上的数据要从一个磁盘全部迁移到另一个磁盘上去，一个优秀的存储架构应当在磁盘损坏时使得数据迁移量降到最低，CRUSH可以做到。
如果保存多个副本，我们希望得到多个OSD结果的输出，HASH只能获得一个，但是CRUSH可以获得任意多个。
如果增加OSD的数量，OSD_num增大了，同样会导致PG在OSD之间的胡乱迁移，但是CRUSH可以保证数据向新增机器均匀的扩散。
所以HASH只适用于一对一的映射关系计算，并且两个映射组合(对象名和PG总数)不能变化，因此这里的假设不适用于PG->OSD的映射计算。因此，这里开始引入CRUSH算法。

## 参考

1. [大话Ceph--CRUSH那点事儿](http://xuxiaopang.com/2016/11/08/easy-ceph-CRUSH/)