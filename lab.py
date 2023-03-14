from tkinter import *
from tkinter import messagebox
class Transaction:
    global acc_no_entry
    global name_entry
    global id_entry
    global balance_entry
    global mobileno_entry
    def __init__(self,master):
        self.accounts={}
        self.master=master
        self.current_balance=0
        width= self.master.winfo_screenwidth()
        height= self.master.winfo_screenheight()
        self.master.geometry('%dx%d' %(width,height))
        self.master['background'] = '#98F'
        
    def login(self):
        name=Label(text="Customer Name")
        user_name=Entry(self.master)
        password=Label(text="Password")
        user_password=Entry(self.master,show="*")
        name.grid(row=0,column=0,padx=20,pady=10)
        password.grid(row=1,column=0,padx=20,pady=10)
        user_name.grid(row=0,column=1,padx=20,pady=10)
        user_password.grid(row=1,column=1,padx=20,pady=10)
        submit=Button(self.master,text="Login",bg = "green",command=self.main_page)
        submit.grid(row=2,column=4) 
        self.master.mainloop() 
            
    def main_page(self):
        self.master1=Toplevel(self.master)
        self.master1.geometry('500x500')
        self.master1['background'] = '#18F'
        width= self.master1.winfo_screenwidth()
        height= self.master1.winfo_screenheight()
        self.master1.geometry('%dx%d' %(width,height))
        self.master1.title("Main Window")
        create_Account=Button(self.master1,text="Create Account",bg = "yellow",command=self.creating_account)
        Withdraw_Amount=Button(self.master1,text="Withdraw Amount",bg = "yellow",command=self.withdrawl)
        Deposit_Amount=Button(self.master1,text="Deposit Amount",bg = "yellow",command=self.deposit)
        Transfer_Amount=Button(self.master1,text="Transfer Amount",bg = "yellow",command=self.transfer)
        Account_Details=Button(self.master1,text="Account Details",bg = "yellow",command=self.details)
        create_Account.grid(row=0,column=0,pady=50,padx=70)
        Withdraw_Amount.grid(row=0,column=1,pady=50)
        Transfer_Amount.grid(row=1,column=0,pady=50,padx=70)
        Deposit_Amount.grid(row=1,column=1)
        Account_Details.grid(row=2,column=0,pady=40)
        self.master1.mainloop()

    def creating_account(self):
        self.v = StringVar()
        self.master2=Toplevel(self.master)
        self.master2.geometry('500x500')
        self.master2['background'] = '#58F'
        width= self.master2.winfo_screenwidth()
        height= self.master2.winfo_screenheight()
        self.master2.geometry('%dx%d' %(width,height))
        self.master2.title("Create Account Window")
        self.name=Label(self.master2,text="Customer Name:")
        self.id=Label(self.master2,text="Customer ID:")
        self.mno=Label(self.master2,text="Customer Mobile No:")
        self.acc_no=Label(self.master2,text="Account No:")
        self.name_entry=Entry(self.master2,textvariable=self.v)
        self.id_entry=Entry(self.master2)
        self.mobileno_entry=Entry(self.master2)
        self.acc_no_entry=Entry(self.master2)
        self.name_entry.grid(row=0,column=1,padx=10,pady=5)
        self.id_entry.grid(row=1,column=1,padx=10,pady=5)
        self.mobileno_entry.grid(row=2,column=1,padx=10,pady=5)
        self.acc_no_entry.grid(row=3,column=1,padx=10,pady=5)
        self.name.grid(row=0,column=0,padx=10,pady=5)
        self.id.grid(row=1,column=0,padx=10,pady=5)
        self.mno.grid(row=2,column=0,padx=10,pady=5)
        self.acc_no.grid(row=3,column=0,padx=10,pady=5)
        submit=Button(self.master2,text="Submit",bg = "yellow",command=lambda:messagebox.showinfo("information","Account Created Successfully"))
        submit.grid(row=5,column=1,padx=10,pady=10)
        self.master2.mainloop()
        
    def calculate_withdrawl(self, acc_no_entry, amount_entry):
        acc_no_entry = acc_no_entry.get()
        amount_entry = amount_entry.get()
        self.accounts['acc_no_entry'] = acc_no_entry
        self.accounts['amount_entry'] = amount_entry
        if float(self.accounts['amount_entry']) > self.current_balance:
            messagebox.showerror("info","no balance")
            print("Insufficient balance!")
        else:
            self.current_balance -= float(self.accounts['amount_entry'])
            print(f"{float(self.accounts['amount_entry'])} withdrawn from account {self.accounts['acc_no_entry']}. New balance: {self.current_balance}")
            messagebox.showinfo("Information","Amount Withdrawl Successfully")
    def withdrawl(self):
        self.master3=Toplevel(self.master)
        self.master3.geometry('500x500')
        self.master3['background'] = '#58F'
        self.master3.title("Amount Withdrawl Window")
        self.master3.resizable(False,False)
        width= self.master3.winfo_screenwidth()
        height= self.master3.winfo_screenheight()
        self.master3.geometry('%dx%d' %(width,height))
        acc_no_label=Label(self.master3,text="Enter Your Account No:")
        amount_label=Label(self.master3,text="Enter Your Amount:")
        acc_no_label.grid(row=0,column=0,padx=50,pady=10)
        amount_label.grid(row=1,column=0,padx=50,pady=10)
        acc_no_entry=Entry(self.master3)
        amount_entry=Entry(self.master3)
        acc_no_entry.grid(row=0,column=1,padx=10,pady=10)
        amount_entry.grid(row=1,column=1,padx=10,pady=10)
        submit=Button(self.master3,text="Submit",bg = "yellow",command=lambda:self.calculate_withdrawl(acc_no_entry, amount_entry))
        submit.grid(row=2,column=1,padx=10,pady=10)
        self.master3.mainloop() 
    
    def calculate_deposit(self, acc_no_entry, amount_entry):
        acc_no_entry = acc_no_entry.get()
        amount_entry = amount_entry.get()
        self.accounts['acc_no_entry'] = acc_no_entry
        self.accounts['amount_entry'] = amount_entry
        self.current_balance += float(self.accounts['amount_entry'])
        print(f"{float(self.accounts['amount_entry'])} deposited into account {float(self.accounts['acc_no_entry'])}. New balance: {self.current_balance}")

    def deposit(self):
        self.master4=Toplevel(self.master)
        self.master4.geometry('500x500')
        self.master4['background'] = '#58F'
        self.master4.title("Amount Deposite Window")
        self.master4.resizable(False,False)
        width= self.master4.winfo_screenwidth()
        height= self.master4.winfo_screenheight()
        self.master4.geometry('%dx%d' %(width,height))
        acc_no_label=Label(self.master4,text="Enter Your Account No:")
        amount_label=Label(self.master4,text="Enter Your Amount:")
        acc_no_label.grid(row=0,column=0,padx=50,pady=10)
        amount_label.grid(row=1,column=0,padx=50,pady=10)
        acc_no_entry=Entry(self.master4)
        amount_entry=Entry(self.master4)
        acc_no_entry.grid(row=0,column=1,padx=50,pady=10)
        amount_entry.grid(row=1,column=1,padx=50,pady=10)
        submit=Button(self.master4,text="Submit",bg = "yellow",command=lambda: [self.calculate_deposit(acc_no_entry, amount_entry),messagebox.showinfo("Information","Amount Deposited Successfully")])
        submit.grid(row=2,column=1,padx=10,pady=10)        
        self.master4.mainloop()

    def calculate_transfer(self, acc_no_entry, amount_entry):
        acc_no_entry = acc_no_entry.get()
        amount_entry = amount_entry.get()
        self.accounts['acc_no_entry'] = acc_no_entry
        self.accounts['amount_entry'] = amount_entry
        if float(self.accounts['amount_entry']) > self.current_balance:
            print("Insufficient balance!")
            messagebox.showerror("info","Insufficient balance!")
        else:
            self.current_balance -= float(self.accounts['amount_entry'])
            print(f"{float(self.accounts['amount_entry'])} withdrawn from account {self.accounts['acc_no_entry']}. New balance: {self.current_balance}")
            messagebox.showinfo("Information","Amount Transfer Successfully")
    def transfer(self):
        self.master5=Toplevel(self.master)
        self.master5.geometry('500x500')
        self.master5['background'] = '#58F'
        self.master5.title("Amount Transfer Window")
        self.master5.resizable(False,False)
        width= self.master5.winfo_screenwidth()
        height= self.master5.winfo_screenheight()
        self.master5.geometry('%dx%d' %(width,height))
        sender_acc_label=Label(self.master5,text="Enter Sender Account No:")
        rece_acc_label=Label(self.master5,text="Enter Receiver Account No:")
        money_label=Label(self.master5,text="Enter Amount:")
        sender_acc_label.grid(row=0,column=0,padx=50,pady=10)
        rece_acc_label.grid(row=1,column=0,padx=50,pady=10)
        money_label.grid(row=2,column=0,padx=50,pady=10)
        sender_acc_entry=Entry(self.master5)
        rece_acc_entry=Entry(self.master5)
        money_entry=Entry(self.master5)
        sender_acc_entry.grid(row=0,column=1,padx=10,pady=10)
        rece_acc_entry.grid(row=1,column=1,padx=10,pady=10)
        money_entry.grid(row=2,column=1,padx=10,pady=10)
        submit=Button(self.master5,text="Submit",bg = "yellow",command=lambda:self.calculate_transfer(sender_acc_entry, money_entry))
        submit.grid(row=3,column=1,padx=10,pady=10)
        self.master5.mainloop()

    def details(self):
        self.master6=Toplevel(self.master)
        self.master6.geometry('500x500')
        self.master6['background'] = '#58F'
        self.master6.title("Show Details Window")
        self.master6.resizable(False,False)
        width= self.master6.winfo_screenwidth()
        height= self.master6.winfo_screenheight()
        self.master6.geometry('%dx%d' %(width,height))
        label1=Label(self.master6, text="", font=("Courier 22 bold"))
        label1.grid(row=0,column=1,padx=10,pady=10)
        label2=Label(self.master6, text="", font=("Courier 22 bold"))
        label2.grid(row=1,column=1,padx=10,pady=10)
        label3=Label(self.master6, text="", font=("Courier 22 bold"))
        label3.grid(row=2,column=1,padx=10,pady=10)
        label4=Label(self.master6, text="", font=("Courier 22 bold"))
        label4.grid(row=3,column=1,padx=10,pady=10)
        label5=Label(self.master6, text="", font=("Courier 22 bold"))
        label5.grid(row=4,column=1,padx=10,pady=10)
        Label(self.master6, text="Account Number=", font=("Courier 22 bold")).grid(row=0,column=0,padx=10,pady=10)
        Label(self.master6, text="Customer Name=", font=("Courier 22 bold")).grid(row=1,column=0,padx=10,pady=10)
        Label(self.master6, text="Customer ID=", font=("Courier 22 bold")).grid(row=2,column=0,padx=10,pady=10)
        Label(self.master6, text="Customer Mobile No=", font=("Courier 22 bold")).grid(row=3,column=0,padx=10,pady=10)
        Label(self.master6, text="Balance=", font=("Courier 22 bold")).grid(row=4,column=0,padx=10,pady=10)
        acc=self.acc_no_entry.get()
        name=self.name_entry.get()
        id=self.id_entry.get()
        mno=self.mobileno_entry.get()
        label1.configure(text=acc)
        label2.configure(text=name)
        label3.configure(text=id)
        label4.configure(text=mno)
        label5.configure(text=self.current_balance)
        self.master6.mainloop()
                
def main():
    root=Tk()
    app=Transaction(root)
    root.title("Login Page")
    app.login()
    root.mainloop()
           
if __name__=='__main__':
    main()