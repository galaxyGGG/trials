import random

def bubble_sort_my(li):
    """
    # 写得太拉跨
    :param li:
    :return:
    """
    for i in range(len(li)-1):
        ind = 0
        while ind< len(li) - 1:
            if li[ind] > li[ind+1]:
                temp = li[ind+1]
                li[ind + 1] = li[ind]
                li[ind] = temp
            ind+=1
    return li


def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-1-i):
            if li[j+1] < li[j]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        # print(li)
        if not exchange:
            break


def select_sort(li):
    for i in range(len(li)-1):
        for j in range(i+1,len(li) ):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]


if __name__ == '__main__':
    random.seed(0)
    li= [random.randint(0,10) for i in range(10)]
    print(li)
    bubble_sort(li)
    print(li)
    select_sort(li)
    print(li)
