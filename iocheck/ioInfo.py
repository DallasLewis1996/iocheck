
def checkIO():
    import psutil
    mydic = {}
    mydic = psutil.disk_io_counters('/')

    return mydic
print(checkIO())