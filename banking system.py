""" this programs involves storing data in a database therefore for the program to run properly, MYSQL database is needed.
therefore one should have wampserver loaded on the computer so as to be able to store the banks data in the database.
the code for creating the database can be executed once afterwhich it can be commented out, this code is illustred with a comment.

the details of the tellers have to be inserted into the database directly since one cannot make themselves a teller
"""

import pymysql

def bank():
    
    print('\n')
    print('1.bankA')
    print('2.bankB')
    select11 = input('please select from the above menu: ')

    while select11 <'3':   #tells the user to either select bankA or B
        if select11 == 1:
            bankA()

        if select11 == 2:
            bankB()

def bankA():
    
    connection = pymysql.connect("localhost","root","","" )   #creating a database where the details are to be stored
    cursor = connection.cursor()
    
    cursor.execute("CREATE DATABASE  bankA")
    cursor.close()
    connection.close()

    connection = pymysql.connect("localhost","root","","bankA" )
    cursor = connection.cursor()
    cursor.execute( "CREATE TABLE  customer(customerId INT PRIMARY KEY ,name VARCHAR(30) NOT NULL, address VARCHAR(20) NOT NULL, phoneNo INT NOT NULL, acctNo INT NOT NULL)")
    cursor.execute( "CREATE TABLE  teller(tellerId INT PRIMARY KEY ,Name VARCHAR(30) NOT NULL)")
    cursor.execute( "CREATE TABLE  bank(bankId INT PRIMARY KEY ,Name VARCHAR(30) NOT NULL, Location VARCHAR(20) NOT NULL)")
    cursor.execute( "CREATE TABLE  account(accountId INT PRIMARY KEY, status VARCHAR(30) NOT NULL, amount INT NOT NULL, customerId INT REFERENCES customer(customerId) )")
    cursor.execute( "CREATE TABLE  loan(loanId INT PRIMARY KEY ,Type VARCHAR(30) NOT NULL,amount INT NOT NULL, accountId INT NOT NULL, customerId INT REFERENCES customer(customerId))")

    cursor.close()
    connection.close()
    
    #the code for creating the database can be executed once after which it can be commented out
    
    
    
    def bankApersonel():     #ask the user whether he'sa teller or customer
        print('\n')
        print('1.Teller')
        print('2.Customer')
        select11 = input('please select from the above menu: ')

        while select11 < 3:
            if select11 == 1:
                teller(bankA)

            if select11 == 2:
                customerA(bankA)
    bankApersonel()       

def bankB():
    
    connection = pymysql.connect("localhost","root","","" )    #creating a database for bankB
    cursor = connection.cursor()
    cursor.execute( "CREATE DATABASE  bankB")
    cursor.close()
    connection.close()

    connection = pymysql.connect("localhost","root","","bankB" )
    cursor = connection.cursor()
    cursor.execute( "CREATE TABLE  customer(customerId INT PRIMARY KEY ,name VARCHAR(30) NOT NULL, address VARCHAR(20) NOT NULL, phoneNo INT NOT NULL, acctNo INT NOT NULL)")
    cursor.execute( "CREATE TABLE  teller(tellerId INT PRIMARY KEY ,Name VARCHAR(30) NOT NULL)")
    cursor.execute( "CREATE TABLE  bank(bankId INT PRIMARY KEY ,Name VARCHAR(30) NOT NULL, Location VARCHAR(20) NOT NULL)")
    cursor.execute( "CREATE TABLE  account(accountId INT PRIMARY KEY, status VARCHAR(30) NOT NULL, amount INT NOT NULL, customerId INT REFERENCES customer(customerId) )")
    cursor.execute( "CREATE TABLE  loan(loanId INT PRIMARY KEY ,Type VARCHAR(30) NOT NULL, amount INT NOT NULL, accountId INT NOT NULL, customerId INT REFERENCES customer(customerId))")
    
    cursor.close()
    connection.close()
    
    
    def bankBpersonel():
        print('\n')
        print('1.Teller')
        print('2.Customer')
        select11 = input('please select from the above menu: ')

        while select11 < 3:
            if select11 == 1:
                teller1(bankB)

            if select11 == 2:
                customerB(bankB)
    bankBpersonel()
    
    
