---
title: jump consist hash
date: 2017-04-10 22:11:40
tags: hash
---
# jump consist hash

## 应用

1. 应用的 shard

一致性哈希缓存还被扩展到分布式存储系统上。数据被分成一组Shard,每个Shard由一个节点管理，当需要扩容时，我们可以添加新的节点，然后将其它Shard的一部分数据移动到这个节点上。比如我们有10个Shard的分布式存储系统，当前存储了120个数据，每个Shard存储了12个数据。当扩容成12个Shard时，我们从每个Shard上拿走2个数据，存入到新的两个Shard上,这样每个Shard都存储了10个数据，而整个过程中我们只移动了20/120=1/6的数据。

## 完整代码

```c
int32_t JumpConsistentHash(uint64_t key, int32_t num_buckets) {
    int64_t b = -1, j = 0;
    while (j < num_buckets) {
        b = j;
        key = key * 2862933555777941757ULL + 1;
        j = (b + 1) * (double(1LL << 31) / double((key >> 33) + 1));
    }
    return b;
}
```

## 特性

### 增加 bucket

增加bucket 对于 移动的数据是理论最小值 1 / n
如果初始bucket为10，增加1个bucket，则需要移动的数据为1/11

### 移除 bucket

因为Jump consistent hash算法不使用节点挂掉，如果你真的有这种需求，比如你要做一个缓存系统，你可以考虑使用ketama算法，或者对Jump consistent hash算法改造一下：节点挂掉时我们不移除节点，只是标记这个节点不可用。当选择节点时，如果选择的节点不可用，则再一次Hash，尝试选择另外一个节点。

```c
int32_t JumpConsistentHash(uint64_t key, int32_t num_buckets) {
    int64_t i = 0;
    for (;i < 3; i++)
    {
        int64_t b = -1, j = 0;
        while (j < num_buckets) {
            b = j;
            key = key * 2862933555777941757ULL + 1;
            j = (b + 1) * (double(1LL << 31) / double((key >> 33) + 1));
        }
        if isAlive(b)
        {
            return b;
        }
    }
}
```

## 参考文章
1. [【翻译/介绍】jump Consistent hash:零内存消耗，均匀，快速，简洁，来自Google的一致性哈希算法](https://blog.helong.info//blog/2015/03/13/jump_consistent_hash/)
1. [一个速度快内存占用小的一致性哈希算法](http://colobu.com/2016/03/22/jump-consistent-hash/)