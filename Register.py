import sqlite3
from tkinter import *
import string
from LoginPage import *
from tkinter import *
import sqlite3


class Register(object):
    def __init__(self, master=None, info='欢迎进入登陆界面'):
        self.root = master  # 定义内部变量root
        self.root.title('销售管理信息系统')

        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.mainlabel = Label(master, text=info, justify=CENTER)
        self.mainlabel.grid(row=0, columnspan=3)

        self.user = Label(master, text='注册用户名：', borderwidth=3)
        self.user.grid(row=1, sticky=W)

        self.pwd = Label(master, text='注册密码：', borderwidth=3)
        self.pwd.grid(row=2, sticky=W)

        self.userEntry = Entry(master)
        self.userEntry.grid(row=1, column=1, columnspan=3)
        self.userEntry.focus_set()

        self.pwdEntry = Entry(master, show='*')
        self.pwdEntry.grid(row=2, column=1, columnspan=3)

        self.loginButton = Button(master, text='确定注册', borderwidth=2, command=self.login)
        self.loginButton.grid(row=3, column=1)

        self.clearButton = Button(master, text='返回', borderwidth=2, command=self.clear)
        self.clearButton.grid(row=3, column=2)

    def login(self):
        self.userEntry = self.userEntry.get()
        self.pwdEntry = self.pwdEntry.get()
        # 打开数据库连接
        db = sqlite3.connect('login.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql0 = "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT NOT NULL ,password TEXT NOT NULL)"
        # SQL 插入语句
        sql = "INSERT INTO user(name, pwd) VALUES ('%s', '%s')" % (self.userEntry, self.pwdEntry)
        #sql语句中不能存在变量，会转换为字符串
        try:
            # 执行sql语句6
            cursor.execute(sql0)
            db.commit()
            cursor.execute(sql)
            print("数据插入成功！！！")
            showinfo('成功')

            # 提交到数据库执行
            db.commit()
        except:
            print("数据插入失败！！！")

            # Rollback in case there is any error
            db.rollback()

        # 关闭数据库连接
        db.close()

    def clear(self):


        self.root.withdraw()
        mainloop()




