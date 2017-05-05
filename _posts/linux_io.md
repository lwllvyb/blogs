---
title: linux io path
date: 2017-05-05 18:53:27
tags: linux io
---
# linux io

![linux_io_1.gif](http://onjwbz75c.bkt.clouddn.com/linux_io_1.gif)
![linux_io_2.jpg](http://onjwbz75c.bkt.clouddn.com/linux_io_2.jpg)


## application process

应用程序：这没什么好说的，通过IO相关系统调用(如open/read/write)发起IO请求，属于IO请求的源头


## file system

文件系统：应用程序的请求直接到达文件系统层。文件系统又分为VFS和具体文件系统（ext3、ext4等），VFS对上层提供统一的访问接口，而ext3等文件系统则是具体实现。另外，在这个层次，为了效率考虑，该层次也实现了page cache等功能。同时，用户也可以选择绕过page cache，而是直接使用direct模式进行IO（如数据库）。

## block io layer

块设备层：文件系统将IO请求打包提交给块设备层，该层会对这些IO请求作合并、排序、调度等，然后以新的格式发往更底层。在该层次上实现了多种电梯调度算法，如cfq、deadline等。

## scsi layer

SCSI层：块设备层将请求发往SCSI层，SCSI就开始真实处理这些IO请求，但是SCSI层又对其内部按照功能划分了不同层次：
SCSI高层：高层驱动负责管理disk，接收块设备层发出的IO请求，打包成SCSI层可识别的命令格式，继续往下发；
SCSI中层：中层负责通用功能，如错误处理，超时重试等
SCSI低层：底层负责识别物理设备，将其抽象提供给高层，同时接收高层派发的scsi命令，交给物理设备处理。