from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox
from GetData import GetData

root = Tk()
root.title("DATAKU")
root.geometry("415x500")
root.configure(bg="lightblue")
root.resizable(False, False)
dataTable = []

def about():
    panelabout = Toplevel()
    myLabel = Label(panelabout, padx=50, pady=30, text="DATAKU \nSistem pendataan pengiriman Barang \n Nama  : Ira Fitri Yani \n NIM   : 1901280 \n Kelas : C2 ").pack()

def exit():
    ex = messagebox.askquestion("Konfirmasi", "Apa anda yakin?")
    if ex == "yes":
        root.quit()

def clear():
    clr = messagebox.askquestion("Konfirmasi", "Apa anda yakin?")
    if clr == "yes":
        dataTable.clear()
        messagebox.showinfo("", "Data Terhapus")

def open():
	global my_image
	layer.filename = filedialog.askopenfilename(initialdir="/gui/images", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
	my_image = ImageTk.PhotoImage(Image.open(layer.filename))
	my_image_label = Label(image=my_image).grid(row=12, column=0, padx=15, pady=14)

class Checkboxx(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, bg="lightblue", padx=5, text=pick, variable=var).pack(side=side)
            self.vars.append(var)
    def hasil(self):
        return map((lambda var: var.get()), self.vars)

def see():
    top = Toplevel()
    top.title("TABEL DATA")
    top.resizable(False, False)

    f1 = LabelFrame(top)
    Label(f1, text="Nama", width=15, bg="grey", fg="white").pack(side=LEFT)
    Label(f1, text="Alamat", width=15, bg="grey", fg="white").pack(side=LEFT)
    Label(f1, text="Telepon", width=15, bg="grey", fg="white").pack(side=LEFT)
    Label(f1, text="Jenis", width=15, bg="grey", fg="white").pack(side=LEFT)
    Label(f1, text="Mudah Pecah", width=15, bg="grey", fg="white").pack(side=LEFT)
    Label(f1, text="Besar", width=15, bg="grey", fg="white").pack(side=LEFT)
    Label(f1, text="Barang Lunak", width=15, bg="grey", fg="white").pack(side=LEFT)
    Label(f1, text="Ekspedisi", width=15, bg="grey", fg="white").pack(side=LEFT)
    f1.pack()

    for i in dataTable:
        f2 = LabelFrame(top)
        Label(f2, width=15, text=i.input1).pack(side=LEFT)
        Label(f2, width=15, text=i.input2).pack(side=LEFT)
        Label(f2, width=15, text=i.input3).pack(side=LEFT)
        Label(f2, width=15, text=i.drop).pack(side=LEFT)
        
        if (i.check[0]) == 1:
            Label(f2, text="*", width=15).pack(side=LEFT)
        else:
            Label(f2, text=" ", width=15).pack(side=LEFT)
        if (i.check[1]) == 1:
            Label(f2, text="*", width=15).pack(side=LEFT)
        else:
            Label(f2, text=" ", width=15).pack(side=LEFT)
        if (i.check[2]) == 1:
            Label(f2, text="*", width=15).pack(side=LEFT)
        else:
            Label(f2, text=" ", width=15).pack(side=LEFT)
        
        Label(f2, width=15, text=hsl).pack(side=LEFT)      
        f2.pack()

def submit():
    global hsl
    if(ekspedisi.get() == 1):
        hsl = "JNE"
    if(ekspedisi.get() == 2):
        hsl = "JNT"
    dataTable.append(GetData(input1.get(),input2.get(),input3.get(),drop.get(),list(check.hasil()),hsl))
    input1.delete(0, END)
    input2.delete(0, END)
    input3.delete(0, END)
    drop.delete(0, END)

layer = LabelFrame(root, padx=5, pady=5, bg="lightblue", borderwidth=0).grid(row=0, column=0)

b_see = Button(layer, text="See All Data", command=see, fg="#689ca6", padx=10, pady=5, width=12).grid(row=1, column=0)

b_clr = Button(layer, text="Clear All Data", command=clear, fg="#689ca6", padx=10, pady=5, width=12).grid(row=1, column=1)

b_abt = Button(layer, text="About", command=about, fg="#689ca6", padx=3, pady=5, width=12).grid(row=1, column=2)

b_exit = Button(layer, text="EXIT", command=exit, fg="red", padx=1, pady=5, width=12).grid(row=1, column=3)

space = Label(layer, text=".. DATAKU .. \n Sebuah sistem pengolahan data pengiriman", padx=25, pady=20, fg="grey", bg="lightblue").grid(row=2, columnspan=4)

label1 = Label(layer, text="Nama", padx=25, pady=12, bg="lightblue").grid(row=3, column=0)
input1 = Entry(layer, width=40)
input1.grid(row=3, column=1, columnspan=3, padx=15, pady=12)

label2 = Label(layer, text="Alamat", padx=25, pady=12, bg="lightblue").grid(row=4, column=0)
input2 = Entry(layer, width=40)
input2.grid(row=4, column=1, columnspan=3, padx=15, pady=12)

label3 = Label(layer, text="Telepon", padx=25, pady=12, bg="lightblue").grid(row=5, column=0)
input3 = Entry(layer, width=40)
input3.grid(row=5, column=1, columnspan=3, padx=15, pady=12)

label4 = Label(layer, text="Jenis", padx=25, pady=12, bg="lightblue").grid(row=6, column=0)
drop = Combobox(layer, width=37, values=['Elektronik','Pakaian', 'Makanan', 'Fotografi','Aksesoris','Kesehatan'])
drop.grid(row=6, column=1, columnspan=3, padx=15, pady=12)

label4 = Label(layer, text="Deskripsi", padx=25, pady=12, bg="lightblue").grid(row=7, column=0)
check = Checkboxx(layer, ['Mudah Pecah', 'Besar', 'Barang lunak'])
check.grid(row=7, column=1, columnspan=3)

label5 = Label(layer, text="Ekspedisi", padx=25, pady=12, bg="lightblue").grid(row=8, column=0)
ekspedisi = IntVar()
Radiobutton(layer, text="JNE", value=1, variable=ekspedisi, padx=25, pady=12, bg="lightblue").grid(row=8, column=1)
Radiobutton(layer, text="JNT", value=2, variable=ekspedisi, padx=25, pady=12, bg="lightblue").grid(row=8, column=2)

btnPhoto = Button(layer, text="OPEN PHOTO FILE ", command=open, width=52, height=1, fg="white", bg="grey").grid(row=9, columnspan=4, padx=15, pady=10)
btnSubmit = Button(layer, text="SUBMIT", command=submit, width=52, height=1, fg="white", bg="grey").grid(row=10, columnspan=4, padx=15, pady=10)

ver = Label(layer, text=".. V.1.0 ..", fg="grey", bg="lightblue").grid(row=11, columnspan=4)

root.mainloop()