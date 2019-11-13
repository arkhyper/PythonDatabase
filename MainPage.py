from tkinter import *
from view import *  # 菜单栏对应的各个子页面


class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (780, 580))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.inputPage11 = InputFrame11(self.root)  # 创建不同Frame
        self.inputpage12 = inputframe12(self.root)
        self.inputpage13 = inputframe13(self.root)
        self.i11 = if1(self.root)
        self.i22 = if2(self.root)
        self.i33 = if3(self.root)
        self.i41 = if4(self.root)
        self.i42 = if5(self.root)
        self.i43 = if6(self.root)
        self.i44 = if7(self.root)











        menubar = Menu(self.root )
        # 创建子菜单filemenu
        filemenu = Menu(menubar, tearoff=0) # tearoff让下拉菜单不独立更好看
        filemenu.add_command(label='进货登记', command=self.inputData)
        filemenu.add_command(label='销售登记', command=self.selldata)
        filemenu.add_command(label='退货登记', command=self.returnback)
        menubar.add_cascade(label='数据录入', menu=filemenu) #cascade叠层

        '''changemenu = Menu(menubar, tearoff=0)
        changemenu.add_command(label='日进货统计',command=self.i1)
        changemenu.add_command(label='月进货统计',command=self.i2)
        changemenu.add_command(label='季进货统计',command=self.i3)
        changemenu.add_command(label='年进货统计',command=self.i4)'''
        menubar.add_command(label='进货统计', command=self.i1)


        menubar.add_cascade(label='销售统计', command=self.i2)

        menubar.add_cascade(label='业绩查看', command=self.i3)

        sheet = Menu(menubar, tearoff=0)
        sheet.add_command(label='进货表', command=self.i401)
        sheet.add_command(label='销售表', command=self.i402)
        sheet.add_command(label='退货表', command=self.i403)
        sheet.add_command(label='员工表', command=self.i404)

        menubar.add_cascade(label='查看数据表', menu=sheet)
     #   menubar.add_command(label='刷新', command=self.ll)


        self.root['menu'] = menubar  # 设置菜单栏

    def returnback(self):
        self.i41.pack_forget()
        self.i42.pack_forget()
        self.i43.pack_forget()
        self.i44.pack_forget()
        self.i22.pack_forget()
        self.i33.pack_forget()
        self.inputPage11.pack_forget()
        self.inputpage12.pack_forget()
        self.inputpage13.pack()
        self.i11.pack_forget()

    def selldata(self):
        self.i41.pack_forget()
        self.i42.pack_forget()
        self.i43.pack_forget()
        self.i44.pack_forget()
        self.inputpage12.pack()
        self.i11.pack_forget()
        self.i22.pack_forget()
        self.i33.pack_forget()
        self.inputPage11.pack_forget()
        self.inputpage13.pack_forget()



    def inputData(self):
        self.inputPage11.pack()
        self.inputpage12.pack_forget()
        self.inputpage13.pack_forget()
        self.i11.pack_forget()
        self.i22.pack_forget()
        self.i33.pack_forget()
        self.i41.pack_forget()
        self.i42.pack_forget()
        self.i43.pack_forget()
        self.i44.pack_forget()


    def i1(self):
        self.i42.pack_forget()
        self.i43.pack_forget()
        self.i44.pack_forget()
        self.inputPage11.pack_forget()
        self.inputpage12.pack_forget()
        self.inputpage13.pack_forget()
        self.i22.pack_forget()
        self.i33.pack_forget()
        self.i41.pack_forget()


        self.i11.pack()

    def i2(self):
        self.i41.pack_forget()
        self.i42.pack_forget()
        self.i43.pack_forget()
        self.i44.pack_forget()
        self.inputPage11.pack_forget()
        self.inputpage12.pack_forget()
        self.inputpage13.pack_forget()
        self.i11.pack_forget()
        self.i22.pack()
        self.i33.pack_forget()



    def i3(self):
        self.inputPage11.pack_forget()
        self.inputpage12.pack_forget()
        self.inputpage13.pack_forget()
        self.i11.pack_forget()
        self.i33.pack()
        self.i41.pack_forget()
        self.i42.pack_forget()
        self.i43.pack_forget()
        self.i44.pack_forget()
        self.i22.pack_forget()

    def i401(self):
        self.inputPage11.pack_forget()
        self.inputpage12.pack_forget()
        self.inputpage13.pack_forget()
        self.i11.pack_forget()
        self.i33.pack_forget()
        self.i22.pack_forget()
        self.i42.pack_forget()
        self.i43.pack_forget()
        self.i44.pack_forget()
        self.i41.pack()

    def i402(self):
        self.inputPage11.pack_forget()
        self.inputpage12.pack_forget()
        self.inputpage13.pack_forget()
        self.i11.pack_forget()
        self.i33.pack_forget()
        self.i22.pack_forget()
        self.i41.pack_forget()
        self.i43.pack_forget()
        self.i44.pack_forget()

        self.i42.pack()
    def i403(self):
        self.inputPage11.pack_forget()
        self.inputpage12.pack_forget()
        self.inputpage13.pack_forget()
        self.i11.pack_forget()
        self.i33.pack_forget()
        self.i22.pack_forget()
        self.i41.pack_forget()
        self.i42.pack_forget()
        self.i44.pack_forget()
        self.i43.pack()
    def i404(self):
        self.inputPage11.pack_forget()
        self.inputpage12.pack_forget()
        self.inputpage13.pack_forget()
        self.i11.pack_forget()
        self.i33.pack_forget()
        self.i22.pack_forget()
        self.i41.pack_forget()
        self.i43.pack_forget()
        self.i42.pack_forget()
        self.i44.pack()






