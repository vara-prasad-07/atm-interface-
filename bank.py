import tkinter as tk
from tkinter import messagebox


class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Banking System")
        self.root.geometry("400x400")
        self.root.config(background='#000C66')

        self.accounts = {"user123": {"pin": "1234", "balance": 1000 },"23211A04D9":{"pin":"04D9","balance":100}}
        self.current_user = None

        self.login_screen()

    def login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="ATM Banking System", font=("Airal", 28),fg="#FFFFFF",bg="black",relief="raised",bd=5,padx=200).pack(padx=10,pady=10)
        tk.Label(self.root, text="Enter Account Number",font=('Helvetica',24,'bold'),fg="#FFFFFF",bg="#222222").pack(pady=10)
        self.account_entry = tk.Entry(self.root,width=50,relief="raised",bd=10)
        self.account_entry.pack(pady=5)

        tk.Label(self.root, text="Enter PIN",font=('Helvetica',24,'bold'),fg="#FFFFFF",bg="#222222").pack(pady=10)
        self.pin_entry = tk.Entry(self.root, width=50,relief="raised",bd=10,show="*")
        self.pin_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login,font=('Helvetica',12,'bold'),relief="raised",bd=5,bg="#FF3386").pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        account_number = self.account_entry.get()
        pin = self.pin_entry.get()

        if account_number in self.accounts and self.accounts[account_number]["pin"] == pin:
            self.current_user = account_number
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid account number or PIN")

    def main_menu(self):
        self.clear_screen()

        tk.Label(self.root, text="Main Menu", font=("Airal", 28),fg="#FFFFFF",bg="black",relief="raised",bd=10,padx=200).pack(pady=10)
        tk.Button(self.root, text="Balance Inquiry", command=self.balance_inquiry,font=('Helvetica',15,'bold'),relief="raised",bd=10,bg="#FFFFFF",width=12).place(x=0,y=140)
        tk.Button(self.root, text="Deposit", command=self.deposit ,font=('Helvetica',16,'bold'),relief="raised",bd=10,bg="#FFFFFF",width=10).place(x=0,y=240)
        tk.Button(self.root, text="Withdrawal", command=self.withdrawal,font=('Helvetica',16,'bold'),relief="raised",bd=10,bg="#FFFFFF",width=12).place(x=220,y=140)
        tk.Button(self.root, text="Logout", command=self.logout,font=('Helvetica',16,'bold'),relief="raised",bd=10,bg="#FFFFFF",fg='#FF3333',width=12).place(x=220,y=240)

    def balance_inquiry(self):
        self.clear_screen()
        balance = self.accounts[self.current_user]["balance"]
        tk.Label(self.root, text=f"Your balance is: RS{balance}/-", font=("Helvetica", 16,'bold'),relief="raised",bd=10,bg="#FFFFFF",width=50).pack(pady=60)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu,font=('Helvetica',16,'bold'),relief="raised",bd=4,bg="#FFFFFF",fg='#FF3333').pack(pady=80)

    def deposit(self):
        self.clear_screen()

        tk.Label(self.root, text="Deposit Amount", font=("Helvetica", 16,'bold'),relief="raised",bd=10,bg="#FFFFFF",width=50).pack(pady=10)
        self.deposit_entry = tk.Entry(self.root,width=50,relief="raised",bd=10)
        self.deposit_entry.pack(pady=15)
        tk.Button(self.root, text="Deposit", command=self.perform_deposit,font=('Helvetica',12,'bold'),relief="raised",bd=4,bg="#FFFFFF",fg='#FF3333').pack(pady=20)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu,font=('Helvetica',12,'bold'),relief="raised",bd=4,bg="#FFFFFF",fg='#FF3333').pack(pady=20)

    def perform_deposit(self):
        amount = float(self.deposit_entry.get())
        self.accounts[self.current_user]["balance"] += amount
        messagebox.showinfo("Success", f"${amount} deposited successfully")
        self.main_menu()

    def withdrawal(self):
        self.clear_screen()

        tk.Label(self.root, text="Withdraw Amount", font=("Helvetica", 16,'bold'),fg="black",bg="#FFFFFF",bd=8,relief="raised",width=50).pack(pady=30)
        self.withdraw_entry = tk.Entry(self.root,width=50,relief="raised",bd=10)
        self.withdraw_entry.pack(pady=15)
        tk.Button(self.root, text="Withdraw", command=self.perform_withdrawal,font=('Helvetica',12,'bold'),relief="raised",bd=4,bg="#FFFFFF",fg='#FF3333').pack(pady=20)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu,font=('Helvetica',12,'bold'),relief="raised",bd=4,bg="#FFFFFF",fg='#FF3333').pack(pady=20)

    def perform_withdrawal(self):
        amount = float(self.withdraw_entry.get())
        if self.accounts[self.current_user]["balance"] >= amount:
            self.accounts[self.current_user]["balance"] -= amount
            messagebox.showinfo("Success", f"${amount} withdrawn successfully")
        else:
            messagebox.showerror("Error", "Insufficient balance")
        self.main_menu()

    def logout(self):
        self.current_user = None
        self.login_screen()

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
