#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2018.5.2
Finished on 2018.5.2
@author: Wang Yuntao
"""

import psutil
import datetime
import platform
import win_unicode_console

win_unicode_console.enable()


def unit_conversion(value):
    """
    unit conversion -> ["B", "KB", "MB", "GB", "TB"]
    :param value: the input value
    :return
        new value with new unit and its unit
    """
    if 0 < value < 1024:
        return value, " B"
    elif 1024 < value < 1024 ** 2:
        return value / 1024, " KB"
    elif 1024 ** 2 < value < 1024 ** 3:
        return value / 1024 / 1024, " MB"
    elif 1024 ** 3 < value < 1024 ** 4:
        return value / 1024 / 1024 / 1024, " GB"
    else:
        return value / 1024 / 1024 / 1024 / 1024, " TB"


def get_system_info():
    """
    Get the information of operation system
    :param 
        NULL
    :return
        system: the system of the current machine
    """
    user = psutil.users()[0].name
    system = platform.platform()
    machine = platform.machine()
    node = platform.node()
    processor = platform.processor()
    print("User: %s, OS: %s, Machine: %s, Host: %s\nprocessor: %s"
          % (user, system, machine, node, processor))

    return system


def get_open_time():
    """
    Get the open time of the current machine
    :param 
        NULL
    :return
        start_time: the strat time of the current machine
    """
    start_time_stamp = psutil.boot_time()
    start_time = datetime.datetime.fromtimestamp(start_time_stamp).strftime("%Y-%m-%d %H:%M:%S")
    
    return start_time


def get_run_time():
    """
    get run time of the current machine
    :param 
        NULL
    :return
        run_time: the run time of the current machine
    """

    start_time = datetime.datetime.utcfromtimestamp(psutil.boot_time())
    current_time = datetime.datetime.now()
    run_time = current_time - start_time
    return run_time


def get_cpu_info():
    """
    Get the information of CPU
    """
    cpu_number = psutil.cpu_count()
    cpu_frquency = psutil.cpu_freq().current / 1000
    cpu_utilization = psutil.cpu_percent()
    print("Kernel: %d, Frequency: %.1f GHz, Usage: %.1f%%" 
          % (cpu_number, cpu_frquency, cpu_utilization))


def get_virtual_memory_info():
    """
    Get the information of virtual memory
    """
    virtual_memory = psutil.virtual_memory()
    memory_total, unit_total = unit_conversion(virtual_memory.total)
    memory_used, unit_used = unit_conversion(virtual_memory.used)
    memory_free, unit_free = unit_conversion(virtual_memory.free)
    utilization_ratio = memory_used / memory_total * 100

    print("Virtual memory - Total memory: %.1f%s, Used memory: %4.1f%s, Free memory: %.1f%s, Memory utilization: %.1f%%"
          % (memory_total, unit_total, memory_used, unit_used, memory_free, unit_free, utilization_ratio))

    return memory_total, memory_used, memory_free, utilization_ratio


def get_swap_memory_info():
    """
    Get the information of virtual memory
    """
    swap_memory = psutil.swap_memory()
    memory_total, unit_total = unit_conversion(swap_memory.total)
    memory_used, unit_used = unit_conversion(swap_memory.used)
    memory_free, unit_free = unit_conversion(swap_memory.free)
    utilization_ratio = memory_used / memory_total * 100

    print("Swap memory    - Total memory: %.1f%s, Used memory: %.1f%s, Free memory: %.1f%s, Memory utilization: %.1f%%"
          % (memory_total, unit_total, memory_used, unit_used, memory_free, unit_free, utilization_ratio))


def get_disk_info():
    """
    Get the information of disks
    """
    partition = psutil.disk_partitions()
    
    for part in partition:
        device = part.device
        fstype = part.fstype
        opts = part.opts
        if "rw" not in opts:
            print("drive: %s, opts: %s" % (device, opts))
        else:
            storage = psutil.disk_usage(device)
            storage_total, unit_total = unit_conversion(storage.total)
            storage_used, unit_used = unit_conversion(storage.used)
            storage_free, unit_free = unit_conversion(storage.free)
            utilization_ratio = storage.percent

            print("drive: %s, type: %s, opts: %s, total storage: %6.2f%s, used storage: %6.2f%s, free storage: %6.2f%s, utilization_ratio: %3.1f%%"
                  % (device, fstype, opts, storage_total, unit_total, storage_used, unit_used, storage_free, unit_free,  utilization_ratio))


if __name__ == "__main__":
    print("The information of the current machine.")
    print("The current machine is started at %s, and has been run for %s" % (get_open_time(), get_run_time()))
    print("--------------------------------------------System--------------------------------------------")
    get_system_info()
    print("---------------------------------------------CPU----------------------------------------------")
    get_cpu_info()              # cpu
    print("--------------------------------------------Memory--------------------------------------------")
    get_virtual_memory_info()   # virtual memory
    get_swap_memory_info()      # swap memory
    print("-------------------------------------------Storage--------------------------------------------")
    get_disk_info()             # disk
    
