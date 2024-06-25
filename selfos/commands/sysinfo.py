import os
from datetime import datetime as dt

__doc__ = "Shows the system information. Usage: sysinfo"

def run(dir, *args):
    """ Shows the system information. """
    
    # Get the current date and time.
    sysinfo = dt.now().strftime("%A, %B %d, %Y %I:%M:%S %p")
    
    # Get the system information.
    info = os.uname()
    sysinfo += f"\nSystem : {info.sysname} {info.release} {info.version}"
    
    # Add disk information.
    diskinfo = os.statvfs('/')
    disksize = diskinfo.f_frsize * diskinfo.f_blocks
    diskfree = diskinfo.f_frsize * diskinfo.f_bfree
    sysinfo += f"\nDisk   : {diskfree / 2**20:.2f} of {disksize / 2**20:.2f} MB free ({diskfree / disksize * 100:.2f}%)"
    
    # Add memory information.
    meminfo = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    sysinfo += f"\nMemory : {meminfo / 2**20:.2f} MB"
    
    # Add CPU information.
    cpuinfo = os.cpu_count()
    sysinfo += f"\nCPU    : {cpuinfo} cores"
    
    return sysinfo, False