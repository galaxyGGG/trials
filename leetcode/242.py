def isAnagram(s: str, t: str) -> bool:

    """
    直接排序的方法
    """
    # ss = list(s)
    # tt = list(t)
    # ss.sort()
    # tt.sort()
    # return ss == tt

    """
    **** 字典统计的方法 ***  此方法比排序更快
    时间复杂度O(m+n)
    """
    if len(s) != len(t):
        return False
    dict1 = {}
    for val in s:
        dict1[val] = dict1.get(val, 0) + 1
    dict2 = {}
    for val in t:
        dict2[val] = dict2.get(val, 0) + 1
    return dict1 == dict2

if __name__ == '__main__':
    print(isAnagram("aacc","acac"))