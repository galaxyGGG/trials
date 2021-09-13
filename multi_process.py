from multiprocessing import Process,Queue
import time,random,os

def consumer(q):
    while True:
        res=q.get()
        # if res is None:break #收到结束信号则结束
        time.sleep(1)
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))

def producer(q):
    count = 0
    while True:
        time.sleep(random.randint(5,6))
        q.put(count)

        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),count))
        count += 1

if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,))

    #消费者们:即吃货们
    c_list=[]
    for i in range(3):
        c=Process(target=consumer,args=(q,))
        c.start()
        c_list.append(c)

    #开始
    p1.start()
    # c1.start()
    p1.join()
    for c in c_list:
        c.join()
    # c1.join()
    print('主')