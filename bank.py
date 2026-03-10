class Bank_Account:
    def _init_(self,Acc_no,bal):
        self.Acc_no = Acc_no
        self.bal= bal

    def deposit(self):
        Amount=float(input("Enter the amount : "))
        self.bal= self.bal+Amount
        print(f"Balance : {self.bal}/-")

    def withdraw (self):
        Amount=float(input("Enter the amount : "))
        if Amount<= self.bal:
            self.bal= self.bal-Amount
            print(f"{Amount}RS withdrawn. Balance : {self.bal}/-")
        else :
            print("Not Sufficient Balance.")

    def check_bal(self):
        print(f"Balance : {self.bal}/-")


Acc_no=int(input("Enter Account Number:"))
bal=int(input("Enter Account Balance:"))
obj=Bank_Account(Acc_no,bal)

while True :
    print("1.Deposite\n2.Withdraw\n3.Check Balance\n4.Exit.")
    choice=int(input("Enter operation to be performed:"))
    if choice == 1 :
            obj.deposit()
     
    elif choice == 2 :
              obj.withdraw()

    elif choice == 3 :
              obj.check_bal()

    elif choice == 4 :
          print("Exited.")
          break

    else :
            print("Invalid choice.")