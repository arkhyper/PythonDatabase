from tkinter import *
from tkinter.messagebox import *
import sqlite3
from MainPage import *
from Register import *
from changepas import *

class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (340, 200))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    # 构造函数里传入一个父组件(master),创建一个Frame组件并显示
    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        # N/S/E/W，分别代表上/下/左/右,想让label靠左显示可以设置stricky的值为W。
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3,column=1, stick=W, pady=10)
        #Button(self.page, text='修改密码', command=self.changepas).grid(row=3, column=2)

        Button(self.page, text='注册', command=self.regis).grid(row=3, column=3)

        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=4, stick=E)

    def regis(self):
        self.rootR = Tk()
        Register(self.rootR)
        self.root.withdraw()
    def changepas(self):
        self.rootR = Tk()
        changepas(self.rootR)
        self.root.withdraw()

    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        e1 = self.username.get()
        e2 = self.password.get()
        if e1 == '':
            showwarning("无用户名", "请输入用户名")
        elif e2 == '':
            showwarning("无密码", "请输入密码")
        else:
            a = 0
            db = sqlite3.connect('login.db')  # 存储用户名密码的数据库
            cursor = db.cursor()  # 创建游标
            sql = "select * from user"
            try:
                cursor.execute(sql)  # 执行sql
                res = cursor.fetchall()  # 获取结果的列表
                for row in res:
                    id = row[0]
                    name = row[1]
                    pas = row[2]
                    if name == e1 and pas == e2:
                        a = 1
                        print("登陆成功")
                        self.page.destroy()
                        MainPage(self.root)

            except:
                print("错误")
            db.close()
            if (a == 0):
                showinfo("用户名或密码错误")
'''
        if name == 'a' and secret == 'a':
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title='错误', message='账号或密码错误！')
'''