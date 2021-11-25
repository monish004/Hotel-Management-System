from tkinter import *
import random
from tkinter import ttk
from time import struct_time
import mysql.connector
import mysql
from datetime import datetime
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Booking Page")
        self.root.geometry("1295x700+230+110")

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("Arial",20,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)

        
        labelframe = LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("Arial",10,"bold"))
        labelframe.place(x=5,y=50,width=425,height=625)


        lbl_cust_contact=Label(labelframe,text="Customer Contact", font=("arial",12,"bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelframe,textvariable=self.var_contact, font=("arial",13,"bold"),width=20)
        entry_contact.grid(row=0,column=1,sticky=W)
        
        btnFetchData=Button(labelframe,command=self.Fetch_contact, text="Fetch data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)

        check_in_date=Label(labelframe,text="Check in Date",font=("Arial",10,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframe,textvariable=self.var_checkin,width=22,font=("Arial",10,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        lbl_Check_out=Label(labelframe,text="Check out Date",font=("Arial",10,"bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframe,textvariable=self.var_checkout,width=22,font=("Arial",10,"bold"))
        txt_Check_out.grid(row=2,column=1)

        label_RoomType=Label(labelframe,text="Room Type",font=("Arial",10,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        combo_RoomType=ttk.Combobox(labelframe,textvariable=self.var_roomtype,font=("Arial",10,"bold"),width=20,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxury")
        combo_RoomType.grid(row=3,column=1)

        lblRoomAvailabe=Label(labelframe,text="Available Room",font=("Arial",10,"bold"),padx=2,pady=6)
        lblRoomAvailabe.grid(row=4,column=0,sticky=W)
        txtlblRoomAvailabe=ttk.Entry(labelframe,textvariable=self.var_roomavailable,width=22,font=("Arial",10,"bold"))
        txtlblRoomAvailabe.grid(row=4,column=1)

        lblMeal=Label(labelframe,text="Meal",font=("Arial",10,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        combo_Meal=ttk.Combobox(labelframe,textvariable=self.var_meal,font=("Arial",10,"bold"),width=20,state="readonly")
        combo_Meal["value"]=("BreakFast","Lunch","Dinner")
        combo_Meal.grid(row=5,column=1)

        lblNoOfDays=Label(labelframe,text="No of days",font=("Arial",10,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframe,textvariable=self.var_noofdays,width=22,font=("Arial",10,"bold"))
        txtNoOfDays.grid(row=6,column=1)

        lblNoOfDays=Label(labelframe,text="Paid Tax",font=("Arial",10,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframe,textvariable=self.var_paidtax,width=22,font=("Arial",10,"bold"))
        txtNoOfDays.grid(row=7,column=1)

        lblNoOfDays=Label(labelframe,text="Sub Total",font=("Arial",10,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframe,textvariable=self.var_actualtotal,width=22,font=("Arial",10,"bold"))
        txtNoOfDays.grid(row=8,column=1)

        lblIdNumber=Label(labelframe,text="Total Cost",font=("Arial",10,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtlblIdNumber=ttk.Entry(labelframe,textvariable=self.var_total,width=22,font=("Arial",10,"bold"))
        txtlblIdNumber.grid(row=9,column=1)

        
        btnBill=Button(labelframe, text="Bill",command=self.total,font=("arial",11,"bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

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
        tableframe.place(x=430,y=280,width=860,height=400)


        tabledetail = LabelFrame(tableframe,bd=2,relief=RIDGE)
        tabledetail.place(x=0,y=0,width=860,height=260)
        scrollx=ttk.Scrollbar(tabledetail,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(tabledetail,orient=VERTICAL)
        self.room_table=ttk.Treeview(tabledetail,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.room_table.xview)
        scrolly.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room type")
        self.room_table.heading("roomavailable",text="Room available")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No of days")
        

        self.room_table["show"]="headings"
        self.room_table.column("contact",width=120)
        self.room_table.column("checkin",width=120)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()


    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parents = self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Mohitisbest1",database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailable.get(),
                                                                                self.var_meal.get(),
                                                                                self.var_noofdays.get()

                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Room booked",parent= self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong: {str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mohitisbest1", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cuersor(self,events=""):
        cusrsor_row = self.room_table.focus()
        content = self.room_table.item(cusrsor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent = self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Mohitisbest1",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                                                            self.var_checkin.get(),
                                                                                                                                            self.var_checkout.get(),
                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                            self.var_meal.get(),
                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                            self.var_contact.get()
                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updates successfully",parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("hotel management system","do you want to delete this customer",parent = self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Mohitisbest1",database="management")
            my_cursor = conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Mohitisbest1", database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")

            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number Not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                conn = mysql.connector.connect(host="localhost", username="root", password="Mohitisbest1", database="management")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                conn = mysql.connector.connect(host="localhost", username="root", password="Mohitisbest1", database="management")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl3 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl3.place(x=90, y=60)

                conn = mysql.connector.connect(host="localhost", username="root", password="Mohitisbest1", database="management")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblNationality = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblNationality.place(x=0, y=90)

                lbl4 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=90)

                conn = mysql.connector.connect(host="localhost", username="root", password="Mohitisbest1", database="management")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAddress = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl5 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=120)

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mohitisbest1", database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs. "+str("%.2f"%((q5)*0.1))
            ST="Rs. "+str("%.2f"%((q5)))
            TT="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.09))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Double"):
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.09))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double"):
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs. " + str("%.2f" % ((q5) * 0.09))
            ST = "Rs. " + str("%.2f" % ((q5)))
            TT = "Rs. " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
