from tkinter import*
from customer import Customer_Window
from room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1545x800+0+0")


        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("Arial",50,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1545,height=80)


        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=80,width=1545,height=720)


        lbl_menu=Label(main_frame,text="MENU",font=("Arial",30,"bold"),bg="black",fg="gold")
        lbl_menu.place(x=0,y=0,width=230)

        
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=50,width=230,height=663)

        
        cust_btn = Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=18,font=("Arial",15,"bold"),bg="black",fg="gold",cursor="hand2")
        cust_btn.grid(row=0,column=0)

        room_btn = Button(btn_frame,text="ROOM",command=self.roombooking,width=18,font=("Arial",15,"bold"),bg="black",fg="gold",cursor="hand2")
        room_btn.grid(row=1,column=0)

        details_btn = Button(btn_frame,text="DETAILS",command=self.details_room,width=18,font=("Arial",15,"bold"),bg="black",fg="gold",cursor="hand2")
        details_btn.grid(row=2,column=0)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer_Window(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
