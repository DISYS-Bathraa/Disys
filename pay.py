import Google

bat= Google.GooglePay("bathraars30@gmail.com",'9629247229',"Bathraa Sethuraman")
bat.OpenGpay()
bat.EmailAuthentication()
bat.MobileVerification()
bat.NameVerification()
bat.OTPVerification(257543,257543)
bat.BankVerification()
bat.SetPin("3456")
bat.EnteryourPin(1278,1278)
