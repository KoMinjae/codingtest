from collections import Counter
my_str = input().strip()
my_str=list(my_str)
countlist = list((Counter(my_str)))
countlist.sorted(key = lambda x : x[1])
print(countlist[0])