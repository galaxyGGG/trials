

def sum_li(li_2d):
    li_2d_out = []
    for li in li_2d:
        li_temp = []
        for i in range(len(li)):
            val_temp = 0
            for j in range(i+1):
                val_temp += li[j]
            li_temp.append(val_temp)
        li_2d_out.append(li_temp)
    return li_2d_out


def sum_li2(li_2d):
    for i in range(len(li_2d)):
        li_tmp = li_2d[i]
        for j in range(1,len(li_tmp)):
            li_2d[i][j] += li_2d[i][j-1]


if __name__ == '__main__':
    li=[]
    for i in range(10):
        line = [x for x in range(10)]
        import random
        range
        li.append(line)
    # print(li)
    import time
    tic = time.time()
    li2 = sum_li(li)
    print("time: %s " % (time.time()-tic))

    tic = time.time()
    sum_li2(li)
    print("new time: %s " % (time.time() - tic))
    print(li)
