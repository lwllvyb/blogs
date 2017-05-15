---
title: swap
date: 2017-05-15 20:48:45
tags: swap
---
{dd if=/dev/zero of=/swapfile bs=1024 count=65536& 生成一个64m的文件
mkswap /swapfile  创建交换文件
swapon –a  /swapfile  打开交换文件
}