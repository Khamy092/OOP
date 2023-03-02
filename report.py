import platform
import psutil

def report():
    print("Device Report\n")
    
    # Get system information
    print("System:", platform.system())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())

    # Get memory information
    mem = psutil.virtual_memory()
    total_mem = mem.total / (1024 ** 2)
    print("Total Memory: {:.2f} GB".format(total_mem))
    # Get storage information
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.device)
        print(f'{partition.device} with total size {round(usage.total / (1024 ** 3))} GB')

report()