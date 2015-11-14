__author__ = 'james'

import psutil

# About CPU
pcpu = psutil.cpu_times()
print pcpu.user, pcpu.system

# About IO

# About Network
