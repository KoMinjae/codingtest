import re
from collections import Counter as mset
p = re.compile("[a-z][a-z]")
def multiSet(str):
    lst = []
    for idx in range(len(str)-1):
        if p.match(str[idx:idx+2]):
            lst.append(str[idx:idx+2])
    return lst
def solution(str1, str2):
    lst1 = multiSet(str1.lower())
    lst2 = multiSet(str2.lower())
    len_lst1 = len(lst1)
    len_lst2 = len(lst2)
    if len_lst1 == 0 and len_lst2 == 0:
        return 65536
    mset1 = mset(lst1)
    mset2 = mset(lst2)
    inter_lst = list((mset1 & mset2).elements())
    len_inter_lst = len(inter_lst)
    len_union_lst = len_lst1 + len_lst2 - len_inter_lst
    return int(len_inter_lst/len_union_lst *65536)

solution("aa1+aa2","AAAA12")