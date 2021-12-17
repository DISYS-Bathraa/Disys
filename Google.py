class GooglePay:                                                                                   


    def __init__(self,EmailID,Phonenumber,Name):                                                                  
        self.emailid=EmailID
        self.mobile=Phonenumber
        self.name=Name

    def OpenGpay(self):
        print("Google Pay")


    def EmailAuthentication(self):  
        if type(self.emailid) == str:                                                                               
            if len(self.emailid) <= 30:                                                                              
                print("email-id verified")
            else:
                raise ValueError("the email-Id should not contain more 30 values")
        else:
            raise TypeError("invalid emailid")



    def MobileVerification(self):                      
        if (len(self.mobile)==10):
            if type(self.mobile) == int:                                                                            
                print("phone number verified")
            
        else:
            raise ValueError("the phone number should not be grater than or lesser than 10")

    def NameVerification(self):
        if type(self.name) == str:                     
            if len(self.name) <= 20:                                                                                
                print("name verified")
            else:
                raise ValueError("The name should contain lesser than or equal to 20 letters")
        else:
            raise TypeError("The name should contain letters only")

    def OTPVerification(self,code,otp):
        if(otp==code):
            print("otp verified")
        else:
            raise ValueError("The otp you are entered is not correct")

    def BankVerification(self):
        self.Account=[]
        self.Accountnumber=3248697451
        self.CVV=257
        self.Account.append(self.Accountnumber)                                                                
        print(self.Account)
        print("Bank account Verified") 


    def SetPin(self,number):
        self.pin=number
        if (len(self.pin)==4 or len(self.pin) ==6):
            print("your pin is successfully created")
        else:
            raise ValueError("Invalid pinnumber")

    def EnteryourPin(self,match,digit):
        self.match=match
        self.pin=digit
        if self.match==self.pin:
            print("DONE")
        else:
            raise ValueError("pin not matched")
