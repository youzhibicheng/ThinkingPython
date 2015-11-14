introduce the command used in linux shell
ps -aux
top
lsof
	list open files
netstate
ifconfig
who
df
kill
free
nice
	nice - run a program with modified scheduling priority
	调整进程优先级
	优先级的范围为-20 ～ 19 等40个等级，其中数值越小优先级越高，数值越大优先级越低，既-20的优先级最高， 19的优先级最低。若调整后的程序运行优先级高于-20，则就以优先级-20来运行命令行；若调整后的程序运行优先级低于19，则就以优先级19来运行命令行。若 nice命令未指定优先级的调整值，则以缺省值10来调整程序运行优先级，既在当前程序运行优先级基础之上增加10。
	# nice
	# nice nice
	# nice -n -21 nice
	# nice --adjustment=20 nice
ionice
iostat
	# yum search iostat
	# yum -y install pcp-import-iostat2pcp.x86_64
	%steal
		Show the percentage of time spent in involuntary wait by the virtual CPU or CPUs while the hypervisor was servicing another virtual processor.
	%steal：管理程序维护另一个虚拟处理器时，虚拟CPU的无意识等待时间百分比。
iotop
	yum -y install iotop
uptime
	tell how long the system has run
pidof
	find the pid of a running program
tty
taskset
	retrieve or set a process's CPU affinity
	taskset 是 Linux 系统当中，用于查看、设定 CPU 核使用情况的命令
	# yum -y install util-linux-ng
	使用默认的行为，用给定的 CPU 核运行位标记运行一个进程
	taskset mask command [arguments]
	获取一个指定进程的 CPU 核运行位标记
	taskset -p pid
	设定一个指定进程的 CPU 核运行位标记
	taskset -p mask pid

	1. 查看物理CPU的个数
	#cat /proc/cpuinfo | grep "physical id"| sort |uniq|wc –l
	2.  查看逻辑CPU的个数
	#cat /proc/cpuinfo |grep "processor"|wc –l
	3. 查看CPU是几核
	#cat /proc/cpuinfo |grep "cores"|uniq
	4. 查看CPU的主频
	#cat /proc/cpuinfo |grep MHz|uniq 
pmap
	pmap - report memory map of a process
	Pmap 提供了进程的内存映射，pmap命令用于显示一个或多个进程的内存状态。其报告进程的地址空间和内存状态信息
vmstat

mpstat
	yum -y install opensips-snmpstats.x86_64
	mpstat是Multiprocessor Statistics的缩写，是实时系统监控工具。其报告与CPU的一些统计信息，这些信息存放在/proc/stat文件中。在多CPUs系统里，其不但能查看所有CPU的平均状况信息，而且能够查看特定CPU的信息。mpstat最大的特点是：可以查看多核心cpu中每个计算核心的统计数据；而类似工具vmstat只能查看系统整体cpu情况。
psutil
https://pypi.python.org/pypi/psutil
pip install psutil
