import psutil
"""
获取CPU信息
"""
# CPU逻辑数量
# 2说明是双核超线程, 4则是4核非超线程
print(psutil.cpu_count())

# CPU物理核心
print(psutil.cpu_count(logical=False))

# 统计CPU的用户／系统／空闲时间
print(psutil.cpu_times())

# 实现类似top命令的CPU使用率，每秒刷新一次，累计10次
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))
"""
获取内存信息
"""
# 使用psutil获取物理内存
print(psutil.virtual_memory())

# 使用psutil获取交换内存信息
print(psutil.swap_memory())
"""
获取磁盘信息
"""
# 通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息
print(psutil.disk_partitions())  # 磁盘分区信息
print(psutil.disk_usage('C:\\'))  # 磁盘使用情况
print(psutil.disk_io_counters())  # 磁盘IO
"""
获取网络信息
"""
# psutil可以获取网络接口和网络连接信息
print(psutil.net_io_counters())  # 获取网络读写字节／包的个数
print(psutil.net_if_addrs())  # 获取网络接口信息
print(psutil.net_if_stats())  # 获取网络接口状态

# 要获取当前网络连接信息，使用net_connections()
print(psutil.net_connections())
"""
获取进程信息
"""
print("===============================进程信息===============================")
print(psutil.pids())  # 所有进程ID
p = psutil.Process(6872)  # 获取指定进程ID=3776
print(p.name())  # 进程名称
print(p.exe())  # 进程exe路径
print(p.cwd())  # 进程工作目录
print(p.cmdline())  # 进程启动的命令行
print(p.ppid())  # 父进程ID
print(p.parent())  # 父进程
print(p.children())  # 子进程列表
print(p.status())  # 进程状态
print(p.username())  # 进程用户名
print(p.create_time())  # 进程创建时间
print(p.terminal())  # 进程终端
print(p.cpu_times())  # 进程使用的CPU时间
print(p.memory_info())  # 进程使用的内存
print(p.open_files())  # 进程打开的文件
print(p.connections())  # 进程相关网络连接
print(p.num_threads())  # 进程的线程数量
print(p.threads())  # 所有线程信息
print(p.environ())  # 进程环境变量
# print(p.terminate())  # 结束进程