def customerA(bank):    #defining what a customer can do
    
    connection = pymysql.connect(host='localhost',user='root',passwd='',db='bankA',autocommit=True)
    cursor = connection.cursor()
    
    print('\n')
    print('1.Open Account')
    print('2.Deposit Amount')  
    print('3.Withdraw Amount')
    print('4.Close Account')                              
    print('5.loan')
    print('6.loan repay')
    select1 = input('please select from the above menu: ')


    while select1 < 7:
        
        if select1 == 1:        #opening an account
            customerid = input('CustomerId: ')
            name = raw_input('Name: ')
            Address = raw_input('Address: ')
            phoneNo = input('PhoneNo: ')            
            acctNo = input('AccountNo: ')
            acctId = input('AccountId: ')
            acctType = raw_input('AccountType savings account or checking account: ')
            Intial_Deposit_Amount = input('Intial_Deposit_Amount: ')

            query = "INSERT INTO customer (customerId, Name,Address,phoneNo,acctNo) VALUES(%s,%s,%s,%s,%s)"
            query1 = "INSERT INTO account (accountId, status,amount,customerId) VALUES(%s,%s,%s,%s)"
            
            if(cursor.execute(query, (customerid,name,Address,phoneNo,acctNo))):
                if(cursor.execute(query1, (acctId,acctType,Intial_Deposit_Amount,customerid))):
                    print('Thanks for creating a new account with us!')
                    customerA(bank)
                else:
                    print('amount not deposited')
                    customerA(bank)   
                                
        if select1 == 2:      #depositing money to your account
            
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            amount1 = input('Amount :')
                        
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute( "UPDATE account SET amount = amount + %s WHERE customerId = %s ",(amount1,customerid))):
                        print('Your amount was deposited!')
                        customerA(bank)
                    else:
                        print('amount not deposited')
                        customerA(bank)
                                                                        
        if select1 == 3:    #withdrawing money from the account
                        
           
            customerid = input('customerId : ')
            account_number = input('Account Number :')	
            amount1 = input('Amount :')
            
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute( "UPDATE account SET amount = amount - %s WHERE customerId = %s ",(amount1,customerid))):
                                
                        print('Your amount was withdrawn!')
                        customerA(bank)
                    else:
                        print('amount not withdrawn')
                        
                        customerA(bank)

                        
        if select1 == 4:    #closing an account by customer
           
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            if(cursor.execute( "DELETE FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "DELETE  FROM account WHERE customerId = %s",(customerid))):
                    print('Account Closed!')
                    customerA(bank)
                else:
                    print('Account not Closed')
                    customerA(bank)

        
        if select1 == 5:    #requesting for a loan
            
            loan_Id = input('Loan_Id:')
            loan_Type = raw_input('Loan_Type:')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            account_Id = input('Account_Id:')
            LoanAmount = input('LoanAmount :')

            query1 = "INSERT INTO loan (loanId,Type,amount,accountId,customerId) VALUES(%s,%s,%s,%s,%s)"
            
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute(query1,(loan_Id,loan_Type,LoanAmount,account_Id,customerid))):
                                
                        print('Loan processed!')
                        customerA(bank)
                    else:
                        print('Loan not processed')
                        
                        customerA(bank)

        if select1 == 6:  #paying back the loan
            
            loan_Id = input('Loan_Id:')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            amount1 = input('Loan Amount payment :')

           
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute("UPDATE loan SET amount = amount - %s WHERE loanId = %s ",(amount1,loan_Id))):
                        print('Loan processed!')
                        customerA(bank)
                    else:
                        print('Loan not processed')
                        
                        customerA(bank)

        
        else:
            print('Invalid option!')
            customerA(bank)

    cursor.close()
    connection.close()

