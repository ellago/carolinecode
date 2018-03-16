#!/usr/bin/python
#-*- coding:utf-8 –*-
import os, sys,re;
from time import *
'''
Created on 2017��8��16��
@author: caroline
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
print('num test')  
'''1-100质数'''
def primenumber():
    for num in range(1,100):
        for i in range(2,num):
            if (num%i ==0):
                print(str(num)+'不是质数')
                break
        else:
                print('num='+str(num))       
                

primenumber()                
'''二分查找'''
# test = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# def banarysearch(data_list,Value):
#     first =0
#     last = len(data_list)-1
#     while first <= last:
#         mid= (first + last)//2
#         if data_list[mid] == Value:
#             return mid
#         elif data_list[mid] > Value:
#             last = mid-1
#         else:
#             first = mid +1
#     return    
# ret = banarysearch(test, 0)
# print(ret)        


'''正则表达式'''
# line = "Cats are smarter than dogs"
# 
# matchObj = re.match( r'(.*) are (.*?) .*', line)
# 
# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print ("No match!!")



'''WebDriverAPI简单元素操作'''
# driver = webdriver.Firefox()
# driver.get("http://www.abc360.com/")
# 
# driver.find_element_by_id("top-log").click()
# driver.find_element_by_id("log-phone").clear()
# driver.find_element_by_id("log-phone").send_keys("17681835099")
# driver.find_element_by_id("log-password").clear()
# driver.find_element_by_id("log-password").send_keys("123456")
# driver.find_element_by_class_name("btn").click()
# driver.quit()

'''
鼠标事件
'''  
# driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
# above = driver.find_element_by_name("tj_settingicon")
# ActionChains(driver).move_to_element(above).perform()
# driver.quit()
'''python 基础练习'''
# name = "wangying"
# print("your name is %r" %name)
# if 2>3:
#     print("yes")
# else:
#     print(3)
# for i in range(1,10):
#     print(i)
# class A():
#     def add(self,a=1,b=2):
#         print("a+b=%r" %(a+b))
# class B(A):
#     def sub(self,a=2,b=1):
#         return a-b
# test = B()
# value=test.sub(8, 5)
# print("A-B=%r"%value)
# sleep(2)
# print(ctime)
    
'''控制浏览器'''   
# driver = webdriver.Firefox()  
# driver.implicitly_wait(30)
# driver.get("https://www.baidu.com/")
# print("设置浏览器宽480、高800显示")
# driver.set_window_size(480, 800)
# first_url="https://www.baidu.com/"
# print("now access %s" %first_url)
# driver.get(first_url)
# second_url="https://news.baidu.com/"
# print("now access %s" %second_url)
# driver.get(second_url)
#driver.find_element_by_class_name("bg s_btn_wr")
#driver.find_element_by_name("wd").send_keys("hello")
# driver.back()
# 
# 
# driver.quit()





'''
selenium 安装是否成功
'''  
# if __name__ == "__main__":
#       
# #   driver = webdriver.Firefox()
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(30)
#       
#     driver.get("http://www.google.com.hk")
#   
#     driver.find_element_by_name("q").send_keys("hello Selenium!")
#   
#     driver.find_element_by_name("q").submit()
#   
#     print('Page title is:',driver.title)
#   
#     driver.quit()

