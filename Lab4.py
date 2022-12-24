
from calendar import month
from ctypes import sizeof
from datetime import datetime


class Breakfast:
    currentMonth = datetime.now().month
    type(currentMonth)

    
    products = {1: 'Tea', 2: 'Coffee', 3: 'Mango shake', 4: 'Sprouted salad', 5: 'boilded egg', 6: 'french fries', 7: 'Burger' , 8: 'chilli potato',9: 'lemon tea', 10: 'green tea',
    11: 'banana shake',12:'chiku shake',13:'fruit juice',14: 'vegetables juice', 15: 'papaya Shake'}

    print("1) Whole Menu")
    print("2) Seasonal Menu")
    num = int(input('Enter the choice : '))

    if(num == 1):
        print("\n\t---------MENU-------")
        for key in products:
            print(key,'-',products[key])
        prdt = int(input("\n\tEnter the choice: "))
        if(prdt==1):
            print("\n\t Item: Tea \n\t price: 1.20$\n")
        elif(prdt==2):
            print("\n\t Item: Coffee \n\t price: 1.41$\n")
        elif(prdt==3):
            print("\n\t Item: Mango Shake \n\t price: 2.01$\n")
        elif(prdt==4):
            print("\n\t Item: Sprouted Salad \n\t price: 2.20$\n")
        elif(prdt==5):
            print("\n\t Item: Boiled Egg \n\t price: 0.20$\n")                 
        elif(prdt==6):
            print("\n\t Item: French Fries \n\t price: 2.40$\n") 
        elif(prdt==7):
            print("\n\t Item: Burger \n\t price: 3.40$\n") 
        elif(prdt==8):
            print("\n\t Item: Chilli potato \n\t price: 4.20$\n") 
        elif(prdt==9):
            print("\n\t Item: Lemon Tea \n\t price: 1.20$\n") 
        elif(prdt==10):
            print("\n\t Item: Green Tea \n\t price: 2.10$\n") 
        elif(prdt==11):
            print("\n\t Item: Banana shake \n\t price: 3.25$\n") 
        elif(prdt==12):
            print("\n\t Item: Chiku shake \n\t price: 3.00$\n") 
        elif(prdt==13):
            print("\n\t Item: Fruit Juice \n\t price: 4.10$\n") 
        elif(prdt==14):
            print("\n\t Item: vegetable Juice \n\t price: 2.45$\n") 
        elif(prdt==15):
            print("\n\t Item: papaya juice \n\t price: 2.80$\n") 
        else:
            print("Please select the correct choice !!!")    
    
    elif(num == 2 and currentMonth == 8):
        print("\n\n\t---- [August  Special] -----")
        for keys2 in products:
            mylist = list(products.values())
        print("\n\n**** Tea ****"'\n\titem 1:',mylist[0],'\n\titem 2:',mylist[8],'\n\titem 3:',mylist[9],'\n\t',"\n**** JUICE ****",'\n\t item 1:',mylist[12],'\n\t item 2:',mylist[13],
        "\n\n**** Shakes ****"'\n\t item 1:',mylist[10],'\n\t item 2:',mylist[11],'\n\t item 3:',mylist[14],'\n\t item 4:',mylist[2],"\n\n**** Healthy ****"'\n\t item 1:',mylist[4],'\n\t item 2:',mylist[3],'\n')    
    else:
        print('Enter the valid choice !!!')

        
                
        
        






