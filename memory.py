import os
import sys 
import tabulate 
import psutil 
import platform 
import time 
import datetime 
from datetime import datetime 

os.system(' clear ')

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

time.sleep(0.1)
print("="*40, "Memory Information", "="*40)
svmem = psutil.virtual_memory()
time.sleep(0.1)
print(f"Total: {get_size(svmem.total)}")
time.sleep(0.1)
print(f"Available: {get_size(svmem.available)}")
time.sleep(0.1)
print(f"Used: {get_size(svmem.used)}")
time.sleep(0.1)
print(f"Percentage: {svmem.percent}%")
time.sleep(0.1)
print("="*40, "SWAP", "="*40)