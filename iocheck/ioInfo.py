
def checkDiskInfo():
    import psutil
    mydic = {}

    for part in psutil.disk_partitions(all=False):
        usage = psutil.disk_usage(part.mountpoint)
        mydic[part.device] = "Total " + sizeof_fmt(usage.total)+", Used "+sizeof_fmt(usage.used)+", Free "+sizeof_fmt(usage.free) +", Percent "+ str(int(usage.percent)) +"%, Format "+part.fstype
    return mydic

def checkDiskIO():
    import psutil
    mydic = psutil.disk_io_counters(perdisk=True)
    return mydic
    

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

checkDiskIO()