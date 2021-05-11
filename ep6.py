from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime

root=Tk()
root.geometry('600x650')
root.title('โปรแกรมบันทึกค่าใช้จ่าย by Rymtarn')


menubar = Menu(root)
root.config(menu=menubar)

filemenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')

def About():
    messagebox.showinfo('About','โปรแกรมนี้คือโปรแกรมบันทึกข้อมูล\nสนใจบริจาคเราไหม ขอ 1 bitcoin\n Adress: ABC')



helpmenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)


donatemenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)


Tab=ttk.Notebook(root)
T1=Frame(Tab)
T2=Frame(Tab)
Tab.pack(fill=BOTH,expand=1)



#.subsample ใช้สำหรับย่อรูป แต่ไม่แนะนำให้ใช้
pic1=PhotoImage(file='expense.png').subsample(10)
pic2=PhotoImage(file='2408341.png').subsample(10)
pic3=PhotoImage(file='Picture1.png').subsample(10)
pic4=PhotoImage(file='save.png').subsample(15)
Tab.add(T1,text=f'{"เพิ่มค่าใช้จ่าย":^{20}}',image=pic1,compound='top')
Tab.add(T2,text=f'{"ค่าใช้จ่ายทั้งหมด":^{20}}',image=pic2,compound='top')
# compound เป็นตัวกำหนดว่า ให้รูปภาพอยู่ตรงไหน



F1 = Frame(T1)
#F1.place(x=50, y=50)
F1.pack()
days = {'Mon': 'จันทร์',
        'Tue': 'อังคาร',
        'Wed': 'พุธ',
        'Thur': 'พฤหัสบดี',
        'Fri': 'ศุกร์',
        'Sat': 'เสาร์',
        'Sun': 'อาทิตย์'}


def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    number = v_number.get()

    if expense == '':
        print('No Data')
        messagebox.showwarning('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
        return
    elif number=='':
        number=1
    elif price=='':
        messagebox.showwarning('Error', 'กรุณากรอกราคา')
        return

    total = float(number) * float(price)

    try:
        total = float(price) * float(number)
        # .get() ดึงค่ามาจาก v_expense = StringVar()
        print('รายการ:{} จำนวน :{}'.format(expense, number))
        print('ราคา:{} รวมทั้งหมด: {} บาท'.format(price, total))
        text = 'รายการ: {} จำนวน: {}\n'.format(expense, number)
        text = text + 'ราคา: {} รวมทั้งหมด: {} บาท'.format(price, total)
        today = datetime.now().strftime('%a')
        dt = datetime.now().strftime('%Y-%m-%d-{} %H:%M:%S'.format(days[today]))
        v_result.set(text)
        # clear ข้อมูลเก่า
        v_expense.set('')
        v_price.set('')
        v_number.set('')

        with open('homework_ep5.csv', 'a', encoding='utf-8', newline='') as f:
            fw = csv.writer(f)  # สร้างฟังชั่นสำหรับเขียนข้อมูล
            data = [dt,expense, number, price, total]  #
            fw.writerow(data)

            e1.focus()
            resulttable.delete(*resulttable.get.children()) #รหัสพิเศษ
            update_table()
            update_table()



    except:
            #print('ERROR')
            #messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกข้อมูลผิด')
            v_expense.set('')
            v_price.set('')
            v_number.set('')
# ทำให้สามารถกด enter ได้
root.bind('<Return>', Save)  # ต้องเพิ่มใน def Save (event=None) ด้วย

FONT1 = (None, 20)  # None is changed to 'Angsana New'


main_icon = PhotoImage(file='money.png').subsample(5)
Mainicon=Label(F1,image=main_icon)
Mainicon.pack()

# ......................text1
l = ttk.Label(F1, text='รายการค่าใช้จ่าย', font=FONT1).pack()
v_expense = StringVar()
e1 = ttk.Entry(F1, textvariable=v_expense, font=FONT1)
e1.pack()
# .................................

# ......................text2
l = ttk.Label(F1, text='จำนวน', font=FONT1).pack()
v_number = StringVar()
e2 = ttk.Entry(F1, textvariable=v_number, font=FONT1)
e2.pack()
# .................................

# ......................text3
l = ttk.Label(F1, text='ราคา (บาท)', font=FONT1, ).pack()
v_price = StringVar()
e3 = ttk.Entry(F1, textvariable=v_price, font=FONT1)
e3.pack()
# .................................


b2 = Button(F1, text='   Save', fg='white',image=pic4, bg="#660066",compound='left', command=Save)
b2.pack(ipadx=50, ipady=10, pady=20)



v_result = StringVar()
v_result.set('........ผลลัพธ์........')
result=ttk.Label(F1,textvariable=v_result,font=FONT1,foreground='blue')
result.pack(pady=20)



def read_csv():
	with open('homework_ep5.csv', encoding='utf-8', newline='') as f:
		fr = csv.reader(f)
		data = list(fr)
	return data

def update_record():
	getdata = read_csv()
	v_allrecord.set('')
	text = ''
	for d in getdata:
		txt = '{}---{}---{}---{}---{}\n'.format(d[0],d[1],d[2],d[3],d[4])
		text = text + txt
# \n เป็นการทำให้ขึ้นบรรทัดใหม่
	v_allrecord.set(text) # เป็นการ set ให้ข้อมูลทั้งหมดเข้าไปใน StringVar

v_allrecord = StringVar()
v_allrecord.set('-------All Record-------')
Allrecord = ttk.Label(T2,textvariable=v_allrecord,font=(None,10),foreground='purple')
Allrecord.pack()

#...........table................
#header = หัวข้อ
#ถ้าไม่สั่ง show='heading' จำกลายเป็น drop down

header = ['Datetime','Expense','Number','Price','Total']
resulttable = ttk.Treeview(T2, columns=header, show='headings',height=10)
resulttable.pack()

#for i in range(len(header)):
    #resulttable.heading(header[i],text=header[i])

for hd in header:
	resulttable.heading(hd,text=hd)


headerwidth = [150,170,80,80,80] #หน่วยเป็น pixel

for hd,W in zip(header,headerwidth):# จับคู่
	resulttable.column(hd,width=W)

def update_table():
	getdata = read_csv()
	for dt in getdata:
		resulttable.insert('','end',value=dt)


update_table()

print('GET CHILD:',resulttable.get_children())
update_record()

root.bind('<Tab>',lambda x: e2.focus())
root.mainloop()