def teller(bank):         #defining activities ofthe teller
    connection = pymysql.connect(host='localhost',user='root',passwd='',db='bankA',autocommit=True)
    cursor = connection.cursor()

    def tellerA(bank):

        connection = pymysql.connect(host='localhost',user='root',passwd='',db='bankA',autocommit=True)
        cursor = connection.cursor()
        
        print('\n')
        print('1.Open Account')
        print('2.Collect money')                                                 
        print('3.Close Account')
        print('4.process Loan')
        
        select1 = input('please select from the above menu: ')

        while select1 <6:  #the teller has to be first inserted into the database
            
            if select1 == 1:  #the teller can open an account for a customer
                customerid = input('CustomerId: ')
                name = raw_input('Name: ')
                Address = raw_input('Address: ')
                phoneNo = input('PhoneNo: ')            
                acctNo = input('AccountNo: ')
                acctId = input('AccountId: ')
                acctType = raw_input('AccountType savings account or checking account: ')
                Intial_Deposit_Amount = input('Intial_Deposit_Amount: ')

                query = "INSERT INTO customer (customerId, Name,Address,phoneNo,acctNo) VALUES(%s,%s,%s,%s,%s)"
                query1 = "INSERT INTO account (accountId, status,amount,customerId) VALUES(%s,%s,%s,%s)"
                
                if(cursor.execute(query, (customerid,name,Address,phoneNo,acctNo))):
                    if(cursor.execute(query1, (acctId,acctType,Intial_Deposit_Amount,customerid))):
                        print('Thanks for creating a new account with us!')
                        tellerA(bank)
                    else:
                        print('amount not deposited')
                        tellerA(bank)

            if select1 == 2:   #the teller can deposit money for a customer
               
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                amount1 = input('Amount :')
                            
                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute( "UPDATE account SET amount = amount + %s WHERE customerId = %s ",(amount1,customerid))):
                            print('Your amount was deposited!')
                            tellerA(bank)
                        else:
                            print('amount not deposited')
                            tellerA(bank)
                                    

            if select1 == 3:   #teller can close an account
              
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                if(cursor.execute( "DELETE FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "DELETE  FROM account WHERE customerId = %s",(customerid))):
                        print('Account Closed!')
                        tellerA(bank)
                    else:
                        print('Account not Closed')
                        tellerA(bank)

                        
            if select1 == 4:    #teller can process a loan for a customer
            
                loan_Id = input('Loan_Id:')
                loan_Type = raw_input('Loan_Type:')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                account_Id = input('Account_Id:')
                LoanAmount = input('LoanAmount :')

                query1 = "INSERT INTO loan (loanId,Type,amount,accountId,customerId) VALUES(%s,%s,%s,%s,%s)"
                
                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute(query1,(loan_Id,loan_Type,LoanAmount,account_Id,customerid))):
                                    
                            print('Loan processed!')
                            tellerA(bank)
                        else:
                            print('Loan not processed')
                            
                            tellerA(bank)
                            
            if select1 == 5:
                loan_Id = input('Loan_Id:')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                amount1 = input('Loan Amount payment :')

                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute("UPDATE loan SET amount = amount - %s WHERE loanId = %s ",(amount1,loan_Id))):
                            print('Loan processed!')
                            tellerA(bank)
                        else:
                            print('Loan not processed')
                            
                            tellerA(bank)

            
            else:
                print('Invalid option!')
                tellerA(bank)

        cursor.close()
        connection.close()

        
    name = raw_input('Name : ')
    tellerid = input('tellerId : ')

    if(cursor.execute( "SELECT * FROM teller WHERE tellerId = %s AND Name = %s",(tellerid,name))):
        tellerA(bank)

