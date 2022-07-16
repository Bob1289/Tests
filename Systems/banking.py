class Person:
    def __init__(self,name,checking,credit_score):
        self.name = name
        self.checking = checking
        self.credit_score = credit_score
        self.credit = 0
        self.debt = 0
        self.log = []

        self.log.append("New Account added")

    def open_credit_card(self):
        open = input("Would you like to open a credit card account? Y/N")
        if open == "Y":
            self.log.append("{} selected Y to open credit card".format(self.name))
            if self.credit >= 0:
                if self.credit_score > 700:
                    self.credit = 5000
                elif self.credit_score > 500:
                    self.credit = 3000
                else:
                    self.credit = 1000

                self.log.append("{} opened credit account of {}".format(self.name, self.credit))
            else:
                print("You already ahve a account")
                self.log.append("{} tried to open credit account".format(self.name))
        else:
            self.log.append("{} exited to open credit card".format(self.name))
            print("exited")

        
    
    def account_info(self):
        self.log.append(self.name + "accessed account info")
        print("{} \n {} \n {} \n {} \n {}".format(self.name,self.checking,self.credit_score,self.credit,self.debt))

    def withdraw(self):
        choose = input("Withdraw from where")
        amount = input("How much would you like to withdraw?")

        if choose == "checking":
            if amount > self.checking:
                print("withdraw amount exceeded")
                self.log.append(self.name + "failed to withdraw " + amount + "from " + self.checking)
            else:
                self.checking -= amount
                self.log.append(self.name + "withdrawing"+ amount + " from checking with balance of " + self.checking)

            if self.checking < 50:
                print("Low Balance")

            print("Remaining: " + self.checking)

        elif choose == "credit":
            if amount > self.credit:
                print("Not enough Credit")
                self.log.append(self.name + "failed to withdraw " + amount + "from " + self.credit)
            else:
                self.credit -= amount
                self.debt += amount
                self.log.append(self.name + "withdrawing" + amount + " from credit with balance of" + self.credit)

            if self.credit < 50:
                print("Low Credit")

            
            print("Remaining: " + self.credit)

    def deposit(self):
        amount = input("How much would you like to deposit")
        if self.debt > 0:
            choose = input("Would you like to pay off debt? Y/N")
            if choose == "Y":
                self.debt -= amount
                print("Remaining: " + self.debt)
                self.log.append(self.name + "depostied" + amount + " to debt with remaining" + self.debt)
        else:
            self.checking += amount
            self.log.append(self.name + "depostied" + amount + " to checking with total of" + self.checking)
            print("Amount:" + self.checking)

    def print_log(self):
        for i in self.log:
            print(i)

if __name__ == '__main__':

    system = 1
    accounts = []

    while system:

        accounts.append(Person("bob",1000,750))

        choose = input("What would you like to do ")
        if choose == "New account":

            name = input("What is your name?")
            initial = input("initial deposit amount?")
            score = input("What is your credit score?")

            accounts.append(Person(name,initial,score))
            
        elif choose == "access account":
            if len(accounts) > 0:
                account_name = input("What is your account name?")
                

                for i in accounts:
                    if i.name == account_name:
                        account_needed = accounts.index(i)

                access_acount = 1

                while access_acount:
                    choose_info = input("What would you like to do ")
                    if choose_info == "Open Credit Card":
                        accounts[account_needed].open_credit_card()
                    elif choose_info == "Info":
                        accounts[account_needed].account_info()
                    elif choose_info == "Withdraw":
                        accounts[account_needed].withdraw()
                    elif choose_info == "deposit":
                        accounts[account_needed].deposit()
                    elif choose_info == "log":
                        accounts[account_needed].print_log()
                    elif choose_info == "exit":
                        access_acount = 0
            else:
                print("No accounts at this bank")
        else:
            system = 0
                








