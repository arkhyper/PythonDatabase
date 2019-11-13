import sqlite3
from tkinter import *
import string
from LoginPage import *


class changepas(object):
    def __init__(self, master=None, info='密码修改界面'):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.mainlabel = Label(master, text=info, justify=CENTER)
        self.mainlabel.grid(row=0, columnspan=3)

        self.user = Label(master, text='注册用户名：', borderwidth=3)
        self.user.grid(row=1, sticky=W)

        self.pwd = Label(master, text='原密码：', borderwidth=3)
        self.pwd.grid(row=2, sticky=W)

        self.pwd = Label(master, text='新密码：', borderwidth=3)
        self.pwd.grid(row=3, sticky=W)


        self.userEntry = Entry(master)
        self.userEntry.grid(row=1, column=1, columnspan=3)
        self.userEntry.focus_set()

        self.pwdEntry = Entry(master, show='*')
        self.pwdEntry.grid(row=2, column=1, columnspan=3)

        self.pwd2Entry = Entry(master, show='*')
        self.pwd2Entry.grid(row=3, column=1, columnspan=3)

        self.loginButton = Button(master, text='确定修改', borderwidth=2, command=self.login)
        self.loginButton.grid(row=4, column=1)

        self.clearButton = Button(master, text='返回', borderwidth=2, command=self.clear)
        self.clearButton.grid(row=4, column=2)

    def login(self):
        self.userEntry = self.userEntry.get().strip()
        self.pwdEntry = self.pwdEntry.get().strip()
        self.pwd2Entry = self.pwd2Entry.get().strip()

        if self.userEntry == '':
            showwarning("无用户名", "请输入用户名")
        elif self.pwdEntry == '':
            showwarning("无密码", "请输入密码")
        else:
            # 打开数据库连接
            db = sqlite3.connect('login.db')
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # SQL 插入语句
            sql = "select * from user"
            try:
                cursor.execute(sql)  # 执行sql
                res = cursor.fetchall()  # 获取结果的列表
                for row in res:
                    id = row[0]
                    name = row[1]
                    pas = row[2]
                    if name == self.userEntry and pas == self.pwdEntry:
                        a = 1



            except:
                print("错误")

            if (a == 0):
                showinfo("用户名或密码错误")
            else:

                sql = "UPDATE user(name, pwd) SET pwd='%s' WHERE name='%s'" % (self.userEntry, self.pwd2Entry)
                try:
                    # 执行sql语句6

                    cursor.execute(sql)
                    print("数据插入成功！！！")

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


