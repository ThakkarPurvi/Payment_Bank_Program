
# **Payment Bank Program**

In this program, there are 2 class. 

**1) Class Customer** - for customer related information

    Customer is a class for all customer-related information. 
    Once any object for this class is created, it will call the init(self) method, also known as the constructor. 
    Inside this method, we are moulding
    
        1. name as empty string
        2. account_number as empty string 
        3. balance as 0
        4. no_deposit as 0
        5. no_withdrawal as 0       
        6. no_transfers as 0
    
    str() and repr() are used to get a string representation of the object.

**2) Class Bank** - for banking related transation

    Bank class is created for all banking transactions. This class has five methods:

        Have used @classmethod decorator using the cls keyword to access class variables
    
            1. create = In the method, the system will take the name as input to create a bank account and share the account number. 
	
        Have used @staticmethod decorator as staticmethod knows nothing about the class and deals with the parameters 
	(it is bound to the class and not the object of the class).
        
            2. deposit = This method is used to deposit money in the customer's account. 
	    		 It takes the amount from the user and adds it to the customer_balance.
            3. balance = This method views the customer's bank balance by inputting the bank account number and shares the balance. 
            4. withdraw = This method is used to withdraw money from the customer's account. 
	    		  It takes the account number and amount from the user and subtracts it from the customer_balance.
            5. transfer = This method transfers money from customer account number 1 to customer account number 2 (or vice versa). It takes 
	    		  the amount from the user, subtracts it from the payee's customer_balance, and adds it to the recipient account. 



## Tech Stack

**Back-end**

- Python - version 3.10
    - [PyCharm](https://www.jetbrains.com/pycharm/) — to run the application 

## Thank you

**Sahaj Software**

- [Sahaj Software](https://sahaj.ai/) — for giving me this opportunity 

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/ThakkarPurvi)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thakkarpurvilondon/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/purvi41)

