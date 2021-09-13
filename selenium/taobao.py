#-*- codeing = utf-8 -*-
#@Time :
#@Author :
import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
# from pymysql import *
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import matplotlib.pyplot as plt
from PIL import Image
import urllib
import csv


def slide_verify():
    # *** 进入滑块验证环节 ***
    # 判断是否需要滑块验证
    flag =False
    # element = EC.visibility_of_element_located((By.XPATH,'//*[@id="nc_1__scale_text"]/span'))
    while len(driver.find_elements_by_xpath('//*[@id="nc_1__scale_text"]/span')) > 0:
        time.sleep(3)
        flag = True
        print("检测到滑块验证")
        # 获取滑块的大小
        span_background = driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
        span_background_size = span_background.size
        print(span_background_size)

        # 获取滑块的位置
        button = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        button_location = button.location
        print(button_location)

        # 拖动操作：drag_and_drop_by_offset
        # 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）
        x_location = span_background_size["width"]
        y_location = button_location["y"]
        print(x_location, y_location)
        action = ActionChains(driver)
        source = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        action.click_and_hold(source).perform()
        action.move_by_offset(300, 0)
        action.release().perform()
        time.sleep(1)
    return flag


def login():
    # *** 直接输入用户名密码 ***
    # 填写用户名密码
    user = 'ganlangreat'
    password = 'InittBB@9409'
    # time.sleep(8)

    # iframe = driver.find_element_by_xpath('//div[@class="bokmXvaDlH"]//iframe')
    # print(iframe)
    # driver.switch_to.frame(iframe)
    driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(user)
    driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(password)
    # 点击登录
    driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
    time.sleep(2)

    # 滑块验证
    slide_verify()


    # # *** 方法2： 扫码登录方法 ***
    # #窗口最大化
    # driver.maximize_window()
    # # 点击扫码
    # driver.find_element_by_xpath("//*[@id=\"login\"]/div[1]/i").click()

    # # 判断当前页面是否为登录页面
    # while driver.current_url.startswith("https://login.taobao.com/"):
    #     print("等待用户输入")
    #     time.sleep(1)
    # # 等待进入淘宝页面
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//*[@id=\"tabFilterAll\"]")))


    print('登录成功\n')


def search_product(key):
    #获得输入框并输入要搜索的关键字key
    driver.find_element_by_id('q').send_keys(key)
    #点击搜索按钮
    driver.find_element_by_class_name("btn-search").click()

    # // *[ @ id = "q"]
    #
    # 登录
    login()

    # 避免登录后回到主页
    if len(driver.find_elements_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]')) == 0:
        # 获得输入框并输入要搜索的关键字key
        driver.find_element_by_id('q').send_keys(key)
        # 点击搜索按钮
        driver.find_element_by_class_name('// *[ @ id = "J_TSearchForm"] / div[1] / button').click()

    #获得总页数
    allPage = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    #re.findall('(\d+)',allPage)返回一个列表元素
    allPage = re.findall('(\d+)',allPage)[0]
    return int(allPage)

# 获取数据
def get_product(_pic_save_dir,_csv_path):
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        # time.sleep(0.2)
        # *** 获取元素信息 ***
        img = div.find_element_by_xpath('.//div[@class="pic"]/a/img').get_attribute('data-src')
        if "http" not in img:
            img = "https:" + img
        print(img)
        title = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text
        price = div.find_element_by_xpath(".//strong").text
        payNums = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text.replace("人付款","")
        # 店名
        shop = div.find_element_by_xpath('.//div[@class="shop"]/a').text
        # save_data(title,img,price,payNums)
        print("name:%s price:%s sales:%s img:%s"%(title,price,payNums,img))


        # *** 下载图片 ***
        save_path = os.path.join(_pic_save_dir,title+".jpg")
        with open(save_path, mode="wb") as f:
            # request = urllib.request.Request(img)
            # response = urllib.request.urlopen(request)
            # # 获取的文本实际上是图片的二进制文
            # img_content = response.read()

            img_content= requests.get(img).content
            # plt.imshow(img_content)
            f.write(img_content)


        with open(_csv_path,"a",newline="") as f:
            f_csv = csv.writer(f)
            # f_csv.writerow(headers)
            row = [title, price, shop, payNums, img]
            f_csv.writerow(row)


# #保存数据
# def save_data(title,img,price,payNums):
#     # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
#     con = connect("localhost", "root", "root", "pachong")
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursors = con.cursor()
#     # 使用 execute()  方法执行 SQL 查询 返回的是你影响的行数
#     cursors.execute("insert into fruit values(%s,%s,%s,%s,%s)", (None, title, img, price,payNums))
#     # 使用 fetchone() 方法获取数据.
#     con.commit()
#     # 关闭数据库连接（别忘了）
#     con.close()

def main(keyWord):
    #获得总共页数
    allPage = search_product(keyWord)
    currentPage = 1
    # *** 保存到csv ***
    csv_path = ("data/data.csv")
    # 创建csv
    if os.path.exists(csv_path):
        os.remove(csv_path)
    with open(csv_path, "a", newline="") as f:
        f_csv = csv.writer(f)
        # f_csv.writerow(headers)
        headers = ["title", "price", "shop", "payNums", "img"]
        f_csv.writerow(headers)
    while currentPage <= allPage:
        print("第{}页数据".format(currentPage))
        print("*****************************************")
        driver.get("https://s.taobao.com/search?q={}&s={}".format(keyWord,(currentPage-1)*44))
        # todo 这里要改
        driver.implicitly_wait(2)  #浏览器等待方法
        # 判断是否需要滑块验证
        if slide_verify():
            driver.get("https://s.taobao.com/search?q={}&s={}".format(keyWord, (currentPage - 1) * 44))
        #driver.maximize_window()
        save_dir = "data/pic/%s"%currentPage
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        # 获取商品
        get_product(save_dir,csv_path)
        print("第{}页数据保存成功".format(currentPage))
        currentPage += 1
        print("*****************************************")


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 这里去掉window.navigator.webdriver的特性
    option.add_argument("--disable-blink-features=AutomationControlled")  # 屏蔽webdriver特征

    driver = webdriver.Chrome(executable_path=r"D:\Study\programming\PycharmProjects\trials\selenium\chromedriver.exe",options=option)
    driver.get("https://s.taobao.com/")
    main("情趣内衣")