import psutil
import time 
import numpy as np

cpu = []

alg = input("Enter alg to use: \n")

try:
    while True:
        cpu.append(psutil.cpu_percent())
        time.sleep(0.08)
except KeyboardInterrupt:
    pass

print (np.max(cpu))
cpu.pop(0)
print(np.max(cpu))
cpu.pop(0)
print (np.max(cpu))
cpu.pop(0)
print (np.max(cpu))
with open(alg+'.txt', 'w') as f:
    for item in cpu:
        f.write("%s\n" % item)

print ("MAX")
print (np.max(cpu))

print ("Average")
print (np.average(cpu))