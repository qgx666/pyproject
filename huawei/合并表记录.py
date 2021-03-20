#coding=utf-8
a = int(input())
dict1 = {}
for i in range(a):
    list1 = input().split(' ')
    key = int(list1[0])
    value = int(list1[1])
    dict1[key] = dict1.get(key,0) + value
for key in sorted(dict1):
    print(key,dict1.get(key))