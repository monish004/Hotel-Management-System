from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import random   


class Customer_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Window")
        self.root.geometry("1295x700+230+110")


        self.var_ref=StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()


        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("Arial",20,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)


        labelframe = LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("Arial",10,"bold"))
        labelframe.place(x=5,y=50,width=425,height=625)

        
        lbl_cust_ref=Label(labelframe,text="Customer Reference",font=("Arial",10,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframe,textvariable=self.var_ref,width=22,font=("Arial",10,"bold"),state='readonly')
        entry_ref.grid(row=0,column=1)

        cname=Label(labelframe,text="Customer FullName",font=("Arial",10,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        entry_cname=ttk.Entry(labelframe,textvariable=self.var_cust_name,width=22,font=("Arial",10,"bold"))
        entry_cname.grid(row=1,column=1)

        lbl_gender=Label(labelframe,text="Gender",font=("Arial",10,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=2,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframe,textvariable=self.var_gender,font=("Arial",10,"bold"),width=20,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.grid(row=2,column=1)

        cmobile=Label(labelframe,text="Mobile Number",font=("Arial",10,"bold"),padx=2,pady=6)
        cmobile.grid(row=3,column=0,sticky=W)
        entry_cmobile=ttk.Entry(labelframe,textvariable=self.var_mobile,width=22,font=("Arial",10,"bold"))
        entry_cmobile.grid(row=3,column=1)

        cemail=Label(labelframe,text="Email Id",font=("Arial",10,"bold"),padx=2,pady=6)
        cemail.grid(row=4,column=0,sticky=W)
        entry_cemail=ttk.Entry(labelframe,textvariable=self.var_email,width=22,font=("Arial",10,"bold"))
        entry_cemail.grid(row=4,column=1)

        lbl_nationality=Label(labelframe,text="Nationality",font=("Arial",10,"bold"),padx=2,pady=6)
        lbl_nationality.grid(row=5,column=0,sticky=W)
        combo_nationality=ttk.Combobox(labelframe,textvariable=self.var_nationality,font=("Arial",10,"bold"),width=20,state="readonly")
        combo_nationality["value"]=("India","Japan","England")
        combo_nationality.grid(row=5,column=1)

        lbl_Idproof=Label(labelframe,text="Id Proof",font=("Arial",10,"bold"),padx=2,pady=6)
        lbl_Idproof.grid(row=6,column=0,sticky=W)
        combo_Idproof=ttk.Combobox(labelframe,textvariable=self.var_id_proof,font=("Arial",10,"bold"),width=20,state="readonly")
        combo_Idproof["value"]=("Adhaar","Passport","Pan Card")
        combo_Idproof.grid(row=6,column=1)

        cidnum=Label(labelframe,text="Id Number",font=("Arial",10,"bold"),padx=2,pady=6)
        cidnum.grid(row=7,column=0,sticky=W)
        entry_cidnum=ttk.Entry(labelframe,textvariable=self.var_id_number,width=22,font=("Arial",10,"bold"))
        entry_cidnum.grid(row=7,column=1)

        caddress=Label(labelframe,text="Address",font=("Arial",10,"bold"),padx=2,pady=6)
        caddress.grid(row=8,column=0,sticky=W)
        entry_caddress=ttk.Entry(labelframe,textvariable=self.var_address,width=22,font=("Arial",10,"bold"))
        entry_caddress.grid(row=8,column=1)


        btn_frame=Frame(labelframe,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=570,width=420,height=33)

        add_btn = Button(btn_frame,text="ADD",command=self.add_data,width=12,font=("Arial",10,"bold"),bg="black",fg="gold",cursor="hand2")
        add_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="UPDATE",command=self.update,width=12,font=("Arial",10,"bold"),bg="black",fg="gold",cursor="hand2")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="DELETE",command=self.mDelete,width=12,font=("Arial",10,"bold"),bg="black",fg="gold",cursor="hand2")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="RESET",command=self.reset,width=11,font=("Arial",10,"bold"),bg="black",fg="gold",cursor="hand2")
        reset_btn.grid(row=0,column=3)


        tableframe = LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details",font=("Arial",10,"bold"))
        tableframe.place(x=430,y=50,width=860,height=625)


        tabledetail = LabelFrame(tableframe,bd=2,relief=RIDGE)
        tabledetail.place(x=0,y=50,width=856,height=554)
        scrollx=ttk.Scrollbar(tabledetail,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(tabledetail,orient=VERTICAL)
        self.custtable=ttk.Treeview(tabledetail,column=("Customer Reference","Customer FullName","Gender","Mobile Number","Email Id",
                                                        "Nationality","Id Proof","Id Number","Address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.custtable.xview)
        scrolly.config(command=self.custtable.yview)

        self.custtable.heading("Customer Reference",text="Customer Reference")
        self.custtable.heading("Customer FullName",text="Customer FullName")
        self.custtable.heading("Gender",text="Gender")
        self.custtable.heading("Mobile Number",text="Mobile Number")
        self.custtable.heading("Email Id",text="Email Id")
        self.custtable.heading("Nationality",text="Nationality")
        self.custtable.heading("Id Proof",text="Id Proof")
        self.custtable.heading("Id Number",text="Id Number")
        self.custtable.heading("Address",text="Address")

        self.custtable["show"]="headings"
        self.custtable.column("Customer Reference",width=120)
        self.custtable.column("Customer FullName",width=120)
        self.custtable.column("Gender",width=100)
        self.custtable.column("Mobile Number",width=100)
        self.custtable.column("Email Id",width=100)
        self.custtable.column("Nationality",width=100)
        self.custtable.column("Id Proof",width=100)
        self.custtable.column("Id Number",width=100)
        self.custtable.column("Address",width=100)
        self.custtable.pack(fill=BOTH,expand=1)
        self.custtable.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_cust_name.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host ="localhost",username="root",password="Mohitisbest1",database = "management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_ref.get(),
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_id_proof.get(),
                                                                                    self.var_id_number.get(),
                                                                                    self.var_address.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "customer has been added", parent = self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}", parent = self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "Mohitisbest1", database = "management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.custtable.delete(*self.custtable.get_children())
            for i in rows:
                self.custtable.insert("", END, values = i)
                conn.commit()
            conn.close()

    def get_cuersor(self, event=""):
        cusrsor_row=self.custtable.focus()
        content=self.custtable.item(cusrsor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_mobile.set(row[3]),
        self.var_email.set(row[4]),
        self.var_nationality.set(row[5]),
        self.var_id_proof.set(row[6]),
        self.var_id_number.set(row[7]),
        self.var_address.set(row[8])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mohitisbest1",database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s, Gender=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s where Ref=%s", (

                                                                                                                                                            self.var_cust_name.get(),
                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                            self.var_mobile.get(),
                                                                                                                                                            self.var_email.get(),
                                                                                                                                                            self.var_nationality.get(),
                                                                                                                                                            self.var_id_proof.get(),
                                                                                                                                                            self.var_id_number.get(),
                                                                                                                                                            self.var_address.get(),
                                                                                                                                                            self.var_ref.get()
                                                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details has been updated successfully", parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mohitisbest1", database="management")
            my_cursor = conn.cursor()
            query = "Delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_cust_name.set(""),
        self.var_gender.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set(""),
        self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))


if __name__ == "__main__":
    root=Tk()
    obj1=Customer_Window(root)
    root.mainloop() 
