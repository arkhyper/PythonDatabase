from tkinter import *

from MainPage import *
import sqlite3
from tkinter.messagebox import *
import os


class if7(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()


    def createPage(self):
        Label(self, text='查看员工表').grid(row=0,column=0, stick=W)
        Button(self, text='查看', command=self.see).grid(row=1)
    def see(self):

        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        sql = "SELECT* FROM employee"
        # 关键
        try:
            cursor.execute(sql)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i = 0

            for row in res:
                Label(self, text=row[0]).grid(row=3 + i, column=1)
                Label(self, text=row[1]).grid(row=3 + i, column=2)
                Label(self, text=row[2]).grid(row=3 + i, column=3)
                Label(self, text=row[3]).grid(row=3 + i, column=4)

                i += 1
        except:
            print("错误")

        db.close()
        mainloop()


class if6(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()


    def createPage(self):
        Label(self, text='查看退货表').grid(row=0,column=0, stick=W)
        Button(self, text='查看', command=self.see).grid(row=1)

    def see(self):

        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        k = 0

        mon = 0
        t = 0
        sql = "SELECT* FROM retreat"
        # 关键
        try:
            cursor.execute(sql)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i = 0

            for row in res:
                Label(self, text=row[0]).grid(row=3 + i, column=1)
                Label(self, text=row[1]).grid(row=3 + i, column=2)
                Label(self, text=row[2]).grid(row=3 + i, column=3)
                Label(self, text=row[3]).grid(row=3 + i, column=4)
                Label(self, text=row[4]).grid(row=3 + i, column=5)
                Label(self, text=row[5]).grid(row=3 + i, column=6)
                Label(self, text=row[6]).grid(row=3 + i, column=7)
                Label(self, text=row[7]).grid(row=3 + i, column=8)
                Label(self, text=row[8]).grid(row=3 + i, column=9)
                Label(self, text=row[9]).grid(row=3 + i, column=10)
                Label(self, text=row[10]).grid(row=3 + i, column=11)

                i += 1
        except:
            print("错误")

        db.close()
        mainloop()


class if5(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()


    def createPage(self):
        Label(self, text='查看销售表').grid(row=0,column=0, stick=W)
        Button(self, text='查看', command=self.see).grid(row=1)

    def see(self):

        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        sql = "SELECT* FROM sell"
        # 关键
        try:
            cursor.execute(sql)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i = 0


            for row in res:
                Label(self, text=row[0]).grid(row=3 + i, column=1)
                Label(self, text=row[1]).grid(row=3 + i, column=2)
                Label(self, text=row[2]).grid(row=3 + i, column=3)
                Label(self, text=row[3]).grid(row=3 + i, column=4)
                Label(self, text=row[4]).grid(row=3 + i, column=5)
                Label(self, text=row[5]).grid(row=3 + i, column=6)
                Label(self, text=row[6]).grid(row=3 + i, column=7)
                Label(self, text=row[7]).grid(row=3 + i, column=8)
                Label(self, text=row[8]).grid(row=3 + i, column=9)
                Label(self, text=row[9]).grid(row=3 + i, column=10)
                Label(self, text=row[10]).grid(row=3 + i, column=11)

                i += 1
        except:
            print("错误")

        db.close()
        mainloop()



class if4(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()


    def createPage(self):
        Label(self, text='查看进货表').grid(row=0,column=0, stick=W)
        Button(self, text='查看', command=self.see).grid(row=1)

    def see(self):


        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        sql = "SELECT* FROM goods"
        # 关键
        try:
            cursor.execute(sql)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i = 0

            for row in res:



                Label(self, text=row[0]).grid(row=3 + i, column=1)
                Label(self, text=row[1]).grid(row=3 + i, column=2)
                Label(self, text=row[2]).grid(row=3 + i, column=3)
                Label(self, text=row[3]).grid(row=3 + i, column=4)
                Label(self, text=row[4]).grid(row=3 + i, column=5)
                Label(self, text=row[5]).grid(row=3 + i, column=6)
                Label(self, text=row[6]).grid(row=3 + i, column=7)
                Label(self, text=row[7]).grid(row=3 + i, column=8)
                Label(self, text=row[8]).grid(row=3 + i, column=9)
                Label(self, text=row[9]).grid(row=3 + i, column=10)
                Label(self, text=row[10]).grid(row=3 + i, column=11)


                i += 1
        except:
            print("错误")

        db.close()
        mainloop()








class if3(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.n17 = StringVar()
        self.n18 = StringVar()
        self.n19 = StringVar()
        self.createPage()


    def createPage(self):
        Label(self, text='业绩查询').grid(row=0, stick=W)
        Label(self, text='查询全部人').grid(row=0, column=1)
        Button(self, text='查询', command=self.ii1).grid(row=0, column=2, pady=10)

        Label(self, text='请输入员工号').grid(row=1, column=0)
        Entry(self, textvariable=self.n17).grid(row=1, column=1)
        Button(self, text='查询', command=self.ii2).grid(row=1, column=2, pady=10)


    def ii1(self):


        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        k = 0

        mon = 0
        t = 0
        sql = "SELECT sell.业务员编号,sell.总金额,employee.员工姓名 FROM sell LEFT OUTER JOIN employee WHERE employee.员工编号 = sell.业务员编号 ORDER BY 业务员编号"
              # 关键
        try:
            cursor.execute(sql)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i=0
            j=0
            tx=0

            for t in range(0,20):
                Label(self, text='                                     ').grid(row=4 + t, column=1)
            tt = res[0][0]

            for row in res:

                if row[0] == tt:
                    mon = row[1]
                    t +=mon
                else:
                    tt=row[0]
                    Label(self, text=t+tx).grid(row=4 + i, column=2)
                    tx = row[1]
                    i += 1
                    t=0
            Label(self, text=tt+tx).grid(row=4 + i, column=2)

            i=0
            for row in res:


                if row[0]==k:
                    k=k
                else:
                    k = row[0]

                    Label(self, text=row[0]).grid(row=4 + i, column=0)
                    Label(self, text=row[2]).grid(row=4 + i, column=1)

                    i+=1
        except:
            print("错误")

        db.close()
        mainloop()

    def ii2(self):
        re17 = self.n17.get()


        ao = [re17]
        if '' in ao:
            showinfo("空项，请补齐")
            raise ValueError
        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        k = 0
        combine = [re17]
        mon = 0
        t = 0
        sql = "SELECT sell.业务员编号,sell.总金额,employee.员工姓名 FROM sell LEFT OUTER JOIN employee WHERE employee.员工编号 = sell.业务员编号 AND 业务员编号=?"
              # 关键
        try:
            cursor.execute(sql, combine)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i=0
            j=0
            tx=0

            for t in range(0,20):
                Label(self, text='                                     ').grid(row=4 + t, column=1)
            tt = res[0][0]
            for row in res:

                if row[0] == tt:
                    mon = row[1]
                    t +=mon
                else:

                    tt=row[0]

                    Label(self, text=t+tx).grid(row=4 + i, column=2)
                    tx = row[1]


                    i += 1
                    t=0
            Label(self, text=t).grid(row=4 + i, column=2)

            i=0
            for row in res:
                if row[0]==k:
                    k=k
                else:
                    k = row[0]

                    Label(self, text=row[0]).grid(row=4 + i, column=0)
                    Label(self, text=row[2]).grid(row=4 + i, column=1)

                    i+=1







        except:
            print("错误")

        db.close()
        mainloop()



class if2(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.n17 = StringVar()
        self.n18 = StringVar()
        self.n19 = StringVar()
        self.createPage()


    def createPage(self):
        Label(self, text='销售统计').grid(row=0, stick=W)
        Label(self, text='请输入查询年月日').grid(row=1, column=0)
        Label(self, text='若只查询年月，其后项目可不输入').grid(row=1, column=1)

        Entry(self, textvariable=self.n17).grid(row=1, column=2)
        Label(self, text='年').grid(row=1, column=3, pady=10)
        Entry(self, textvariable=self.n18).grid(row=1, column=4)
        Label(self, text='月').grid(row=1, column=5, pady=10)
        Entry(self, width=5, textvariable=self.n19).grid(row=1, column=6)
        Label(self, text='日').grid(row=1, column=7, pady=10)
        Button(self, text='查询日', command=self.ii1).grid(row=2, column=7)
        Button(self, text='查询月', command=self.ii2).grid(row=2, column=5)
        Button(self, text='查询年', command=self.ii3).grid(row=2, column=3)
        Label(self, text='结果:').grid(row=3, column=0)
        Label(self, text='商品编号 生产厂商 商品名 型号 总金额').grid(row=3, column=1)
        Label(self, text='总金额:').grid(row=3, column=2)


    def ii1(self):

        re17 = self.n17.get()
        re18 = self.n18.get()
        re19 = self.n19.get()


        ao = [re17, re18, re19]
        if '' in ao:
            showinfo("年月日空项，请补齐")
            raise ValueError

        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        combine = [re17, re18, re19]  # 关键
        mon = 0
        t = 0
        sql = "SELECT 商品编号,生产厂商,商品名,型号,总金额 FROM sell WHERE 销售年=? AND 销售月=? AND 销售日=? "  # 关键
        try:
            cursor.execute(sql, combine)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i=0
            j=0

            for t in range(0,20):
                Label(self, text='                                     ').grid(row=4 + t, column=1)


            for culumn in res:
                # 关键
                i+=1
                j += 1
                Label(self, text=culumn).grid(row=4+i,column=1)  # culum外不要打引号也不要加[]

            for row in res:
                mon = row[4]
                t +=mon





        except:
            print("错误")
        Label(self, text=t).grid(row=3, column=3)
        db.close()
        mainloop()

    def ii2(self):
        re17 = self.n17.get()
        re18 = self.n18.get()
        re19 = self.n19.get()

        ao = [re17, re18]
        if '' in ao:
            showinfo("年月空项，请补齐")
            raise ValueError

        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        combine = [re17, re18]  # 关键
        mon = 0
        t = 0
        sql = "SELECT 商品编号,生产厂商,商品名,型号,总金额 FROM sell WHERE 销售年=? AND 销售月=? "  # 关键
        try:
            cursor.execute(sql, combine)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i=0
            j=0
            for t in range(0, 20):
                Label(self, text='                                     ').grid(row=4 + t, column=1)
            for culumn in res:
                # 关键
                i+=1
                j += 1
                Label(self, text=culumn).grid(row=4+i,column=1)  # culum外不要打引号也不要加[]

            for row in res:
                mon = row[4]

                t +=mon





        except:
            print("错误")
        Label(self, text=t).grid(row=3, column=3)
        db.close()

    def ii3(self):
        re17 = self.n17.get()
        re18 = self.n18.get()
        re19 = self.n19.get()

        ao = [re17]
        if '' in ao:
            showinfo("年空项，请补齐")
            raise ValueError
        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        combine = [re17]  # 关键
        mon = 0
        t = 0
        sql = "SELECT 商品编号,生产厂商,商品名,型号,总金额 FROM sell WHERE 销售年=?"  # 关键
        try:
            cursor.execute(sql, combine)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i=0
            j=0
            for t in range(0, 20):
                Label(self, text='                                     ').grid(row=4 + t, column=1)
            for culumn in res:
                # 关键
                i+=1
                j += 1
                Label(self, text=culumn).grid(row=4+i,column=1)  # culum外不要打引号也不要加[]

            for row in res:
                mon = row[4]
                t +=mon





        except:
            print("错误")
        Label(self, text=t).grid(row=3, column=3)
        db.close()




class if1(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.n17 = StringVar()
        self.n18 = StringVar()
        self.n19 = StringVar()
        self.createPage()


    def createPage(self):
        Label(self, text='进货统计').grid(row=0, stick=W)
        Label(self, text='请输入查询年月日').grid(row=1, column=0)
        Label(self, text='若只查询年月，其后项目可不输入').grid(row=1, column=1)

        Entry(self, textvariable=self.n17).grid(row=1, column=2)
        Label(self, text='年').grid(row=1, column=3, pady=10)
        Entry(self, textvariable=self.n18).grid(row=1, column=4)
        Label(self, text='月').grid(row=1, column=5, pady=10)
        Entry(self, width=5, textvariable=self.n19).grid(row=1, column=6)
        Label(self, text='日').grid(row=1, column=7, pady=10)
        Button(self, text='查询日', command=self.ii1).grid(row=2, column=7)
        Button(self, text='查询月', command=self.ii2).grid(row=2, column=5)
        Button(self, text='查询年', command=self.ii3).grid(row=2, column=3)
        Label(self, text='结果:').grid(row=3, column=0)
        Label(self, text='商品编号 生产厂商 商品名 型号 总金额').grid(row=3, column=1)
        Label(self, text='总金额:').grid(row=3, column=2)

    def ii1(self):

        re17 = self.n17.get()
        re18 = self.n18.get()
        re19 = self.n19.get()


        ao = [re17, re18, re19]
        if '' in ao:
            showinfo("年月日空项，请补齐")
            raise ValueError

        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        combine = [re17, re18, re19]  # 关键
        mon = 0
        t = 0
        sql = "SELECT 商品编号,生产厂商,商品名,型号,总金额 FROM goods WHERE 进货年=? AND 进货月=? AND 进货日=? "  # 关键
        try:
            cursor.execute(sql, combine)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i=0
            j=0

            for t in range(0,20):
                Label(self, text='                                     ').grid(row=4 + t, column=1)


            for culumn in res:
                # 关键
                i+=1
                j += 1
                Label(self, text=culumn).grid(row=4+i,column=1)  # culum外不要打引号也不要加[]

            for row in res:
                mon = row[4]
                t +=mon

        except:
            print("错误")
        Label(self, text=t).grid(row=3, column=3)
        db.close()
        mainloop()

    def ii2(self):
        re17 = self.n17.get()
        re18 = self.n18.get()
        re19 = self.n19.get()

        ao = [re17, re18]
        if '' in ao:
            showinfo("年月空项，请补齐")
            raise ValueError

        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        combine = [re17, re18]  # 关键
        mon = 0
        t = 0
        sql = "SELECT 商品编号,生产厂商,商品名,型号,总金额 FROM goods WHERE 进货年=? AND 进货月=? "  # 关键
        try:
            cursor.execute(sql, combine)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i=0
            j=0
            for t in range(0, 20):
                Label(self, text='                                     ').grid(row=4 + t, column=1)
            for culumn in res:
                # 关键
                i+=1
                j += 1
                Label(self, text=culumn).grid(row=4+i,column=1)  # culum外不要打引号也不要加[]

            for row in res:
                mon = row[4]

                t +=mon





        except:
            print("错误")
        Label(self, text=t).grid(row=3, column=3)
        db.close()

    def ii3(self):
        re17 = self.n17.get()
        re18 = self.n18.get()
        re19 = self.n19.get()

        ao = [re17]
        if '' in ao:
            showinfo("年空项，请补齐")
            raise ValueError
        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        combine = [re17]  # 关键
        mon = 0
        t = 0
        sql = "SELECT 商品编号,生产厂商,商品名,型号,总金额 FROM goods WHERE 进货年=?"  # 关键
        try:
            cursor.execute(sql, combine)  # 执行sql
            res = cursor.fetchall()  # 获取结果的列表
            i=0
            j=0
            for t in range(0, 20):
                Label(self, text='                                     ').grid(row=4 + t, column=1)
            for culumn in res:
                # 关键
                i+=1
                j += 1
                Label(self, text=culumn).grid(row=4+i,column=1)  # culum外不要打引号也不要加[]

            for row in res:
                mon = row[4]
                t +=mon





        except:
            print("错误")
        Label(self, text=t).grid(row=3, column=3)
        db.close()




class inputframe13(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.n11 = StringVar()
        self.n12 = StringVar()
        self.n13 = StringVar()
        self.n14 = StringVar()
        self.n15 = StringVar()
        self.n16 = StringVar()
        self.n17 = StringVar()
        self.n18 = StringVar()
        self.n19 = StringVar()
        self.n20 = StringVar()
        self.n21 = StringVar()
        self.createPage()
    def createPage(self):
        Label(self, text='退货登记').grid(row=0, stick=W)
        Label(self, text='退货编号： ').grid(row=1, column=1, pady=10)
        Entry(self, textvariable=self.n11).grid(row=1, column=2)

        Label(self, text='商品名称： ').grid(row=1, column=3, pady=10)
        Entry(self, textvariable=self.n12).grid(row=1, column=4)
        Label(self, text='生产厂商： ').grid(row=2, column=1, pady=10)
        Entry(self, textvariable=self.n13).grid(row=2, column=2)
        Label(self, text='型号： ').grid(row=2, column=3, pady=10)
        Entry(self, textvariable=self.n14).grid(row=2, column=4)
        Label(self, text='单价： ').grid(row=3, pady=10, column=1)
        Entry(self, textvariable=self.n15).grid(row=3, column=2)
        Label(self, text='数量： ').grid(row=3, column=3, pady=10)
        Entry(self, textvariable=self.n16).grid(row=3, column=4)
        Label(self, text='退货日期： ').grid(row=4, column=1, pady=10)
        Entry(self, textvariable=self.n17).grid(row=4, column=2)
        Label(self, text='年').grid(row=4, column=3, pady=10)
        Entry(self, textvariable=self.n18).grid(row=4, column=4)
        Label(self, text='月').grid(row=4, column=5, pady=10)
        Entry(self, width=5, textvariable=self.n19).grid(row=4, column=6)
        Label(self, text='日').grid(row=4, column=7, pady=10)

        Label(self, text='业务员编号： ').grid(row=5, pady=10, column=1)
        Entry(self, textvariable=self.n20).grid(row=5, column=2)
        Label(self, text='退货总金额： ').grid(row=5, column=3, pady=10)
        Entry(self, textvariable=self.n21).grid(row=5, column=4)
        Button(self, text='退货', command=self.retu).grid(row=6, column=2)
    def retu(self):
        re10=self.n11.get()
        re12=self.n12.get()
        re13=self.n13.get()
        re14=self.n14.get()
        re15=self.n15.get()
        re16=self.n16.get()
        re17=self.n17.get()
        re18=self.n18.get()
        re19=self.n19.get()
        re20=self.n20.get()
        re21=self.n21.get()
        ao=[re10,re12, re13, re14, re15, re16, re17, re18, re19, re20, re21]
        if '' in ao:
            showinfo("有空项，请补齐")
            raise ValueError



        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql = "INSERT INTO retreat values(?,?,?,?,?,?,?,?,?,?,?) "
        try:
            # 执行sql语句

            cursor.execute(sql,(re10,re13,re12,re14,re15,re16,re21,re17,re18,re19,re20 ))
            print("数据插入成功！！！")

            # 提交到数据库执行
            db.commit()
            showinfo("成功")
        except:
            print("数据插入失败！！！")
            showinfo("失败")


            # Rollback in case there is any error
            db.rollback()

        # 关闭数据库连接
        db.close()



class inputframe12(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.n11 = StringVar()
        self.n12 = StringVar()
        self.n13 = StringVar()
        self.n14 = StringVar()
        self.n15 = StringVar()
        self.n16 = StringVar()
        self.n17 = StringVar()
        self.n18 = StringVar()
        self.n19 = StringVar()
        self.n20 = StringVar()
        self.n21 = StringVar()
        self.createPage()
    def createPage(self):
        Label(self, text='销售统计').grid(row=0, stick=W)
        Label(self, text='商品编号： ').grid(row=1, column=1, pady=10)
        Entry(self, textvariable=self.n11).grid(row=1, column=2)

        Label(self, text='商品名称： ').grid(row=1, column=3, pady=10)
        Entry(self, textvariable=self.n12).grid(row=1, column=4)
        Label(self, text='生产厂商： ').grid(row=2, column=1, pady=10)
        Entry(self, textvariable=self.n13).grid(row=2, column=2)
        Label(self, text='型号： ').grid(row=2, column=3, pady=10)
        Entry(self, textvariable=self.n14).grid(row=2, column=4)
        Label(self, text='单价： ').grid(row=3, pady=10, column=1)
        Entry(self, textvariable=self.n15).grid(row=3, column=2)
        Label(self, text='数量： ').grid(row=3, column=3, pady=10)
        Entry(self, textvariable=self.n16).grid(row=3, column=4)
        Label(self, text='销售日期： ').grid(row=4, column=1, pady=10)
        Entry(self, textvariable=self.n17).grid(row=4, column=2)
        Label(self, text='年').grid(row=4, column=3, pady=10)
        Entry(self, textvariable=self.n18).grid(row=4, column=4)
        Label(self, text='月').grid(row=4, column=5, pady=10)
        Entry(self, width=5, textvariable=self.n19).grid(row=4, column=6)
        Label(self, text='日').grid(row=4, column=7, pady=10)

        Label(self, text='业务员编号： ').grid(row=5, pady=10, column=1)
        Entry(self, textvariable=self.n20).grid(row=5, column=2)
        Label(self, text='总金额： ').grid(row=5, column=3, pady=10)
        Entry(self, textvariable=self.n21).grid(row=5, column=4)
        Button(self, text='添加入库', command=self.sell).grid(row=6, column=2)

    def sell(self):
        re10=self.n11.get()
        re12=self.n12.get()
        re13=self.n13.get()
        re14=self.n14.get()
        re15=self.n15.get()
        re16=self.n16.get()
        re17=self.n17.get()
        re18=self.n18.get()
        re19=self.n19.get()
        re20=self.n20.get()
        re21=self.n21.get()
        ao = [re10, re12, re13, re14, re15, re16, re17, re18, re19, re20, re21]
        if '' in ao:
            showinfo("有空项，请补齐")
            raise ValueError
        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql = "INSERT INTO sell(商品编号,生产厂商,商品名,型号,单价,数量,总金额,销售年,销售月,销售日,业务员编号) values(?,?,?,?,?,?,?,?,?,?,?) "
        try:
            # 执行sql语句

            cursor.execute(sql,( re10,re13,re12,re14,re15,re16,re21,re17,re18,re19,re20 ))
            print("数据插入成功！！！")

            # 提交到数据库执行
            db.commit()
            showinfo("成功")
        except:
            print("数据插入失败！！！")
            showinfo("失败")


            # Rollback in case there is any error
            db.rollback()

        # 关闭数据库连接
        db.close()






class InputFrame11(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.itemName = StringVar()
        self.importPrice = StringVar()

        self.sellPrice = StringVar()
        self.deductPrice = StringVar()
        self.n11 = StringVar()
        self.n12 = StringVar()
        self.n13 = StringVar()
        self.n14 = StringVar()
        self.n15 = StringVar()
        self.n16 = StringVar()
        self.n17 = StringVar()
        self.n18 = StringVar()
        self.n19 = StringVar()
        self.n20 = StringVar()
        self.n21 = StringVar()

        self.n31 = StringVar()
        self.n32 = StringVar()
        self.n33 = StringVar()
        self.n34 = StringVar()


        self.createPage()

    def createPage(self):
        Label(self, text='添加商品').grid(row=0, stick=W )
        Label(self, text='商品编号： ').grid(row=1, column=1, pady=10)
        Entry(self, textvariable=self.n11).grid(row=1, column=2)

        Label(self, text='商品名称： ').grid(row=1,column=3 , pady=10 )
        Entry(self, textvariable=self.n12).grid(row=1, column=4)
        Label(self, text='生产厂商： ').grid(row=2, column=1, pady=10)
        Entry(self, textvariable=self.n13).grid(row=2, column=2)
        Label(self, text='型号： ').grid(row=2, column=3, pady=10)
        Entry(self, textvariable=self.n14).grid(row=2, column=4)
        Label(self, text='单价： ').grid(row=3, pady=10,column=1)
        Entry(self, textvariable=self.n15).grid(row=3, column=2)
        Label(self, text='数量： ').grid(row=3, column=3, pady=10)
        Entry(self, textvariable=self.n16).grid(row=3, column=4)
        Label(self, text='送货日期： ').grid(row=4, column=1, pady=10)
        Entry(self,  textvariable=self.n17).grid(row=4, column=2)
        Label(self, text='年').grid(row=4, column=3, pady=10)
        Entry(self, textvariable=self.n18).grid(row=4, column=4)
        Label(self, text='月').grid(row=4, column=5, pady=10)
        Entry(self, width = 5,textvariable=self.n19).grid(row=4, column=6)
        Label(self, text='日').grid(row=4, column=7, pady=10)

        Label(self, text='业务员编号： ').grid(row=5, pady=10, column=1)
        Entry(self, textvariable=self.n20).grid(row=5, column=2)
        Label(self, text='总金额： ').grid(row=5, column=3, pady=10)
        Entry(self, textvariable=self.n21).grid(row=5, column=4)
        Button(self, text='添加入库', command=self.r1).grid(row=6, column=2)
    #    Button(self, text='清空重填', command=self.k1).grid(row=6, column=4)


        Label(self, text='添加厂商').grid(row=7, stick=W)
        Label(self, text='厂商名称：').grid(row=8, pady=10, column=1)
        Entry(self,textvariable=self.n31).grid(row=8,column=2)
        Label(self, text='法人代表：').grid(row=8, pady=10, column=3)
        Entry(self, textvariable=self.n32).grid(row=8, column=4)
        Label(self, text='厂商地址：').grid(row=9, pady=10, column=1)
        Entry(self, textvariable=self.n33).grid(row=9, column=2)
        Label(self, text='电话：').grid(row=9, pady=10, column=3)
        Entry(self, textvariable=self.n34).grid(row=9, column=4)
        Button(self, text='添加入库', command=self.r2).grid(row=10, column=2)

    #    Button(self, text='清空重填', command=self.k2).grid(row=10, column=4)

        '''
        Label(self, text='进价 /元: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.importPrice).grid(row=2, column=1, stick=E)
        Label(self, text='售价 /元: ').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.sellPrice).grid(row=3, column=1, stick=E)
        Label(self, text='优惠 /元: ').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.deductPrice).grid(row=4, column=1, stick=E)
        Button(self, text='录入').grid(row=6, column=1, stick=E, pady=10)
         '''





    def r2(self):
        re10=self.n31.get()
        re12=self.n32.get()
        re13=self.n33.get()
        re14=self.n34.get()

        ao = [re10, re12, re13, re14]
        if '' in ao:
            showinfo("有空项请补齐")
            raise ValueError
        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql = "INSERT INTO manufacturer(厂商名称,法人代表,电话,厂商地址) values(?,?,?,?)"
        try:
            # 执行sql语句

            cursor.execute(sql,(re10, re12, re14, re13))
            print("数据插入成功！！！")

            # 提交到数据库执行
            db.commit()
            showinfo("成功")
        except:
            print("数据插入失败！！！")
            showinfo("失败")


            # Rollback in case there is any error
            db.rollback()

        # 关闭数据库连接
        db.close()

    def r1(self):
        re10 = self.n11.get()
        re12 = self.n12.get()
        re13 = self.n13.get()
        re14 = self.n14.get()
        re15 = self.n15.get()
        re16 = self.n16.get()
        re17 = self.n17.get()
        re18 = self.n18.get()
        re19 = self.n19.get()
        re20 = self.n20.get()
        re21 = self.n21.get()
        ao = [re10, re12, re13, re14, re15, re16, re17, re18, re19, re20, re21]
        if '' in ao:
            showinfo("有空项，请补齐")
            raise ValueError
        # 打开数据库连接
        db = sqlite3.connect('sellsys.db')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql = "INSERT INTO goods values(?,?,?,?,?,?,?,?,?,?,?) "
        try:
            # 执行sql语句

            cursor.execute(sql, (re10, re13, re12, re14, re15, re16, re21, re17, re18, re19, re20))
            print("数据插入成功！！！")

            # 提交到数据库执行
            db.commit()
            showinfo("成功")
        except:
            print("数据插入失败！！！")
            showinfo("失败")

            # Rollback in case there is any error
            db.rollback()

        # 关闭数据库连接
        db.close()

