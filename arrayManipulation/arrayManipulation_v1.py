#! /usr/bin/env python
'''
import sys 
def r(curr_list, a_b_k_list, n):
    if a_b_k_list == []:
        print(max(curr_list))
    else:
        a = a_b_k_list[0][0] - 1
        b = a_b_k_list[0][1]
        k = a_b_k_list[0][2]
        y_list = [0 for i in range(n)]
        y_list[a:b] = [k] * (b-a)
        curr_list = [x+y for x,y in zip(curr_list, y_list)]
        r(curr_list, a_b_k_list[1:],n)
'''

def r2(curr_list, a_b_k_list, n):
    a = a_b_k_list[0] - 1
    b = a_b_k_list[1]
    k = a_b_k_list[2]
    y_list = [0 for i in range(n)]
    y_list[a:b] = [k] * (b-a)
    curr_list = [x+y for x,y in zip(curr_list, y_list)]
    return curr_list

def arrayManipulation(n, queries):
    curr_list = [0 for i in range(n)]
    a_b_k_list = queries
    for p in a_b_k_list:
        curr_list = r2(curr_list, p,n)

    return max(curr_list)
    
if __name__ == '__main__':
    pair = input()
    n = int(pair.split(" ")[0])
    queries_list = []
    for i in range(int(pair.split(" ")[1])):
        new_line = input().split(" ")
        s = [int(val) for val in new_line]
        queries_list.append(s)
        
    print(arrayManipulation(n, queries_list))
