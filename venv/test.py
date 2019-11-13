'''


Label(self, text='送货日期： ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E)
        Label(self, text='商品编号： ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E)
        Label(self, text='商品编号： ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E)
        
        
        
self.inputPage12 = InputFrame12(self.root)  # 创建不同Frame
        self.inputPage13 = InputFrame13(self.root)  # 创建不同Frame
        self.inputPage21 = InputFrame21(self.root)  # 创建不同Frame
        self.inputPage22 = InputFrame22(self.root)  # 创建不同Frame
        self.inputPage23 = InputFrame23(self.root)  # 创建不同Frame
        self.inputPage24 = InputFrame24(self.root)  # 创建不同Frame
        self.inputPage31 = InputFrame31(self.root)  # 创建不同Frame
        self.inputPage32 = InputFrame32(self.root)  # 创建不同Frame
        self.inputPage33 = InputFrame33(self.root)  # 创建不同Frame
        self.inputPage34 = InputFrame34(self.root)  # 创建不同Frame
        self.inputPage41 = InputFrame41(self.root)  # 创建不同Frame
        self.inputPage51 = InputFrame51(self.root)  # 创建不同Frame
        self.inputPage52 = InputFrame52(self.root)  # 创建不同Frame
        self.inputPage53 = InputFrame53(self.root)  # 创建不同Frame
        self.inputPage54 = InputFrame54(self.root)  # 创建不同Frame
     '''


class if1(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()



'''
self.n12.delete(0, END)
self.n13.delete(0, END)
self.n14.delete(0, END)
self.n15.delete(0, END)
self.n16.delete(0, END)
self.n17.delete(0, END)
self.n18.delete(0, END)
self.n19.delete(0, END)
self.n20.delete(0, END)
self.n21.delete(0, END)
'''
import sqlite3
cx = sqlite3.connect('sellsys.db')
cu = cx.cursor()
cu.execute("select * from retreat")
cu.fetchall()
for item in cu.fetchall()
        for element in item
                print element


sellmenu = Menu(menubar, tearoff=0)
        sellmenu.add_command(label='日销售统计', command=self.inputData)
        sellmenu.add_command(label='月销售统计', command=self.inputData)
        sellmenu.add_command(label='季销售统计', command=self.inputData)
        sellmenu.add_command(label='年销售统计', command=self.inputData)


def ll(self):
    self.inputPage11.destroy()
    self.inputpage12.destroy()
    self.inputpage13.destroy()
    self.i11.destroy()
    self.inputPage11.pack()
    self.inputpage12.pack()
    self.inputpage13.pack()
    self.i11.pack()


sheet = Menu(menubar, tearoff=0)
        sheet.add_command(label='进货表', command=self.inputData)
        sheet.add_command(label='销售表', command=self.inputData)
        sheet.add_command(label='退货表', command=self.inputData)
        sheet.add_command(label='员工表', command=self.inputData)
        sheet.add_command(label='进货表', command=self.inputData)