import PhneBook

B= PhneBook.PhoneContacts("bathraa","sethuraman","9629247229","bathraars30@gmail.com","17/04/2001")
B.Openphcontacts()
B.FirstnameVerification()
B.LastnameVerification()
B.PhonenumberVerification()
B.EmailidVerification()
B.DobVerification()



        
phone=[{"Firstname":"siddharth","Lastname":"bala","Phno":9857720857,"Email_id":"siddy16@gmail.com","DOB":"15/06/1998"},                                  
           {"Firstname":"bathraa","Lastname":"sethuraman","Phno":9629247229,"Email_id":"bathraars30@gmail.com","DOB":"20/08/2001"},]


'''Looping'''

for i in phone:                                                                                                             
    for j,k in i.items():                                                                                                     
        print(f"{j}:{k}")
