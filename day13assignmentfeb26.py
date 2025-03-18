print("**welcome to 5 tirties packages**")
def agra():
    print("agra package is 10k per person")
    var=input("do you want to book this package: ")
    if var == "yes":
        per_person=10000
        fullname=input("enter your fullname: ")
        age=int(input("enter your age: "))
        phone_number=int(input("enter your phone_number: "))
        emai_id=input("enter your email_id: ")
        pin_number=int(input("enter your address: "))
        number_of_persons=int(input("enter the number of persons: "))
        gst_amount=per_person+15
        total_amount=gst_amount*number_of_persons    
        total=total_amount
        if total > 100000:
           discount = total * 0.2
        elif total > 80000:
           discount = total * 0.1
        else:
            dicount = 0
        final_amount= total-discount
        print(f"total amount= {total:.2f} ")
        print(f"discount={discount:.2f}")
        print(f"final amount={final_amount:.2f}")
        print("thank you sir")
    else:
        print("thank you ")

def arunachalam():
    print("arunachalam package is 5k per person")
    var=input("do you want to book this packaage: ")
    if var == "yes":
        per_person=5000
        fullname=input("enter yourfullname: ")
        age=int(input("enter your age: "))
        phone_number=int(input("enter your phone_number: "))
        emai_id=input("enter your email_id: ")
        pin_number=int(input("enter your address: "))
        number_of_persons=int(input("enter the number of persons: "))
        gst_amount=per_person+10
        total_amount=gst_amount*number_of_persons
        total=total_amount
        if total > 100000:
           discount = total * 0.2
        elif total > 80000:
           discount = total * 0.1
        else:
            dicount = 0
        final_amount= total-discount
        print(f"total amount= {total:.2f} ")
        print(f"discount={discount:.2f}")
        print(f"final amount={final_amount:.2f}")

        print("thank you sir")
    else :
        print("thank you")

def ayodhya():
    print("ayodhya package is 10k per person ")
    var=input("do you want to book this package: ")
    if var == "yes":
        per_person=10000
        fullname=input("enter your fullnmae: ")
        age=int(input("enter your age: "))
        phone_number=int(input("enter your phone_number: "))
        emai_id=input("enter your email_id: ")
        pin_number=int(input("enter your address: "))
        number_of_persons=int(input("enter the number of persons: "))
        gst_amount=per_person+20
        total_amount=gst_amount*number_of_persons
        total=total_amount
        if total > 100000:
           discount = total * 0.2
        elif total > 80000:
           discount = total * 0.1
        else:
            dicount = 0
        final_amount= total-discount
        print(f"total amount= {total:.2f} ")
        print(f"discount={discount:.2f}")
        print(f"final amount={final_amount:.2f}")    
        print("thank you sir")

    else:
        print("thank you ")

def thiruvananthapuram():
    print("thiruvananthapuram package is 10k per person ")
    var=input("do you want to book this package: ")
    if var == "yes":
        per_person=10000
        fullname=input("enter you fullname: ")
        age=int(input("enter your age: "))
        phone_number=int(input("enter your phone_number: "))
        emai_id=input("enter your email_id: ")
        pin_number=int(input("enter your address: "))
        number_of_persons=int(input("enter the number of persons: "))
        gst_amount=per_person+10
        total_amount=gst_amount*number_of_persons
        total=total_amount
        if total > 100000:
           discount = total * 0.2
        elif total > 80000:
           discount = total * 0.1
        else:
            dicount = 0
        final_amount= total-discount
        print(f"total amount= {total:.2f} ")
        print(f"discount={discount:.2f}")
        print(f"final amount={final_amount:.2f}")    
        print("thank you sir")
    else:
        print("thank you ")  

def kerala():
    print("kerala package is 10k per person") 
    var=input("do you want to book this package: ") 
    if var == "yes":
        per_person=10000
        fullname=input("enter you fullname: ")
        age=int(input("enter your age: ")) 
        phone_number=int(input("enter your phone_number: "))
        emai_id=input("enter your email_id: ")
        pin_number=int(input("enter your address: "))
        number_of_persons=int(input("enter the number of persons: ")) 
        gst_amount=per_person+10 
        total_amount=gst_amount*number_of_persons 
        total=total_amount
        if total > 100000:
           discount = total * 0.2
        elif total > 80000:
           discount = total * 0.1
        else:
            dicount = 0
        final_amount= total-discount
        print(f"total amount= {total:.2f} ")
        print(f"discount={discount:.2f}")
        print(f"final amount={final_amount:.2f}")    

        print("thank you sir")
    else:
        print("thank you")        

def main():
    print("***welcome harsha travels***")
    print("1.agra")
    print("2.arunachalam")
    print("3.ayodhya")
    print("4.thiruvananthapuram")
    print("5.kerala")
    choose_number= int(input("enter your choice: "))
    if choose_number == 1:
        agra()
    elif choose_number == 2:
        arunachalam()
    elif choose_number == 3:
        ayodhya()
    elif choose_number == 4:
        thiruvananthapuram()
    elif choose_number == 5:
        kerala()       

    else:
        print("invalid choice")

main()



'''
output:-
 **welcome to 5 tirties packages**
***welcome harsha travels***
1.agra
2.arunachalam
3.ayodhya
4.thiruvananthapuram
5.kerala
enter your choice: 1
agra package is 10k per person
do you want to book this package: yes
enter your fullname: harshavardhan
enter your age: 20
enter your phone_number: 6281240878
enter your email_id: harsha@gmail.com
enter your address: 515411
enter the number of persons: 9
total amount= 90135.00 
discount=9013.50
final amount=81121.50
thank you sir
PS D:\kummetha harshavardhan> '''                               

                
                
                
            
            
        
        
        
                
             