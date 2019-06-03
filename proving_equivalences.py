#! /usr/bin/python3
import sys

N = 2
M = []
for line in sys.stdin:
    AB = line.split()
    M.extend(AB)
N = int(M[0])
in1 = str(M[1])
in2 = str(M[2])

if N%2 == 0: #OM JÄMNT ANTAL ÖVERSKRIVNINGAR
    if  in1==in2:
        print("Deletion succeeded")

    else:
        print("Deletion failed")

else: # OM UDDA ANTAL ÖVERSKRIVNINGAR
    in1_list = list(in1)
    in1_list = [int(i) for i in in1_list]
    in2_list = list(in2)
    in2_list = [int(i) for i in in2_list]
    
    new_list = []
    for i in range(len(in1)):
        new_list.append(abs(in1_list[i]-in2_list[i]))
    if new_list.count(0)==0:
        print("Deletion succeeded")

    else:
        print("Deletion failed")