def customerB(bank):
    
    connection = pymysql.connect(host='localhost',user='root',passwd='',db='bankB',autocommit=True)
    cursor = connection.cursor()
    
    print('\n')
    print('1.Open Account')
    print('2.Deposit Amount')  
    print('3.Withdraw Amount')
    print('4.Close Account')                              
    print('5.loan')
    print('6.loan repay')
    select1 = input('please select from the above menu: ')


    while select1 < 7:
        
        if select1 == 1:
            customerid = input('CustomerId: ')
            name = raw_input('Name: ')
            Address = raw_input('Address: ')
            phoneNo = input('PhoneNo: ')            
            acctNo = input('AccountNo: ')
            acctId = input('AccountId: ')
            acctType = raw_input('AccountType savings account or checking account: ')
            Intial_Deposit_Amount = input('Intial_Deposit_Amount: ')

            query = "INSERT INTO customer (customerId, Name,Address,phoneNo,acctNo) VALUES(%s,%s,%s,%s,%s)"
            query1 = "INSERT INTO account (accountId, status,amount,customerId) VALUES(%s,%s,%s,%s)"
            
            if(cursor.execute(query, (customerid,name,Address,phoneNo,acctNo))):
                if(cursor.execute(query1, (acctId,acctType,Intial_Deposit_Amount,customerid))):
                    print('Thanks for creating a new account with us!')
                    customerB(bank)
                else:
                    print('amount not deposited')
                    customerB(bank)   
                                
        if select1 == 2:
            
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            amount1 = input('Amount :')
                        
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute( "UPDATE account SET amount = amount + %s WHERE customerId = %s ",(amount1,customerid))):
                        print('Your amount was deposited!')
                        customerB(bank)
                    else:
                        print('amount not deposited')
                        customerB(bank)
                                                                        
        if select1 == 3:
                        
           
            customerid = input('customerId : ')
            account_number = input('Account Number :')	
            amount1 = input('Amount :')
            
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute( "UPDATE account SET amount = amount - %s WHERE customerId = %s ",(amount1,customerid))):
                                
                        print('Your amount was withdrawn!')
                        customerB(bank)
                    else:
                        print('amount not withdrawn')
                        
                        customerB(bank)

                        
        if select1 == 4:
           
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            if(cursor.execute( "DELETE FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "DELETE  FROM account WHERE customerId = %s",(customerid))):
                    print('Account Closed!')
                    customerB(bank)
                else:
                    print('Account not Closed')
                    customerB(bank)

        
        if select1 == 5:
            
            loan_Id = input('Loan_Id:')
            loan_Type = raw_input('Loan_Type:')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            account_Id = input('Account_Id:')
            LoanAmount = input('LoanAmount :')

            query1 = "INSERT INTO loan (loanId,Type,amount,accountId,customerId) VALUES(%s,%s,%s,%s,%s)"
            
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute(query1,(loan_Id,loan_Type,LoanAmount,account_Id,customerid))):
                                
                        print('Loan processed!')
                        customerB(bank)
                    else:
                        print('Loan not processed')
                        
                        customerB(bank)

        if select1 == 6:
            
            loan_Id = input('Loan_Id:')
            customerid = input('customerId : ')
            account_number = input('Account Number :')
            amount1 = input('Loan Amount payment :')

           
            if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                    if(cursor.execute("UPDATE loan SET amount = amount - %s WHERE loanId = %s ",(amount1,loan_Id))):
                        print('Loan processed!')
                        customerB(bank)
                    else:
                        print('Loan not processed')
                        
                        customerB(bank)
        
        else:
            print('Invalid option!')
            customerB(bank)

    cursor.close()
    connection.close()



def teller1(bank):
    connection = pymysql.connect(host='localhost',user='root',passwd='',db='bankB',autocommit=True)
    cursor = connection.cursor()

    def tellerB(bank):

        connection = pymysql.connect(host='localhost',user='root',passwd='',db='bankB',autocommit=True)
        cursor = connection.cursor()
        
        print('\n')
        print('1.Open Account')
        print('2.Collect money')                                                 
        print('3.Close Account')
        print('4.process Loan')
        print('5.Logout')
        
        select1 = input('please select from the above menu: ')

        while select1 <6:
            
            if select1 == 1:
                customerid = input('CustomerId: ')
                name = raw_input('Name: ')
                Address = raw_input('Address: ')
                phoneNo = input('PhoneNo: ')            
                acctNo = input('AccountNo: ')
                acctId = input('AccountId: ')
                acctType = raw_input('AccountType savings account or checking account: ')
                Intial_Deposit_Amount = input('Intial_Deposit_Amount: ')

                query = "INSERT INTO customer (customerId, Name,Address,phoneNo,acctNo) VALUES(%s,%s,%s,%s,%s)"
                query1 = "INSERT INTO account (accountId, status,amount,customerId) VALUES(%s,%s,%s,%s)"
                
                if(cursor.execute(query, (customerid,name,Address,phoneNo,acctNo))):
                    if(cursor.execute(query1, (acctId,acctType,Intial_Deposit_Amount,customerid))):
                        print('Thanks for creating a new account with us!')
                        tellerB(bank)
                    else:
                        print('amount not deposited')
                        tellerB(bank)

            if select1 == 2:
              
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                amount1 = input('Amount :')
                            
                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute( "UPDATE account SET amount = amount + %s WHERE customerId = %s ",(amount1,customerid))):
                            print('Your amount was deposited!')
                            tellerB(bank)
                        else:
                            print('amount not deposited')
                            tellerB(bank)
                                    

            if select1 == 3:
                
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                if(cursor.execute( "DELETE FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "DELETE  FROM account WHERE customerId = %s",(customerid))):
                        print('Account Closed!')
                        tellerB(bank)
                    else:
                        print('Account not Closed')
                        tellerB(bank)

                        
            if select1 == 4:
            
                loan_Id = input('Loan_Id:')
                loan_Type = raw_input('Loan_Type:')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                account_Id = input('Account_Id:')
                LoanAmount = input('LoanAmount :')

                query1 = "INSERT INTO loan (loanId,Type,amount,accountId,customerId) VALUES(%s,%s,%s,%s,%s)"
                
                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute(query1,(loan_Id,loan_Type,LoanAmount,account_Id,customerid))):
                                    
                            print('Loan processed!')
                            tellerB(bank)
                        else:
                            print('Loan not processed')
                            
                            tellerB(bank)
                            
            if select1 == 5:
                loan_Id = input('Loan_Id:')
                customerid = input('customerId : ')
                account_number = input('Account Number :')
                amount1 = input('Loan Amount payment :')

                if(cursor.execute( "SELECT * FROM customer WHERE customerId = %s AND acctNo = %s",(customerid,account_number))):
                    if(cursor.execute( "SELECT * FROM account WHERE customerId = %s",(customerid))):
                        if(cursor.execute("UPDATE loan SET amount = amount - %s WHERE loanId = %s ",(amount1,loan_Id))):
                            print('Loan processed!')
                            tellerB(bank)
                        else:
                            print('Loan not processed')
                            
                            tellerB(bank)

            
           
            else:
                print('Invalid option!')
                tellerB(bank)

        cursor.close()
        connection.close()
        
    name = raw_input('Name : ')
    tellerid = input('tellerId : ')

    if(cursor.execute( "SELECT * FROM teller WHERE tellerId = %s AND Name = %s",(tellerid,name))):
        tellerB(bank)
     
bank()
