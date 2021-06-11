from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
import DoAn as DA
import os
import hashlib

# Create object ---------------------------------------------------
ROOT = Tk()
ROOT.title("TH2L")
ROOT.geometry("1180x635")
ROOT.resizable(0,0)


# Add background ---------------------------------------------------
bg = PhotoImage(file="hinh9.png")
label1 = Label(ROOT, image=bg)
label1.place(x=0, y=0)


#Add label - textbox -----------------------------------------------
lbl_Welcome=Label(ROOT,text="GIẢI MÃ FILE",font=("Time 14",23,"bold"),fg='red')
lbl_Welcome.pack()

lbl_FileName=Label(ROOT,text="Nhập Tên File :",font=("Time 14",20),fg='blue').place(x=0,y=100)
txb_FileName=Entry(ROOT,width=40,font=("Time 14,",20))
txb_FileName.place(x=200,y=100)


# Kiểm tra FileName ------------------------------------------------
def btn_CheckFileName_Click():
    list_auto = []
    list_byHand = []

    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename[-4:] == ".txt" and filename[-13:] != "_KEY_Auto.txt" and filename[-15:] != "_KEY_byHand.txt":
                if filename[-9:] == "_Auto.txt":
                    list_auto.append(filename[:-9])
                elif filename[-11:] == "_byHand.txt":
                    list_byHand.append(filename[:-11])

    name=txb_FileName.get()
    check=False
    for i in list_auto:
        if name == i:
            check=True
            messagebox.showinfo("Thông báo","FileName hợp lệ")
            btn_XacThuc.config(state="normal")
    for i in list_byHand:
        if name ==i:
            check=True
            messagebox.showinfo("Thông báo","File bí mật: vui lòng nhập khoá")
            txb_FileName.configure(state="disable")
            txb_NhapKhoa.configure(state="normal")
            btn_CheckKhoa.config(state="normal")
    if check==False:
        messagebox.showerror("Thông báo","File không tồn tại")


btn_CheckFileName=Button(ROOT,text="CHECK FILE",font=("Time 14",15,"bold"),width=12,heigh=1,fg="Red",bg="#FFFF66",command=btn_CheckFileName_Click)
btn_CheckFileName.place(x=850,y=100)

# Kiểm tra KHOÁ nhập vào -----------------------------------------------------------------------
lbl_NhapKhoa=Label(ROOT,text="Nhập Khoá :",font=("Time 14",20),fg='blue').place(x=0,y=150)
txb_NhapKhoa=Entry(ROOT,width=40,font=("Time 14,",20),state="disabled")
txb_NhapKhoa.place(x=200,y=150)

def btn_CheckKhoa_Click():
    khoa=txb_NhapKhoa.get()
    KEY = hashlib.sha512(khoa.encode()).digest()
    b2 = KEY[32:48]
    KEY=b2
    filename_KEY=txb_FileName.get()+"_KEY_byHand.txt"

    data=open(filename_KEY,'rb').read()
    if data==KEY:
        messagebox.showinfo("Thông báo","KEY chính xác")
        btn_XacThuc.config(state="normal")
        txb_NhapKhoa.config(state="disabled")
    else:
        messagebox.showerror("Thông báo","KEY không chính xác")


btn_CheckKhoa=Button(ROOT,text="CHECK KHOÁ",font=("Time 14",15,"bold"),width=12,heigh=1,fg="Red",bg="#FFFF66",state="disabled",command=btn_CheckKhoa_Click)
btn_CheckKhoa.place(x=850,y=150)


# XÁC Thực ------------------------------------------------------
def GETFile(x):
    list_auto = []
    list_byHand = []

    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename[-4:] == ".txt" and filename[-13:] != "_KEY_Auto.txt" and filename[-15:] != "_KEY_byHand.txt":
                if filename[-9:] == "_Auto.txt":
                    list_auto.append(filename[:-9])
                elif filename[-11:] == "_byHand.txt":
                    list_byHand.append(filename[:-11])
    for i in list_auto:
        if x==i:
            return x+"_Auto.txt"
    for i in list_byHand:
        if x==i:
            return x+"_byHand.txt"

def btn_XacThuc_Click():
    x=txb_FileName.get()
    filesave=GETFile(x)
    fileRSA=txb_FileName.get()+"publickey.pem"
    check=DA.XacThuc(filesave,fileRSA)
    if check==True:
        messagebox.showinfo("Thông báo","Nội dung file không bị thay đổi")
        btn_GiaiMa.config(state="normal")
    if check==False:
        messagebox.showerror("Thông báo","Nội dung file bị thay đổi")

btn_XacThuc=Button(ROOT,text="XÁC THỰC",font=("Time 14",15,"bold"),width=27,heigh=1,fg="Red",bg="#FFFF66",state="disabled",command=btn_XacThuc_Click)
btn_XacThuc.place(x=50,y=200)


#   GIẢI MÃ -----------------------------------------------
def btn_GiaiMa_Click():
    len=txb_NhapKhoa.get()
    ten = txb_FileName.get()
    fileout=ten+"_OUT.txt"
    fileRSA=ten+"publickey.pem"
    if len=="":
        tenfile=ten+"_Auto.txt"
        tenfile_key=ten+"_KEY_Auto.txt"
        DA.GiaiMa(tenfile,tenfile_key,fileout,fileRSA)
        messagebox.showinfo("Thông báo","GIẢI MÃ THÀNH CÔNG")
    else:
        tenfile = ten + "_byHand.txt"
        tenfile_key=ten+"_KEY_byHand.txt"
        DA.GiaiMa(tenfile, tenfile_key, fileout,fileRSA)
        messagebox.showinfo("Thông báo","GIẢI MÃ THÀNH CÔNG")

btn_GiaiMa=Button(ROOT,text="GIẢI MÃ",font=("Time 14",20,"bold"),width=15,heigh=1,fg="Red",bg="#FFFF66",state="disabled",command=btn_GiaiMa_Click)
btn_GiaiMa.place(x=50,y=250)


#   RESET -----------------------------------------------------
def btn_Reset_Click():
    txb_FileName.config(state="normal")
    txb_NhapKhoa.config(state="normal")
    txb_FileName.delete(0,END)
    txb_NhapKhoa.delete(0,END)

    btn_CheckKhoa.config(state="disabled")
    btn_XacThuc.config(state="disabled")
    btn_GiaiMa.config(state="disabled")

    txb_NhapKhoa.config(state="disabled")
    messagebox.showinfo("Thông báo","RESET THÀNH CÔNG")

btn_Reset=Button(ROOT, text='RESET!',font=("Times 14",14,"bold"),height=3,width=7,bg="RED",command=btn_Reset_Click)
btn_Reset.place(x=1080,y=550)

ROOT.mainloop()





