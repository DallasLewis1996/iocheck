
def checkIO():
    import psutil
    return psutil.disk_io_counters('/')
