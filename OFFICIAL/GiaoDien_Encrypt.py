from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
import DoAn as DA
from tkinter import filedialog as fd

# Create object ---------------------------------------------
root = Tk()
root.title("TH2L")
root.geometry("1540x840")
root.resizable(0,0)

# Add background
bg = PhotoImage(file="hinh6.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

#Add label - textbox ----------------------------------------
lbl_Welcome=Label(root,text="MÃ HOÁ FILE",font=("Time 14",23,"bold"),fg='red')
lbl_Welcome.pack()

lbl_NhapDuLieu=Label(root,text="Nhập dữ liệu:",font=("Time 14",20),fg='blue').place(x=0,y=100)
txb_DuLieu=Entry(root,width=70,font=("Time 14,",20))
txb_DuLieu.place(x=200,y=100)

lbl_NameFileSave=Label(root,text="Nhập Tên File:",font=("Time 14",20),fg='blue').place(x=0,y=150)
txb_NameFileSave=Entry(root,width=70,font=("Time 14",20))
txb_NameFileSave.place(x=200,y=150)


#Ẩn khoá cá nhân --------------------------------------------
def funct1():
    lbl_KhoaCaNhan.place_forget()
def funct2():
    txb_KhoaCaNhan.place_forget()


#Tạo khoá tự động
def Show1():
    #Hàm để toạ khoá tự động
    tenfile_key = txb_NameFileSave.get() + '_KEY_Auto.txt'
    if txb_KhoaCaNhan.get()!="":
        txb_KhoaCaNhan.delete(0, END)

    if tenfile_key=="_KEY_Auto.txt":
        messagebox.showerror("Thông báo","Bạn Chưa nhập tên File")
    else:
        DA.Create_Key_Auto(tenfile_key)
        messagebox.showinfo("Thông báo","Tạo Khoá thành công")
        txb_KhoaCaNhan.config(state="disabled")
        btn_TaoKhoaCaNhan.config(state="disabled")
        En1()


#Tạo khoá bằng tay
def Show2():
    #Hàm để tạo khoá bằng tay
    key=txb_KhoaCaNhan.get()
    tenfile_key=txb_NameFileSave.get()+'_KEY_byHand.txt'
    if key=="":
        messagebox.showerror("Thông báo", "Bạn chưa nhập khoá")
    elif tenfile_key=="_KEY_byHand.txt":
        messagebox.showerror("Thông báo","Bạn Chưa nhập tên File")
    else:
        DA.Create_Key_by_Hand(key,tenfile_key)
        messagebox.showinfo("Thông báo","Tạo Khoá thành công")
        btn_TaoKhoaTuDong.config(state="disabled")
        En1()

#Bật - Tắt
def Dis1():
    btn_TaoKhoaCaNhan.config(state="disabled")
def Dis2():
    btn_TaoKhoaTuDong.config(state="disabled")
def Dis3():
    txb_KhoaCaNhan.config(state="disabled")
def En1():
    btn_MaHoa.config(state="normal")
def En2():
    txb_KhoaCaNhan.config(state="normal")
#Tạo khoá cá nhân _ Click
def btn_TaoKhoaCaNhan_click():
    key=txb_KhoaCaNhan.get()
    if key=="":
        messagebox.showerror("Thông báo","Khoá rỗng")
    elif key!="":
        Show2()
        #Dis2()
        Dis3()


#Tạo cái Label, button ----------------------------------
lbl_KhoaCaNhan=Label(root,text="Nhập Key: ",font=("Time 14",20),fg='blue')
txb_KhoaCaNhan=Entry(root,width=70,font=("Time 14",20))#,state='disabled')

btn_TaoKhoaTuDong=Button(root,text="Tạo Khoá Tự Động",font=("Time 14",20,"bold"),width=25,heigh=2,fg="Red",bg="#FFFF66",command=lambda:[Show1()])#,funct1(),funct2(),Dis1()])
btn_TaoKhoaTuDong.place(x=50,y=220)

btn_TaoKhoaCaNhan=Button(root,text="Tạo Khoá Cá Nhân",font=("Time 14",20,"bold"),width=25,heigh=2,fg="Red",bg="#FFFF66",command= lambda: [En2(),btn_TaoKhoaCaNhan_click()])
btn_TaoKhoaCaNhan.place(x=600,y=220)

lbl_KhoaCaNhan.place(x=0,y=320)
txb_KhoaCaNhan.place(x=200,y=320)


# MÃ HOÁ ---------------------------------------------------
#Check tất cả điều kiện
def Check1():
    DuLieu=txb_DuLieu.get()
    TenFile=txb_NameFileSave.get()
    if TenFile==""and DuLieu=="":
        return 2
    elif DuLieu[:44]=="D:/PYTHON_HackerRank/MatMaHoc_DoAn/OFFICIAL/" and TenFile!="":
        return 0
    elif DuLieu!="" and TenFile!="":
        return 1


def btn_MaHoa_click():
    check_mahoa=Check1()
    if check_mahoa==2:
        messagebox.showerror("Thông báo", "Dữ liệu không hợp lệ")
    elif check_mahoa==1:
        tenfile_key=""
        tenfile=""
        if txb_KhoaCaNhan.get()=="":
            tenfile_key = txb_NameFileSave.get() + '_KEY_Auto.txt'
            tenfile=txb_NameFileSave.get()+'_Auto.txt'
            dulieu = txb_DuLieu.get()
            filePEM = txb_NameFileSave.get()
            DA.MaHoa(tenfile_key, dulieu, tenfile,filePEM)
        elif txb_KhoaCaNhan.get()!="":
            tenfile_key = txb_NameFileSave.get() + '_KEY_byHand.txt'
            tenfile = txb_NameFileSave.get() + '_byHand.txt'
            filePEM=txb_NameFileSave.get()
            dulieu=txb_DuLieu.get()
            DA.MaHoa(tenfile_key,dulieu,tenfile,filePEM)
        messagebox.showinfo("Thông báo", "Mã hoá hoàn thành")
    elif check_mahoa == 0:
        if txb_KhoaCaNhan.get()=="":
            tenfile_key = txb_NameFileSave.get() + '_KEY_Auto.txt'
            tenfile=txb_NameFileSave.get()+'_Auto.txt'
            file_INPUT = txb_DuLieu.get()
            filePEM = txb_NameFileSave.get()
            DA.MaHoa_1(tenfile_key, file_INPUT, tenfile, filePEM)
        elif txb_KhoaCaNhan.get()!="":
            tenfile_key = txb_NameFileSave.get() + '_KEY_byHand.txt'
            tenfile = txb_NameFileSave.get() + '_byHand.txt'
            file_INPUT = txb_DuLieu.get()
            filePEM = txb_NameFileSave.get()
            DA.MaHoa_1(tenfile_key, file_INPUT, tenfile, filePEM)
        messagebox.showinfo("Thông báo", "Mã hoá hoàn thành")


btn_MaHoa=Button(root,text="Mã Hoá",font=("Time 14",22,"bold"),width=40,heigh=4,fg="#FF8000",bg="#CCFF99",state="disabled",command=btn_MaHoa_click)
btn_MaHoa.place(x=60,y=420)


# RESET ------------------------------------------------------
def btn_Reset_Click():
    txb_NameFileSave.delete(0,END)
    txb_DuLieu.delete(0,END)
    btn_MaHoa.config(state="disabled")
    btn_TaoKhoaTuDong.config(state="normal")
    btn_TaoKhoaCaNhan.config(state="normal")

    lbl_KhoaCaNhan.config(state="normal")
    txb_KhoaCaNhan.configure(state='normal')
    txb_KhoaCaNhan.delete(0, END)
    messagebox.showinfo("Thông báo","RESET THÀNH CÔNG")


btn_Reset=Button(root, text='RESET!',font=("Times 14",14,"bold"),height=3,width=7,bg="RED",command=btn_Reset_Click)
btn_Reset.place(x=1440,y=750)

#-----------------------------------------------------------------

def btn_BigFile_Click():
    filepath = fd.askopenfilename()
    # print(filepath)
    # file = open(filepath, 'r')
    # FILE=file.read()
    txb_DuLieu.insert(END,filepath)
    # file.close()
    messagebox.showinfo("Thông báo","Chọn File hoàn thành")


btn_Reset=Button(root, text='BIG FILE',font=("Times 14",14,"bold"),height=3,width=7,bg="RED",command=btn_BigFile_Click)
btn_Reset.place(x=1270,y=100)


# # Execute tkinter
root.mainloop()



