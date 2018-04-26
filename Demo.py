#!/usr/bin/env python
#-*- coding:utf-8 -*- 
#@Time: 2018/4/26下午2:13
#@Author:zhangrongwu
#@File:Demo.py

from tkinter import  * #引入tk模块

root = Tk()#初始化tk

root.title("Hello world")
root.geometry('500x300')#设置大小
root.resizable(width=False, height=True) #宽不可变， 高可变，默认true


l = Label(root, text="这是一个label", font=("Arial", 12), width=10,height=3)
l.pack(side=TOP)

root.mainloop()#进入循环





