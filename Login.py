from tkinter import *
import tkinter as tk
from tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import datetime as dt

    
class Login_Page:
    def __init__(self,me):
        self.me=me
        self.me.title("login form")
        self.me.geometry("1550x800+0+0")
        #image
        self.image1=Image.open(r"B:\python2021\python projects\taxi booking\sushilbakcground.jpg")
        self.bg=ImageTk.PhotoImage(self.image1)
         
        lbl_bg=Label(self.me,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        #frame 
        self.frame1= Frame(self.me,bg="black")
        self.frame1.place(x=560,y=170,width=440,height=440)
        
        self.img1=Image.open(r"B:\python2021\python projects\taxi booking\user1.png")
        self.img1=self.img1.resize((100,100),Image.ANTIALIAS)
        self.img11=ImageTk.PhotoImage(self.img1)

        self.lbl_img1=Label(self.me,image=self.img11,bg="red",borderwidth=0)
        self.lbl_img1.place(x=740,y=180,width=100,height=100)
        
        
        
        # label

        self.str_email=Label(self.frame1,text="Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        self.str_email.place(x=90,y=210)
        
        str_psd= Label(self.frame1,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        str_psd.place(x=90,y=270)
  
        
        str_register=Label(self.frame1,text="Didn't have account yet?",font=("times new roman",10,"bold"),bg="black",fg="white")
        str_register.place(x=20,y=400)
        
        
        # entry box
        self.em_entry=Entry(self.frame1,font=("times new roman",15,"bold"),fg="black",bg="white",borderwidth=4)
        self.em_entry.place(x=200,y=210,width=200)
        
        self.psd_entry= Entry(self.frame1,show='*',font=("times new roman",15,"bold"),fg="black",bg="white",borderwidth=4)
        self.psd_entry.place(x=200,y=270,width=200)
        
        
        #button
        login_btn= Button(self.frame1,text="login",command=self.login,font=("times new roman",20,"bold"),bg="black",fg="white")
        login_btn.place(x=200,y=350,width=100,height=40)
        
        register_btn=Button(self.frame1,command=self.register_page, text="register",font=("times new roman",13,"bold"),bg="black",fg="red")
        register_btn.place(x=155,y=400,width=80,height=20)

        #treeview style code
        style=ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",foreground="white",background="black",fieldbackground="black")
        style.map("Treeview",background=[("selected","red")])
      
      #to enter in register page
    def register_page(self):
        self.reg_win=Toplevel(self.me) 
        self.app= registration(self.reg_win)

        
    def login(self):
        #validation check
        if self.em_entry.get()=="" or self.psd_entry.get()=="":
            messagebox.showerror("error","field are empty")
            
        # enter into adming page 
        elif(self.em_entry=="damon" or self.psd_entry.get()=="damon" ):
            self.admin_form()
        else:
            try:
                #database connection
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
                my_cursor=conn.cursor()
                
                #execution of sql query in cursor
                my_cursor.execute("select * from customer_register where email=%s and password=%s",( self.em_entry.get(),
                                self.psd_entry.get()
                ))
                
                #selecting data from database using fetchone 
                row=my_cursor.fetchone()
                if row==None:
                    my_cursor.execute("select * from driver where email=%s and password=%s",(self.em_entry.get(),self.psd_entry.get()))
                    row2=my_cursor.fetchone()
                    if row2==None:
                        messagebox.showerror("error","wrong email or password")
                    else:
                        #making global variable
                        global driver_id
                        global driver_name
                        driver_id=row2[0]
                        driver_name=row2[1]
                        messagebox.showinfo("success","it is driver")
                        self.driver_window()
                    
                else:
                    messagebox.showinfo("success")
                    #assining customer id 
                    x=row[0]
                    
                    #assining customer name
                    y=row[1]
                    global profile_value1
                    profile_value1=y
                    global profile_value
                    profile_value=x
                    
#calling booking class
                    self.ui=booking(me)
                    
                    
                    
                conn.commit()
#closing database connection
                conn.close()
            except Exception as e:
                messagebox.showerror("error",e)

# calling adming form
    def admin_form(self):
        self.admin_win=admin(me)
        self.admin_win.admin_table()
        
#calling driver page 
    def driver_window(self):
        self.dri_win1=driver_window(me)

        
        
#registration page
class registration:
    def __init__(self,me):
        self.me= me
        self.me.title("Registration")
        self.me.geometry("1550x800+0+0")

        
        # variable for text variable in entry box
        self.name=StringVar()
        self.address=StringVar()
        self.email=StringVar()
        self.phone=StringVar()
        self.password=StringVar()
        self.payment=StringVar()

        
        # image
        img_reg=Image.open(r"B:\python2021\python projects\taxi booking\sushilbakcground.jpg")
        self.img_reg= ImageTk.PhotoImage(img_reg)
         
    

        # lable
        regimg_lbl=Label(self.me,image=self.img_reg)
        regimg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        reg_frame=Frame(self.me,bg="black")
        reg_frame.place(x=560,y=150,width=840,height=540)
        
        
        regtxt_lbl=Label(reg_frame,text="Register for free",font=("times new roman",20,"bold"),bg="black",fg="red")
        regtxt_lbl.place(x=10,y=20)
        
        name_lbl=Label(reg_frame,text="Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        name_lbl.place(x=50,y=100)
        
        
        address_lbl=Label(reg_frame,text="Address",font=("times new roman",15,"bold"),fg="white",bg="black")
        address_lbl.place(x=400,y=100)
        
        phone_lbl=Label(reg_frame,text="phone",font=("times new roman",15,"bold"),bg="black",fg="white")
        phone_lbl.place(x=50,y=150)
        
        email_lbl=Label(reg_frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        email_lbl.place(x=400,y=150)
        
        psd_lbl=Label(reg_frame,text="password",font=("times new roman",15,"bold"),bg="black",fg="white")
        psd_lbl.place(x=50,y=200)
        
        payment_lbl=Label(reg_frame,text="payment by",font=("times new roman",15,"bold"),bg="black",fg="white")
        payment_lbl.place(x=400,y=200)
        
 
        #entry box
        name_entry= Entry(reg_frame,textvariabl=self.name,  font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        name_entry.place(x=150,y=100,width=200)
        
        address_entry= Entry(reg_frame,textvariabl=self.address, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        address_entry.place(x=500,y=100,width=200)
        
        phone_entry= Entry(reg_frame,textvariabl=self.phone, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        phone_entry.place(x=150,y=150,width=200)
        
        email_entry= Entry(reg_frame,textvariabl=self.email, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        email_entry.place(x=500,y=150,width=200)
        
        psd_entry= Entry(reg_frame,textvariabl=self.password, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        psd_entry.place(x=150,y=200,width=200)
        
        
        #combobox
        payment_cmbx=ttk.Combobox(reg_frame,textvariable=self.payment,font=("times new roman",15,"bold"),state="readonly")
        payment_cmbx["values"]=("select","online payment","cash")
        payment_cmbx.place(x=500,y=200,width=200)
        payment_cmbx.current(0)
        
        
        #button
        reg_btn= Button(reg_frame,command=self.register_val,text="sign up",font=("times new roman",20,"bold"),fg="white",bg="black")
        reg_btn.place(x=380,y=400,width=120,height=40)
        
        log_btn= Button(reg_frame,command=self.login_page,text="<<login",font=("times new roman",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
        log_btn.place(x=40,y=450,width=120,height=40)
        
   
   #back in login page    
    def login_page(self):
        self.me.destroy()
        
#inserting user register credentials into database
    def register_val(self):
# validatation for user input
        if self.name.get()=="" or self.address.get()=="" or self.email.get()==""    or   self.phone.get()=="" or self.password.get()=="" or self.payment.get()=="":
            messagebox.showerror("error","all field are required", parent = self.me)
            
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
                my_cursor=conn.cursor()
#inserting data into customer_register table of database
                my_cursor.execute("insert into customer_register (name,address,phone,email,password,pay_method) values (%s,%s,%s,%s,%s,%s)",(
                                                                                                                                                               self.name.get(),
                                                                                                                                                               self.address.get(),
                                                                                                                                                               self.phone.get(),
                                                                                                                                                               self.email.get(),
                                                                                                                                                               self.password.get(),
                                                                                                                                                               self.payment.get(),
                                                                      ))
                
                conn.commit()
                conn.close()
                messagebox.showinfo("success","data is registered",parent=self.me)    
                self.me.destroy()
            
            except Exception as es:
                messagebox("error",f"Error {str(es)}", parent= self.me)
                
            
    
    
    

#booking page
class booking:
    def __init__(self,me):
        self.me=me
        self.me.title("booking page")
        self.me.geometry("1550x800+0+0")
        self.me.background='black'
        
        self.img= Image.open(r"B:\python2021\python projects\taxi booking\sushilbakcground.jpg")
        self.img=ImageTk.PhotoImage(self.img)
        
        img_lbl= Label(self.me,image=self.img)
        img_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #frames
        self.table_frame=Frame(self.me,bg="black")
        self.table_frame.place(x=760,y=150,width=700,height=540)
        
        self.book_frame= Frame(self.me,bg="black")
        self.book_frame.place(x=60,y=150,width=700,height=540)
        
        
        # text variable for booking entry boxes
        self.pickup=StringVar()
        self.drop= StringVar()
        self.date= StringVar()
        self.time= StringVar()
        self.price=IntVar()
        
        # all labels
        booktxt=Label(self.book_frame,text="Book Now",font=("times new roman",20,"bold"),bg="black",fg="red")
        booktxt.place(x=10,y=20)

        
        date_lbl=Label(self.book_frame,text="date",font=("times new roman",15,"bold"),bg="black",fg="white")
        date_lbl.place(x=50,y=100)
        
        
        time_lbl=Label(self.book_frame,text="time",font=("times new roman",15,"bold"),fg="white",bg="black")
        time_lbl.place(x=410,y=100)
        
        pickup_lbl=Label(self.book_frame,text="pickup location",font=("times new roman",15,"bold"),bg="black",fg="white")
        pickup_lbl.place(x=50,y=200)
        
        drop_lbl=Label(self.book_frame,text="drop locationnnn",font=("times new roman",15,"bold"),fg="white",bg="black")
        drop_lbl.place(x=410,y=200)
        
        price_lbl=Label(self.book_frame,text="path distance(KM)",font=("times new roman",15,"bold"),bg="black",fg="white")
        price_lbl.place(x=50,y=300)

        self.profile_lbl= Label(self.book_frame,text=profile_value1,font=("times new roman",20,"bold"),fg="white",bg="black")
        self.profile_lbl.place(x=200,y=20)
        
        
        #inserting date into entry box
        date_last=dt.datetime.now()
        format_date=f"{date_last:%a,%b %d %y}"
        self.date.set(format_date)
        
        # all booking entry box
        date_entry= Entry(self.book_frame,textvariabl=self.date,state='readonly', font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        date_entry.place(x=50,y=150,width=200)
        
        time_entry= Entry(self.book_frame,textvariabl=self.time,  font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        time_entry.place(x=410,y=150,width=200)
    
        pickup_entry= Entry(self.book_frame,textvariabl=self.pickup, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        pickup_entry.place(x=50,y=250,width=200)
        
        drop_entry= Entry(self.book_frame,textvariabl=self.drop, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        drop_entry.place(x=410,y=250,width=200)
        
        price_entry= Entry(self.book_frame,textvariabl=self.price, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        price_entry.place(x=50,y=350,width=200)
        
        # button
        confirm_btn= Button(self.book_frame,command=self.booking_val,text="confirm",font=("times new roman",20,"bold"),fg="white",bg="black")
        confirm_btn.place(x=265,y=400,width=120,height=40)
        
        view_btm= Button(self.book_frame,command=self.small_scrn1,text="view",font=("times new roman",20,"bold"),fg="white",bg="black")
        view_btm.place(x=400,y=400,width=120,height=40)
        
        back_btn1=Button(self.me,command=self.logout2,text="logout",font=("times new roman",15,"bold"),fg="red",bg="black")
        back_btn1.place(x=1400,y=20)
        
    #converting km into price  
    def kmtoprice(self):
        self.x=self.price.get() 
        self.y=self.x*20
        self.average=self.y+((10*self.y)/100)
        return self.average
        
#inserting user booking data into database 
    def booking_val(self):
        #validation
        if self.pickup.get()=="" or self.date.get()=="" or self.drop.get()=="" or self.time.get()=="":
            messagebox.showerror("error","all field are required")
        else:
            try:
                self.priceforkm=self.kmtoprice()
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
                my_cursor=conn.cursor()
                #query execution
                my_cursor.execute("insert into booking (date,time,pickup_location,drop_location,sn,ride_status,price) values(%s,%s,%s,%s,%s,%s,%s)",(
                                self.date.get(),
                                self.time.get(),
                                self.pickup.get(),
                                self.drop.get(),
                                profile_value,
                                "pending",
                                self.priceforkm
                                
                ))
                
                conn.commit()
                conn.close()
                messagebox.showinfo("success","booked")
                self.reset_val()
                self.small_scrn()
            
            except Exception as e:
                messagebox.showerror("error",e)
            
           
    
            
 
    #function to reset entry boxes
    def reset_val(self):
        for widget in self.book_frame.winfo_children():
            
            if isinstance(widget,Entry):
                widget.delete(0,'end')
    
    #function to enter into window which shows recent booking request         
    def small_scrn(self):
        self.sm_scrn=Toplevel(self.me)
        self.sm_scrn=smallscrean(self.sm_scrn)
    
    #function to enter into window which show all booking records of customer
    def small_scrn1(self):
        self.srn1=Toplevel(self.me)
        self.srn1=allbookingdata(self.srn1)
    
    #logout function
    def logout2(self):
         msg_box = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',icon='warning')
         if msg_box=='yes':
             self.application=Login_Page(me)   


#recent booking request window class
class smallscrean:
     def __init__(self,me):
        self.me=me
        self.me.title("booking page")
        self.me.geometry("700x320+740+200")
        self.img= Image.open(r"B:\python2021\python projects\taxi booking\sushilbakcground.jpg")
        self.img=ImageTk.PhotoImage(self.img)
        
        img_lbl= Label(self.me,image=self.img)
        img_lbl.place(x=0,y=0,relwidth=1,relheight=1)
    
        self.dri_av_frame= Frame(self.me,bg="black")
        self.dri_av_frame.place(x=10,y=10,width=670,height=250)
        
        
        showprice_btn= Button(self.me,command=self.select_price,text="price",font=("times new roman",15,"bold"),fg="white",bg="black")
        showprice_btn.place(x=10,y=260) 
        
        
        self.showprice_entry=Entry(self.me,text="price",font=("times new roman",15,"bold"),fg="white",bg="black")
        self.showprice_entry.place(x=100,y=260,width=70,height=40) 
       
        
        cancel_button= Button(self.me,text="cancel",command=self.delete_data,font=("times new roman",15,"bold"),fg="white",bg="black")
        cancel_button.place(x=600,y=260) 
        self.view_table()
        
        
        
    #showing table of recent booking request
     def view_table(self):
         try:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from booking where ride_status='pending' and sn=%s ",(
                                              profile_value,
                                              
            ))
            
            self.tree=ttk.Treeview(self.dri_av_frame)
            self.tree['show']='headings'
            self.tree.place(x=0,y=0,width=100,height=100)
           
            
            # assign column
            self.tree["columns"]=("id","price","date","time","pickup_location","drop_location","ride status")
            
            
            #assign width and anchor
            self.tree.column("id",width=50,minwidth=100,anchor=tk.CENTER) 
            self.tree.column("price",width=50,minwidth=100,anchor=tk.CENTER) 
            self.tree.column("date",width=100,minwidth=100,anchor=tk.CENTER) 
            self.tree.column("time",width=100,minwidth=100,anchor=tk.CENTER) 
            self.tree.column("pickup_location",width=100,minwidth=100,anchor=tk.CENTER) 
            self.tree.column("drop_location",width=100,minwidth=150,anchor=tk.CENTER) 
            self.tree.column("ride status",width=200,minwidth=150,anchor=tk.CENTER) 
            
            
            # assing heading
            
            self.tree.heading("id",text="id",anchor=tk.CENTER)
            self.tree.heading("price",text="price",anchor=tk.CENTER)
            self.tree.heading("date",text="date",anchor=tk.CENTER)
            self.tree.heading("time",text="time",anchor=tk.CENTER)
            self.tree.heading("pickup_location",text="pickup_location",anchor=tk.CENTER)
            self.tree.heading("drop_location",text="drop_location",anchor=tk.CENTER)
            self.tree.heading("ride status",text="ride status",anchor=tk.CENTER)
            
            i=0
            for row in my_cursor:
                self.tree.insert('',i,text="",values=(row[0],row[8],row[1],row[2],row[3],row[4],row[6]))
                i=i+1
            
            scroll=ttk.Scrollbar(self.dri_av_frame,orient="horizontal")
            scroll.configure(command=self.tree.xview)
            self.tree.configure(xscrollcommand=scroll.set)
            scroll.pack(fill=X,side=BOTTOM)
            self.tree.pack()
               
            
            
            conn.commit()
            conn.close()
         except Exception as e:
            messagebox.showerror("error",e)
            
    #function to cancel booking request        
     def delete_data(self):
         try:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
            my_cursor=conn.cursor()
            selected_item=self.tree.selection()[0]    
            
            uid=self.tree.item(selected_item)['values'][0]
            
            
            # sel_data=(uid)
            my_cursor.execute("DELETE FROM booking WHERE id=%s",(uid,))
            conn.commit()
            self.tree.delete(selected_item)
            messagebox.showinfo("success","data deleted",parent=self.me)
         except Exception as e:
            messagebox.showerror("error",e)
            
    #selecting price from treeview table     
     def select_price(self):
        selected_item=self.tree.selection()[0]
        uid=self.tree.item(selected_item)['values'][1]
        self.showprice_entry.insert(0,uid)
        
   
#class for showing all booking records of customer   
class allbookingdata:
     def __init__(self,me):
        self.me=me
        self.me.title("booking page")
        self.me.geometry("1400x500+60+180")
        self.img= Image.open(r"B:\python2021\python projects\taxi booking\sushilbakcground.jpg")
        self.img=ImageTk.PhotoImage(self.img)
        
        img_lbl= Label(self.me,image=self.img)
        img_lbl.place(x=0,y=0,relwidth=1,relheight=1)
 
        #frame
        self.frame_allbookingdata1=Frame(self.me,bg='black')
        self.frame_allbookingdata1.place(x=0,y=0,height=500,width=1400)
        
        #calling treeview table
        self.view_table()
      
    #treeview table function  
     def view_table(self):
         try:
             #database connection code
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
            my_cursor=conn.cursor()
            
            #selecting all data by connecting three table for customer 
            my_cursor.execute("select * from customer_register c join booking b on c.sn=b.sn join driver d on b.driver_id=d.driver_id  where c.sn=%s ",(
                                              profile_value,
                                              
            ))
            
            self.tree=ttk.Treeview(self.frame_allbookingdata1)
            self.tree['show']='headings'
            self.tree.place(x=0,y=0,width=100,height=100)
           
            
            # assign column
            self.tree["columns"]=("id","payment through","date","time","pickup_location","drop_location","ride status","price","driver name","driver phone")
        
            
            
            #assign width and anchor of column
            self.tree.column("id",width=100,minwidth=100,anchor=tk.CENTER) 
            self.tree.column("payment through",width=200,minwidth=100,anchor=tk.CENTER) 
            self.tree.column("date",width=200,minwidth=200,anchor=tk.CENTER) 
            self.tree.column("time",width=100,minwidth=200,anchor=tk.CENTER) 
            self.tree.column("pickup_location",width=100,minwidth=100,anchor=tk.CENTER) 
            self.tree.column("drop_location",width=100,minwidth=150,anchor=tk.CENTER) 
            self.tree.column("ride status",width=200,minwidth=150,anchor=tk.CENTER) 
            self.tree.column("price",width=100,minwidth=150,anchor=tk.CENTER) 
            self.tree.column("driver name",width=200,minwidth=150,anchor=tk.CENTER) 
            self.tree.column("driver phone",width=200,minwidth=150,anchor=tk.CENTER) 
            
            
            # assing heading in table
            
            self.tree.heading("id",text="id",anchor=tk.CENTER)
            self.tree.heading("payment through",text="payment through",anchor=tk.CENTER)
            self.tree.heading("date",text="date",anchor=tk.CENTER)
            self.tree.heading("time",text="time",anchor=tk.CENTER)
            self.tree.heading("pickup_location",text="pickup_location",anchor=tk.CENTER)
            self.tree.heading("drop_location",text="drop_location",anchor=tk.CENTER)
            self.tree.heading("ride status",text="ride status",anchor=tk.CENTER)
            self.tree.heading("price",text="price",anchor=tk.CENTER)
            self.tree.heading("driver name",text="driver name",anchor=tk.CENTER)
            self.tree.heading("driver phone",text="driver phone",anchor=tk.CENTER)
            i=0
            #inserting data
            for row in my_cursor:
                self.tree.insert('',i,text="",values=(row[0],row[6],row[8],row[9],row[10],row[11],row[13],row[15],row[17],row[18]))
                i=i+1
            
            #scroll bar
            scroll=ttk.Scrollbar(self.frame_allbookingdata1,orient="horizontal")
            scroll.configure(command=self.tree.xview)
            self.tree.configure(xscrollcommand=scroll.set)
            scroll.pack(fill=X)
            self.tree.pack()

            conn.commit()
            conn.close()
         except Exception as e:
             print(e)
            
        
        
        
        
        


#admin page
class admin:
     def __init__(self,me):
        self.me=me
        self.me.title("booking page")
        self.me.geometry("1550x800+0+0")
#image
        self.img= Image.open(r"B:\python2021\python projects\taxi booking\sushilbakcground.jpg")
        self.img=ImageTk.PhotoImage(self.img)
        
        img_lbl= Label(self.me,image=self.img)
        img_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #frame
        self.admin_tbl_fm=Frame(self.me,bg="black")
        self.admin_tbl_fm.place(x=400,y=100,width=1050,height=650)
        
        time_lbl=Label(self.me,text="all pendings",font=("times new roman",15,"bold"),fg="red",bg="black")
        time_lbl.place(x=400,y=60)
        
        #back button
        back_btn1=Button(self.me,command=self.logout,text="logout",font=("times new roman",15,"bold"),fg="red",bg="black")
        back_btn1.place(x=1400,y=20)
     
     
        #frame
        self.admin_frame= Frame(self.me,bg="black")
        self.admin_frame.place(x=60,y=100,width=300,height=650)
        
        
        # text variable
        self.pickup=StringVar()
        self.drop= StringVar()
        self.date= StringVar()
        self.time= StringVar()
        self.bookid=StringVar()
        self.driveriiid=StringVar()
        
        # label

        date_lbl=Label(self.admin_frame,text="date",font=("times new roman",15,"bold"),bg="black",fg="white")
        date_lbl.place(x=50,y=50)
        
        
        time_lbl=Label(self.admin_frame,text="time",font=("times new roman",15,"bold"),fg="white",bg="black")
        time_lbl.place(x=50,y=150)
        
        pickup_lbl=Label(self.admin_frame,text="pickup location",font=("times new roman",15,"bold"),bg="black",fg="white")
        pickup_lbl.place(x=50,y=250)
        
        drop_lbl=Label(self.admin_frame,text="drop locationnnn",font=("times new roman",15,"bold"),fg="white",bg="black")
        drop_lbl.place(x=50,y=350)
        
        driverno_lbl=Label(self.admin_frame,text="driver number",font=("times new roman",15,"bold"),fg="white",bg="black")
        driverno_lbl.place(x=50,y=450)
  
        
        # entry
        self.date_entry= Entry(self.admin_frame,textvariabl=self.date,  font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.date_entry.place(x=50,y=100,width=200)
        
        self.time_entry= Entry(self.admin_frame,textvariabl=self.time,  font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.time_entry.place(x=50,y=200,width=200)
    
        self.pickup_entry= Entry(self.admin_frame,textvariabl=self.pickup, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.pickup_entry.place(x=50,y=300,width=200)
        
        self.drop_entry= Entry(self.admin_frame,textvariable=self.drop, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.drop_entry.place(x=50,y=400,width=200)
        
        self.driverno_entry= Entry(self.admin_frame,textvariable=self.driveriiid,font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.driverno_entry.place(x=50,y=500,width=200)
        
        # button
        confirm_btn= Button(self.admin_frame,command=self.update_for_driver,text="confirm",font=("times new roman",20,"bold"),fg="white",bg="black")
        confirm_btn.place(x=60,y=560,width=120,height=40)  
              
        showrow_btn= Button(self.admin_tbl_fm,command=self.row_from_admin,text="show row",font=("times new roman",20,"bold"),fg="white",bg="black")
        showrow_btn.place(x=30,y=300,width=200,height=40)   
             
        driadd_lbl= Button(self.admin_tbl_fm,command=self.add_driver,text="add driver",font=("times new roman",20,"bold"),fg="red",bg="black")
        driadd_lbl.place(x=30,y=600,width=200,height=40)        
    
        dravailable_lbl= Button(self.admin_tbl_fm,command=self.alldriver,text="all driver",font=("times new roman",20,"bold"),fg="red",bg="black")
        dravailable_lbl.place(x=250,y=600,width=200,height=40)   
             
        dravailable_lbl= Button(self.admin_tbl_fm,command=self.av_driver_win,text="available driver",font=("times new roman",20,"bold"),fg="red",bg="black")
        dravailable_lbl.place(x=500,y=600,width=200,height=40)
                
        dravailable_lbl= Button(self.admin_tbl_fm,command=self.all_trips,text="all trips",font=("times new roman",20,"bold"),fg="red",bg="black")
        dravailable_lbl.place(x=750,y=600,width=200,height=40)
                
        

    #table to show pending request of customer  
     def admin_table(self):
            self.tree_admin=ttk.Treeview(self.admin_tbl_fm)
            
            self.tree_admin['show']='headings'
           
            
            # assign column
            self.tree_admin["columns"]=("id","name","address","phone","email","pay_by","date","time","pickup","drop","status")
            
            
            #assign width and anchor
            self.tree_admin.column("id",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_admin.column("name",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_admin.column("address",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_admin.column("phone",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_admin.column("email",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_admin.column("pay_by",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_admin.column("date",width=200,minwidth=10,anchor=tk.CENTER) 
            self.tree_admin.column("time",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_admin.column("pickup",width=200,minwidth=10,anchor=tk.CENTER) 
            self.tree_admin.column("drop",width=200,minwidth=15,anchor=tk.CENTER) 
            self.tree_admin.column("status",width=200,minwidth=15,anchor=tk.CENTER) 
            
            # assing heading
            
            self.tree_admin.heading("id",text="id",anchor=tk.CENTER)
            self.tree_admin.heading("name",text="name",anchor=tk.CENTER)
            self.tree_admin.heading("address",text="address",anchor=tk.CENTER)
            self.tree_admin.heading("phone",text="phone",anchor=tk.CENTER)
            self.tree_admin.heading("email",text="email",anchor=tk.CENTER)
            self.tree_admin.heading("pay_by",text="pay_by",anchor=tk.CENTER)
            self.tree_admin.heading("date",text="date",anchor=tk.CENTER)
            self.tree_admin.heading("time",text="time",anchor=tk.CENTER)
            self.tree_admin.heading("pickup",text="pickup",anchor=tk.CENTER)
            self.tree_admin.heading("drop",text="drop",anchor=tk.CENTER)
            self.tree_admin.heading("status",text="status",anchor=tk.CENTER)
            
            scroll_admin=ttk.Scrollbar(self.admin_tbl_fm,orient="horizontal")
            scroll_admin.configure(command=self.tree_admin.xview)
            self.tree_admin.configure(xscrollcommand=scroll_admin.set)
            scroll_admin.pack(fill=X)
            self.tree_admin.pack()
            #calling function to insert data in table
            self.insert_admintable()
            
            
#function to enter data in admin main page
     def insert_admintable(self):
         try:
            self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
            self.my_cursor=self.conn.cursor()
            
            #query to select pending request
            self.my_cursor.execute("select * from customer_register C join booking B ON C.sn=B.sn where B.ride_status='pending'")
            
            i=0
            for row in self.my_cursor:
                self.tree_admin.insert('',i,text="",values=(row[7],row[1],row[2],row[3],row[4],row[6],row[8],row[9],row[10],row[11],row[13]))
                i=i+1
            self.conn.commit()
            self.conn.close() 
        #exception handling
         except Exception as e:
            messagebox.showerror("error",e) 
            
            
  
    #selecting row from admin main table
     def row_from_admin(self):
         try:
            self.reset_val()
            selected_item= self.tree_admin.selection()[0]            
            one=self.tree_admin.item(selected_item)['values'][6]
            two=self.tree_admin.item(selected_item)['values'][7]
            three=self.tree_admin.item(selected_item)['values'][8]
            four=self.tree_admin.item(selected_item)['values'][9]
            five=self.tree_admin.item(selected_item)['values'][0]
            
            #insert the selected data from row of table into entry box
            self.date_entry.insert(0,one)
            self.time_entry.insert(0,two)
            self.pickup_entry.insert(0,three)
            self.drop_entry.insert(0,four)
            self.bookid=five
            
         except Exception as e:
            messagebox.showerror("error","select row")
            
    #function to reset entry box
     def reset_val(self):
            for widget in self.admin_frame.winfo_children():
                if isinstance(widget,Entry):
                    widget.delete(0,'end')

            
    # function to change the status of driver and booking
     def update_for_driver(self):
         try:
        
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
            my_cursor=conn.cursor()
            
            #booking status changed to accepted by admin here
            my_cursor.execute("update booking set ride_status='accepted', driver_id=%s where id=%s",(self.driverno_entry.get(),self.bookid))
            
            #here driver status changed to unavailable
            my_cursor.execute("update driver set status='unavailable' where driver_id=%s",(self.driverno_entry.get(),))
            conn.commit()
            messagebox.showinfo("success","data entered")
            selected_item=self.tree_admin.selection()[0]
            self.tree_admin.delete(selected_item)
            
            #reseting entry box after confirming
            self.reset_val()
         
         except Exception as e:
            messagebox.showerror("error","insert into the fields")

#function to enter add driver window     
     def add_driver(self):
         self.adddriver_win=Toplevel(self.me)
         self.adddriver_win1=addriver(self.adddriver_win)

#function to enter in window which show available driver         
     def av_driver_win(self):
         self.av_driver=Toplevel(self.me)
         self.av_driver=availabledriver(self.av_driver)
        
#window for all trips for admin       
     def all_trips(self):
        self.trip_win=Toplevel(self.me)
        
        self.trip_win.title("booking page")
        self.trip_win.geometry("1550x800+0+0")
 
        
        back_btn= Button(self.trip_win,command=self.trip_win.destroy,text="back",font=("times new roman",20,"bold"),fg="white",bg="black")
        back_btn.place(x=20,y=750,width=120,height=40)  
        
        self.all_trip_tree=ttk.Treeview(self.trip_win)
            
        self.all_trip_tree['show']='headings'
           
            
            # assign column
        self.all_trip_tree["columns"]=("status","id","customer name","address","phone","email","pay_by","date","time","pickup","drop","asigned driver","driver phone")
            
            
            #assign width and anchor
        self.all_trip_tree.column("status",width=200,minwidth=15,anchor=tk.CENTER) 
        
        self.all_trip_tree.column("id",width=100,minwidth=10,anchor=tk.CENTER) 
        self.all_trip_tree.column("customer name",width=100,minwidth=10,anchor=tk.CENTER) 
        self.all_trip_tree.column("address",width=100,minwidth=10,anchor=tk.CENTER) 
        self.all_trip_tree.column("phone",width=100,minwidth=10,anchor=tk.CENTER) 
        self.all_trip_tree.column("email",width=100,minwidth=10,anchor=tk.CENTER) 
        self.all_trip_tree.column("pay_by",width=100,minwidth=10,anchor=tk.CENTER) 
        self.all_trip_tree.column("date",width=200,minwidth=10,anchor=tk.CENTER) 
        self.all_trip_tree.column("time",width=100,minwidth=10,anchor=tk.CENTER) 
        self.all_trip_tree.column("pickup",width=200,minwidth=10,anchor=tk.CENTER) 
        self.all_trip_tree.column("drop",width=200,minwidth=15,anchor=tk.CENTER) 
        self.all_trip_tree.column("asigned driver",width=200,minwidth=15,anchor=tk.CENTER) 
        self.all_trip_tree.column("driver phone",width=200,minwidth=15,anchor=tk.CENTER) 
        
            
            # assing heading
            
        self.all_trip_tree.heading("status",text="status",anchor=tk.CENTER)
        self.all_trip_tree.heading("id",text="id",anchor=tk.CENTER)
        self.all_trip_tree.heading("customer name",text="name",anchor=tk.CENTER)
        self.all_trip_tree.heading("address",text="address",anchor=tk.CENTER)
        self.all_trip_tree.heading("phone",text="phone",anchor=tk.CENTER)
        self.all_trip_tree.heading("email",text="email",anchor=tk.CENTER)
        self.all_trip_tree.heading("pay_by",text="pay_by",anchor=tk.CENTER)
        self.all_trip_tree.heading("date",text="date",anchor=tk.CENTER)
        self.all_trip_tree.heading("time",text="time",anchor=tk.CENTER)
        self.all_trip_tree.heading("pickup",text="pickup",anchor=tk.CENTER)
        self.all_trip_tree.heading("drop",text="drop",anchor=tk.CENTER)
        self.all_trip_tree.heading("asigned driver",text="asigned driver",anchor=tk.CENTER)
        self.all_trip_tree.heading("driver phone",text="driver phone",anchor=tk.CENTER)
        
         #scroll bar   
        scroll_admin=ttk.Scrollbar(self.trip_win,orient="horizontal")
        scroll_admin.configure(command=self.all_trip_tree.xview)
        self.all_trip_tree.configure(xscrollcommand=scroll_admin.set)
        scroll_admin.pack(fill=X)
        self.all_trip_tree.pack()
        self.insert_alltrip()   
    
    #showing all data in alltrip window in table
     def insert_alltrip(self):
         try:
            self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
            self.my_cursor=self.conn.cursor()
            
            #select request which are not pending
            self.my_cursor.execute("select * from customer_register C join booking B ON C.sn=B.sn join driver D on D.driver_id=B.driver_id where B.ride_status !='pending'")
            
            #insert
            i=0
            for row in self.my_cursor:
                self.all_trip_tree.insert('',i,text="",values=(row[13],row[7],row[1],row[2],row[3],row[4],row[6],row[8],row[9],row[10],row[11],row[17],row[18]))
                i=i+1
            self.conn.commit()
            self.conn.close()  
        
         except Exception as e:
            messagebox.showerror("error",e)
#logout function
     def logout(self):
         msg_box = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',icon='warning')
         if msg_box=='yes':
             self.application=Login_Page(me)       
 
#alldriver window by which admin can see all driver information
     def alldriver(self):
         self.win= Toplevel(self.me)
         
         self.win.title("booking page")
         self.win.geometry("1050x650+400+100")
        #image
         self.img_another= Image.open(r"B:\python2021\python projects\taxi booking\sushilbakcground.jpg")
         self.img_another=ImageTk.PhotoImage(self.img_another)
        
         img_lbl= Label(self.win,image=self.img_another)
         img_lbl.place(x=0,y=0,relwidth=1,relheight=1)
         #frame
         self.dri_all_frame= Frame(self.win,bg="black")
         self.dri_all_frame.place(x=170,y=50,width=800,height=540)
         self.alldriver_table()
       
       
    #alldriver window table
     def alldriver_table(self):
         try:
             conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from driver")
                

             self.tree_alldriver=ttk.Treeview(self.dri_all_frame)
                
             self.tree_alldriver['show']='headings'
            
                
                # assign column
             self.tree_alldriver["columns"]=("id","name","phone","address","email","taxi number","license number","status")
                
                
                #assign width and anchor
             self.tree_alldriver.column("id",width=100,minwidth=10,anchor=tk.CENTER) 
             self.tree_alldriver.column("name",width=100,minwidth=10,anchor=tk.CENTER) 
             self.tree_alldriver.column("phone",width=100,minwidth=10,anchor=tk.CENTER) 
             self.tree_alldriver.column("address",width=100,minwidth=10,anchor=tk.CENTER) 
             self.tree_alldriver.column("email",width=100,minwidth=10,anchor=tk.CENTER) 
             self.tree_alldriver.column("taxi number",width=100,minwidth=10,anchor=tk.CENTER) 
             self.tree_alldriver.column("license number",width=200,minwidth=10,anchor=tk.CENTER) 
             self.tree_alldriver.column("status",width=100,minwidth=10,anchor=tk.CENTER) 
                
                
                # assing heading
                
             self.tree_alldriver.heading("id",text="id",anchor=tk.CENTER)
             self.tree_alldriver.heading("name",text="name",anchor=tk.CENTER)
             self.tree_alldriver.heading("phone",text="phone",anchor=tk.CENTER)
             self.tree_alldriver.heading("address",text="address",anchor=tk.CENTER)
             self.tree_alldriver.heading("email",text="email",anchor=tk.CENTER)
             self.tree_alldriver.heading("taxi number",text="taxi number",anchor=tk.CENTER)
             self.tree_alldriver.heading("license number",text="license number",anchor=tk.CENTER)
             self.tree_alldriver.heading("status",text="status",anchor=tk.CENTER)
        #insert 
             i=0
             for row in my_cursor:
                self.tree_alldriver.insert('',i,text="",values=(row[0],row[1],row[2],row[3],row[4],row[6],row[7],row[8]))
                i=i+1
                
             #scroll bar   
             scroll_admin=ttk.Scrollbar(self.dri_all_frame,orient="horizontal")
             scroll_admin.configure(command=self.tree_alldriver.xview)
             self.tree_alldriver.configure(xscrollcommand=scroll_admin.set)
             scroll_admin.pack(fill=X)
             self.tree_alldriver.pack()
                
             conn.commit()
             conn.close()  
#exception
         except Exception as e:
            messagebox.showerror("error",e) 


#admin can add driver here
class addriver:
    def __init__(self,me):
        self.me=me
        self.me.title("booking page")
        self.me.geometry("1050x650+400+100")
        self.img= Image.open(r"B:\python2021\python projects\taxi booking\sushilbakcground.jpg")
        self.img=ImageTk.PhotoImage(self.img)
        
        img_lbl= Label(self.me,image=self.img)
        img_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
  
        self.dri_reg_frame= Frame(self.me,bg="black")
        self.dri_reg_frame.place(x=170,y=50,width=800,height=540)
        
        
        # text variable
        self.name=StringVar()
        self.phone= StringVar()
        self.address= StringVar()
        self.email= StringVar()
        self.psd= StringVar()
        self.taxno= StringVar()
        self.license= StringVar()
        self.status="available"

        
        # label
        booktxt=Label(self.dri_reg_frame,text="add driver",font=("times new roman",20,"bold"),bg="black",fg="red")
        booktxt.place(x=10,y=10)
        
        drname_lbl=Label(self.dri_reg_frame,text="driver name",font=("times new roman",15,"bold"),bg="black",fg="white")
        drname_lbl.place(x=20,y=100)
        
        
        draddress_lbl=Label(self.dri_reg_frame,text="address",font=("times new roman",15,"bold"),fg="white",bg="black")
        draddress_lbl.place(x=390,y=100)
        
        drphone_lbl=Label(self.dri_reg_frame,text="phone",font=("times new roman",15,"bold"),bg="black",fg="white")
        drphone_lbl.place(x=20,y=150)
        
        dremail_lbl=Label(self.dri_reg_frame,text="email",font=("times new roman",15,"bold"),fg="white",bg="black")
        dremail_lbl.place(x=390,y=150)

        drpsd_lbl=Label(self.dri_reg_frame,text="password",font=("times new roman",15,"bold"),bg="black",fg="white")
        drpsd_lbl.place(x=20,y=200)
        
        drlic_lbl=Label(self.dri_reg_frame,text="licence number",font=("times new roman",15,"bold"),fg="white",bg="black")
        drlic_lbl.place(x=390,y=200)
        
        drtaxno_lbl=Label(self.dri_reg_frame,text="taxi number",font=("times new roman",15,"bold"),bg="black",fg="white")
        drtaxno_lbl.place(x=20,y=250)
        
 
    
        # entry
        drname_lbl= Entry(self.dri_reg_frame,textvariable=self.name, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        drname_lbl.place(x=150,y=100,width=200)
        
        draddress_entry= Entry(self.dri_reg_frame, textvariable=self.address, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        draddress_entry.place(x=550,y=100,width=200)
    
        drphone_entry= Entry(self.dri_reg_frame,textvariable=self.phone, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        drphone_entry.place(x=150,y=150,width=200)
        
        dremail_entry= Entry(self.dri_reg_frame,textvariable=self.email, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        dremail_entry.place(x=550,y=150,width=200)
        
        drpsd_entry= Entry(self.dri_reg_frame,textvariable=self.psd, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        drpsd_entry.place(x=150,y=200,width=200)
        
        drlic_entry= Entry(self.dri_reg_frame,textvariable=self.license, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        drlic_entry.place(x=550,y=200,width=200)
        
        drtaxno_entry= Entry(self.dri_reg_frame,textvariable=self.taxno, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        drtaxno_entry.place(x=150,y=250,width=200)
        
        # button
        confirm_btn= Button(self.dri_reg_frame,text="Add",command=self.booking_val,font=("times new roman",20,"bold"),fg="white",bg="black")
        confirm_btn.place(x=350,y=350,width=120,height=40)
      
    #driver registration  
    def booking_val(self):
       #validation
        if self.name.get()=="" or self.phone.get()=="" or self.address.get()=="" or self.email.get()=="" or self.psd.get()=="" or self.taxno.get()=="" or self.license.get()=="":
            messagebox.showerror("error","all field are required",parent=self.me)
        else:
            try:
                #sql connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
                my_cursor=conn.cursor()
                #insert into database
                my_cursor.execute("insert into driver (name,phone,address,email,password,taxino,license,status) values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                self.name.get(),
                                self.phone.get(),
                                self.address.get(),
                                self.email.get(),
                                self.psd.get(),
                                self.taxno.get(),
                                self.license.get(),
                                self.status
                                
                                
                                
                ))
                
                conn.commit()
                conn.close()
                messagebox.showinfo("success","successfully added",parent=self.me)  
                self.reset_val()  
            except Exception as e:
                messagebox.showerror("error",e)       
  
  #reset entry boxes
    def reset_val(self):
            for widget in self.dri_reg_frame.winfo_children():
                if isinstance(widget,Entry):
                    widget.delete(0,'end')
                    

#class for available driver window 
class availabledriver:
    def __init__(self,me):
        self.me=me
        self.me.title("booking page")
        self.me.geometry("1050x650+400+100")
        
        self.img= Image.open(r"B:\python2021\python projects\taxi booking\sushilbakcground.jpg")
        self.img=ImageTk.PhotoImage(self.img)
        
        img_lbl= Label(self.me,image=self.img)
        img_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        self.dri_av_frame= Frame(self.me,bg="black")
        self.dri_av_frame.place(x=170,y=50,width=800,height=540)
        
        self.admin_table()
       
       
  
#showing driver whose status is available     
    def admin_table(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from driver where status='available'")
            
            self.tree_driver=ttk.Treeview(self.dri_av_frame)
            
            self.tree_driver['show']='headings'
           
            
            # assign column
            self.tree_driver["columns"]=("id","name","phone","address","email","taxi number","license number","status")
            
            
            #assign width and anchor
            self.tree_driver.column("id",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("name",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("phone",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("address",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("email",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("taxi number",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("license number",width=200,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("status",width=100,minwidth=10,anchor=tk.CENTER) 
            
            
            # assing heading
            
            self.tree_driver.heading("id",text="id",anchor=tk.CENTER)
            self.tree_driver.heading("name",text="name",anchor=tk.CENTER)
            self.tree_driver.heading("phone",text="phone",anchor=tk.CENTER)
            self.tree_driver.heading("address",text="address",anchor=tk.CENTER)
            self.tree_driver.heading("email",text="email",anchor=tk.CENTER)
            self.tree_driver.heading("taxi number",text="taxi number",anchor=tk.CENTER)
            self.tree_driver.heading("license number",text="license number",anchor=tk.CENTER)
            self.tree_driver.heading("status",text="status",anchor=tk.CENTER)
    
            i=0
            for row in my_cursor:
                self.tree_driver.insert('',i,text="",values=(row[0],row[1],row[2],row[3],row[4],row[6],row[7],row[8]))
                i=i+1
            
            #scroll bar
            scroll_admin=ttk.Scrollbar(self.dri_av_frame,orient="horizontal")
            scroll_admin.configure(command=self.tree_driver.xview)
            self.tree_driver.configure(xscrollcommand=scroll_admin.set)
            scroll_admin.pack(fill=X)
            self.tree_driver.pack()
            
            conn.commit()
            conn.close() 
        
        except Exception as e:
            messagebox.showerror("error",e)  





 
 
#driver page
class driver_window:
    def __init__(self,me):
        self.me=me
        self.me.title("booking page")
        self.me.geometry("1550x800+0+0")
        
        self.img= Image.open(r"B:\python2021\python projects\taxi booking\sushilbakcground.jpg")
        self.img=ImageTk.PhotoImage(self.img)
        
        img_lbl= Label(self.me,image=self.img)
        img_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
       # Frame
        self.frameone=Frame(self.me,bg="black")
        self.frameone.place(x=400,y=100,width=850,height=250)
        
        self.frametwo=Frame(self.me,bg="black")
        self.frametwo.place(x=400,y=400,width=850,height=350)
        
        #button
        self.accpt_btn= Button(self.me,command=self.row_from_drivertable,text="accept request",font=("times new roman",15,"bold"),fg="white",bg="black")
        self.accpt_btn.place(x=550,y=355,width=200)
        
        self.complete_btn= Button(self.me,text="payment and complete",command=self.reset_val,font=("times new roman",15,"bold"),fg="white",bg="black")
        self.complete_btn.place(x=770,y=355,width=200)
        
        self.complete_btn= Button(self.me,text="all your trips",command=self.allyourtrip,font=("times new roman",15,"bold"),fg="white",bg="black")
        self.complete_btn.place(x=1300,y=750,width=200)
        
        #label
        
        drivernm_lbl=Label(self.me,text="welcom:",font=("times new roman",15,"bold"),bg="black",fg="white")
        drivernm_lbl.place(x=50,y=50)
        
        drivernm1_lbl=Label(self.me,text=driver_name,font=("times new roman",15,"bold"),bg="black",fg="white")
        drivernm1_lbl.place(x=150,y=50)
        
        #calling table which show customer request
        self.admin_table()
        self.insert_into_admintable()
        
        
        date_lbl=Label(self.frametwo,text="today date",font=("times new roman",15,"bold"),bg="black",fg="white")
        date_lbl.place(x=10,y=20)
        
        self.cst_name=Label(self.frametwo,text="customer name",font=("times new roman",15,"bold"),bg="black",fg="white")
        self.cst_name.place(x=400,y=20)
        
        phone_lbl=Label(self.frametwo,text="phon no",font=("times new roman",15,"bold"),bg="black",fg="white")
        phone_lbl.place(x=10,y=90)
        
        pay_lbl=Label(self.frametwo,text="payment by",font=("times new roman",15,"bold"),bg="black",fg="white")
        pay_lbl.place(x=400,y=90)
        
        pickup_lbl=Label(self.frametwo,text="pickup location",font=("times new roman",15,"bold"),bg="black",fg="white")
        pickup_lbl.place(x=10,y=160)
        
        drop_lbl=Label(self.frametwo,text="drop location",font=("times new roman",15,"bold"),bg="black",fg="white")
        drop_lbl.place(x=400,y=160)
        
        price_lbl=Label(self.frametwo,text="price",font=("times new roman",15,"bold"),bg="black",fg="white")
        price_lbl.place(x=10,y=230)
        
        
        #labels
        self.date_entry= Label(self.frametwo, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.date_entry.place(x=150,y=20,width=200)
        
       
        self.cstname_entry= Label(self.frametwo, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.cstname_entry.place(x=550,y=20,width=200)
        

        self.phone_entry= Label(self.frametwo, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.phone_entry.place(x=150,y=90,width=200)
  
        
        self.pay_entry= Label(self.frametwo, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.pay_entry.place(x=550,y=90,width=200)
        
    
        self.pickup_entry= Label(self.frametwo, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.pickup_entry.place(x=150,y=160,width=200)
    
        self.drop_entry= Label(self.frametwo, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.drop_entry.place(x=550,y=160,width=200)
        
        
        self.price_entry= Label(self.frametwo, font=("times new roman",15,"bold"),bg="white",fg="black",borderwidth=4)
        self.price_entry.place(x=150,y=230,width=200)
        
        # button
        back_btn2=Button(self.me,command=self.logout1,text="logout",font=("times new roman",15,"bold"),fg="red",bg="black")
        back_btn2.place(x=1400,y=20)
        
    
    #table to show recent request of customer in driver page
    def admin_table(self):

            
            self.tree_driver=ttk.Treeview(self.frameone)
            
            self.tree_driver['show']='headings'
           
            
            # assign column
            self.tree_driver["columns"]=("id","date","time","name","address","phone","payment method","pickup location","drop location","price","status")
            
            
            #assign width and anchor
            self.tree_driver.column("id",width=50,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("date",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("time",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("name",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("address",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("phone",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("payment method",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("pickup location",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("drop location",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("price",width=100,minwidth=10,anchor=tk.CENTER) 
            self.tree_driver.column("status",width=100,minwidth=10,anchor=tk.CENTER) 
            
            
            
            
            # assing heading
            
            self.tree_driver.heading("id",text="id",anchor=tk.CENTER)
            self.tree_driver.heading("date",text="date",anchor=tk.CENTER)
            self.tree_driver.heading("time",text="time",anchor=tk.CENTER)
            self.tree_driver.heading("name",text="name",anchor=tk.CENTER)
            self.tree_driver.heading("address",text="address",anchor=tk.CENTER)
            self.tree_driver.heading("phone",text="phone",anchor=tk.CENTER)
            self.tree_driver.heading("payment method",text="payment method",anchor=tk.CENTER)
            self.tree_driver.heading("pickup location",text="pickup location",anchor=tk.CENTER)
            self.tree_driver.heading("drop location",text="drop location",anchor=tk.CENTER)
            self.tree_driver.heading("price",text="price",anchor=tk.CENTER)
            self.tree_driver.heading("status",text="status",anchor=tk.CENTER)

            
            scroll_admin=ttk.Scrollbar(self.frameone,orient="horizontal")
            scroll_admin.configure(command=self.tree_driver.xview)
            self.tree_driver.configure(xscrollcommand=scroll_admin.set)
            scroll_admin.pack(fill=X)
            self.tree_driver.pack()
            
             
    #insert into table of driver page
    def insert_into_admintable(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
            my_cursor=conn.cursor()
            #query execution
            my_cursor.execute("select * from customer_register c join booking b on c.sn=b.sn join driver d on b.driver_id=d.driver_id where (b.ride_status='accepted' or b.ride_status='on the way') and d.driver_id=%s",(driver_id,))
            
            
            i=1
            self.tree_driver.delete(*self.tree_driver.get_children())
            for row in my_cursor:
                self.tree_driver.insert('',i,text="",values=(row[7],row[8],row[9],row[1],row[2],row[3],row[6],row[10],row[11],row[15],row[13]))
                i=i+1
            conn.commit()
            conn.close() 
        
        except Exception as e:
            messagebox.showerror("error",e)
        
    
    
    #selecting row from driver page table
    def row_from_drivertable(self):
        try:
         #row selected
         selected_item= self.tree_driver.selection()[0]
         self.one=self.tree_driver.item(selected_item)['values'][0]
         #databse connection
         conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
         my_cursor=conn.cursor()
         #changing booking status into on the way 
         my_cursor.execute("update booking set ride_status='on the way' where id=%s",(self.one,))
         
         #assigning data from row into variable
         two=self.tree_driver.item(selected_item)['values'][1]
         threesome=self.tree_driver.item(selected_item)['values'][3]
         four=self.tree_driver.item(selected_item)['values'][5]
         five=self.tree_driver.item(selected_item)['values'][6]
         six=self.tree_driver.item(selected_item)['values'][7]
         seven=self.tree_driver.item(selected_item)['values'][8]
         eight=self.tree_driver.item(selected_item)['values'][9]
         
         #assignin variable data into entry box
         self.date_entry.config(text=two)
         self.cstname_entry.config(text=threesome)
         self.phone_entry.config(text=four)
         self.pay_entry.config(text=five)
         self.pickup_entry.config(text=six)
         self.drop_entry.config(text=seven)
         self.price_entry.config(text=eight)
         self.insert_into_admintable()
         
         conn.commit()
         conn.close()
        
        except Exception as e:
            messagebox.showerror("error","please select row")
            
#function to change driver and booking status    
    def reset_val(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
            my_cursor=conn.cursor()
            # booking stattus changed to completed
            my_cursor.execute("update booking set ride_status='completed' where id=%s",(self.one,))
            #driver status change to available
            my_cursor.execute("update driver set status='available' where driver_id=%s",(driver_id,))
            
            #reseting entry box 
            self.date_entry.config(text="")
        
            self.cstname_entry.config(text="")
            self.phone_entry.config(text="")
            self.pay_entry.config(text="")
            self.pickup_entry.config(text="")
            self.drop_entry.config(text="")
            self.price_entry.config(text="")
            
            
            #inserting updated data into driver tables
            self.insert_into_admintable()
            
            
            
        
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("error",e)

#function to show all history records of driver trips
    def allyourtrip(self):
        self.your_trip_tree=Toplevel(self.me)
        
        self.your_trip_tree.title("booking page")
        self.your_trip_tree.geometry("1550x800+0+0")
 
        
        back_btn= Button(self.your_trip_tree,command=self.your_trip_tree.destroy,text="back",font=("times new roman",20,"bold"),fg="white",bg="black")
        back_btn.place(x=20,y=750,width=120,height=40) 
        
        self.tree_driver12=ttk.Treeview(self.your_trip_tree)
        self.tree_driver12['show']='headings'
           
            
            # assign column
        self.tree_driver12["columns"]=("id","date","time","name","address","phone","payment method","pickup location","drop location","price","status")
            
            
            #assign width and anchor
        self.tree_driver12.column("id",width=50,minwidth=10,anchor=tk.CENTER) 
        self.tree_driver12.column("date",width=100,minwidth=10,anchor=tk.CENTER) 
        self.tree_driver12.column("time",width=100,minwidth=10,anchor=tk.CENTER) 
        self.tree_driver12.column("name",width=100,minwidth=10,anchor=tk.CENTER) 
        self.tree_driver12.column("address",width=100,minwidth=10,anchor=tk.CENTER) 
        self.tree_driver12.column("phone",width=100,minwidth=10,anchor=tk.CENTER) 
        self.tree_driver12.column("payment method",width=100,minwidth=10,anchor=tk.CENTER) 
        self.tree_driver12.column("pickup location",width=100,minwidth=10,anchor=tk.CENTER) 
        self.tree_driver12.column("drop location",width=100,minwidth=10,anchor=tk.CENTER) 
        self.tree_driver12.column("price",width=100,minwidth=10,anchor=tk.CENTER) 
        self.tree_driver12.column("status",width=100,minwidth=10,anchor=tk.CENTER) 
            
            
            
            
            # assing heading
            
        self.tree_driver12.heading("id",text="id",anchor=tk.CENTER)
        self.tree_driver12.heading("date",text="date",anchor=tk.CENTER)
        self.tree_driver12.heading("time",text="time",anchor=tk.CENTER)
        self.tree_driver12.heading("name",text="name",anchor=tk.CENTER)
        self.tree_driver12.heading("address",text="address",anchor=tk.CENTER)
        self.tree_driver12.heading("phone",text="phone",anchor=tk.CENTER)
        self.tree_driver12.heading("payment method",text="payment method",anchor=tk.CENTER)
        self.tree_driver12.heading("pickup location",text="pickup location",anchor=tk.CENTER)
        self.tree_driver12.heading("drop location",text="drop location",anchor=tk.CENTER)
        self.tree_driver12.heading("price",text="price",anchor=tk.CENTER)
        self.tree_driver12.heading("status",text="status",anchor=tk.CENTER)

            
        scroll_admin=ttk.Scrollbar(self.your_trip_tree,orient="horizontal")
        scroll_admin.configure(command=self.tree_driver12.xview)
        self.tree_driver12.configure(xscrollcommand=scroll_admin.set)
        scroll_admin.pack(fill=X)
        self.tree_driver12.pack()
            
        

        conn=mysql.connector.connect(host="localhost",user="root",password="",database="taxibooking")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer_register c join booking b on c.sn=b.sn join driver d on b.driver_id=d.driver_id where d.driver_id=%s",(driver_id,))
        i=1
        self.tree_driver12.delete(*self.tree_driver12.get_children())
        
        #insert
        for row in my_cursor:
            self.tree_driver12.insert('',i,text="",values=(row[7],row[8],row[9],row[1],row[2],row[3],row[6],row[10],row[11],row[15],row[13]))
            i=i+1
        conn.commit()
        conn.close() 
        
        
    #logout function
    def logout1(self):
         msg_box = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',icon='warning')
         if msg_box=='yes':
             self.application=Login_Page(me)  
                

       
        
if __name__=="__main__":
    me=Tk()
    form=Login_Page(me)
    me.mainloop()