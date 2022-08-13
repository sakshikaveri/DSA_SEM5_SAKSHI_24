# Menu driven program using stack
# Sakshi Vadiraj Kaveri
# Roll_no- 24


# 1. Empty plan
picnic_list=[]  #empty stack
print('\n\nInitially the members in the picnic plan: ')
print(picnic_list)

while True:
    print("\nSELECT APPROPRIATE CHOICE")                    
    print("1. ADD members into the plan")  
    print("2.DELETE members in the plan") 
    print("3.Display the members in the plan")  
    print("4. Exit")  
    choice=int(input("Enter your choice: "))

    if choice==1:
        # Adding members to the plan
        total=int(input("How many members you want to add: "))
        for i in range(total):
            person=str(input("Enter the name of the person: "))
            picnic_list.append(person)
        print(picnic_list)
       
    elif choice==2:
        if len(picnic_list)==0:
            print("There are no members yet!!!")
        else:
            print('''\n
OOPS!
Since the deadline is over for registration of the names,
we can't accept further new names:
NOTE: last added name will thus be deleted, first come first serve basis''')

            
            print("Member deleted:")
            print(picnic_list.pop())
    elif choice==3:
        if len(picnic_list)==0:
            print("There are no members")
        else:
            print("\n The final members are: ")
            print(picnic_list)
    elif choice==4:
        break
    else:
        print("You have entered a wrong choice buddy!!")
    




