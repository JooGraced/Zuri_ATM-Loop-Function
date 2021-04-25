import random
database = {} #dictionary 

def init():
    isValidOptionSelected = False
    print('Welcome to H&H Bank')

    while isValidOptionSelected == False:

        haveAccount = int(input('Do you have an account with us: 1 (yes) 2 (no) \n? '))

        if (haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            print(register())
        else:
            print('You selected an invalid option')
    


def login():

    print('*****Login to your Account*****')

    isloginSuccessful = False

    while isloginSuccessful == False:

        accountNumberFromUser = int(input('What is your account number? \n'))
        password = input('What is your password \n')

        for accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3]== password):
                    isloginSuccessful = True
            print('Welcome our Cherished Customer to h & h Bank-Gh')
            #print('Invalid account or password')

    bankFunction(userDetails)

def register():
    print('**********REGISTER WITH h & h BANK-Gh**********')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    email = input('What is your email address? \n')
    password = input('Type in a password? \n')

    accountNumber = AccountGenerator()

    database[accountNumber] = [first_name, last_name, email, password]

    print('Your Account Has been created')
    print('== ==== ==== === ==')
    print('Your account number is:%d' %accountNumber)
    print('Make sure you keep it safe')
    print('= == === ==== === == =')
    
    login()
    

def AccountGenerator():
    print('Your Account Number has been generated to be:')
    return random.randrange(1111111111,9999999999)

def bankFunction(user):

    print('Welcome %s %s'% (user[0], user[1]))

  

    

    SelectedOption = int(input('What would you like to do today? (1) deposit (2) withdrawal (3) Logout (4) Exit\n'))

    if (SelectedOption == 1):
            
            depositFunction()
    elif(SelectedOption == 2):
            
            withdrawalFunction()
    elif(SelectedOption == 3):
            
            logout()
    elif(SelectedOption == 4):
            exit()
    else:
            print('invalid option selected')
            bankFunction(user)


def withdrawalFunction():
    print('How much would you like to withdraw?' )
    withdraw=input()
    print('You have withdrawn an amount of ', withdraw)
    print('Have a great day and thank you for banking with us')



def depositFunction():
    print('How much would you like to deposit ?')
    deposite=input()
    print('You have deposited an amount of ', deposite)
    print('Have a great day and thank you for banking with us')

def logout():
    
    login()

init()



