import turtle

# turtle.pencolor("red")
# turtle.fillcolor("yellow")
# turtle.begin_fill()
# turtle.circle(160,180)
# turtle.end_fill()
# turtle.done()

# turtle.pencolor("red")
# turtle.pensize(3)
# turtle.circle(50)
# turtle.penup()
# turtle.goto(0,-50)
# turtle.pendown()
# turtle.circle(100)
# turtle.penup()
# turtle.goto(0,-150)
# turtle.pendown()
# turtle.circle(200)
# turtle.done()


# def my_sum(a,b):
#     c = a+b
#     return c

# import math
# def cal_circumference(r):
#     c = 2*math.pi*r
#     return c
#
# print(cal_circumference(1))


import random
def gen_num():
    a = 3 * random.randint(0,33)
    b = 3 * random.randint(0,33)
    c = 3 * random.randint(0,33)
    return a,b,c
print(gen_num())
