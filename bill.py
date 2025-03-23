import random
print("------------")
print("XYZ Restaurant")
print("somewhere in India")
print("Mob No.1234567890")
print("Guest check")
print("Thank you for Visiting")
print("Please visit us on facebook at XYZ Restaurant""\n""We welcome all feedback regarding your visit""\n""Email us at xyz@13gmail.com")
import random
randomnum=random.randint(1,20)
print("Table:",randomnum)
print("-----------------")
print("Menu")
print("-----------------")
total = 0
items = [] 

while True:  
    print("S.no.       Item")
    print("1          Starters")
    print("2          Main Course")
    print("3          Chinese")
    print("4          Italian")
    print("5          Dessert")
    print("6          Exit")

    a = int(input("Enter the S.no. that you would like to eat: "))

    if a == 6:
        print("Thanks for visiting")
        break
    elif a == 1:
        while True:
            print("Starters")
            print("S.No.   Item                 Amt")
            print("1       Panipuri             100")
            print("2       Antipasto Bites      150")
            print("3       Tomato bruschetta    150")
            print("4       Methi pakora         200")
            print("5       Padron Peppers       250")
            print("6       Exit")
            b = int(input("Enter the S.no. that you would like to eat: "))
            if b == 6:
                break
            elif b == 1:
                total += 100
                items.append(("Panipuri", 1, 100))
            elif b == 2:
                total += 150
                items.append(("Antipasto Bites", 1, 150))
            elif b == 3:
                total += 150
                items.append(("Tomato bruschetta", 1, 150))
            elif b == 4:
                total += 200
                items.append(("Methi pakora", 1, 200))
            elif b == 5:
                total += 250
                items.append(("Padron Peppers", 1, 250))
            else:
                print("Invalid choice, please try again.")
    elif a == 2:
        while True:
            print("Main Course")
            print("S.No.   Item                 Amt")
            print("1       Palak Paneer         250")
            print("2       Chana Masala         250")
            print("3       Enchilada Pasta      300")
            print("4       Lasagna              300")
            print("5       Chicken Bhuna        350")
            print("6       Exit")
            b = int(input("Enter the S.no. that you would like to eat: "))
            if b == 6:
                break
            elif b == 1:
                total += 250
                items.append(("Palak Paneer", 1, 250))
            elif b == 2:
                total += 250
                items.append(("Chana Masala", 1, 250))
            elif b == 3:
                total += 300
                items.append(("Enchilada Pasta", 1, 300))
            elif b == 4:
                total += 300
                items.append(("Lasagna", 1, 300))
            elif b == 5:
                total += 350
                items.append(("Chicken Bhuna", 1, 350))
            else:
                print("Invalid choice, please try again.")
    elif a == 3:
        while True:
            print("Chinese")
            print("S.No.   Item                 Amt")
            print("1       Manchurian           200")
            print("2       Spring Rolls         200")
            print("3       Schezwan Rice        250")
            print("4       Chow Mein            250")
            print("5       Momos                250")
            print("6       Exit")
            b = int(input("Enter the S.no. that you would like to eat: "))
            if b == 6:
                break
            elif b == 1:
                total += 200
                items.append(("Manchurian", 1, 200))
            elif b == 2:
                total += 200
                items.append(("Spring Rolls", 1, 200))
            elif b == 3:
                total += 250
                items.append(("Schezwan Rice", 1, 250))
            elif b == 4:
                total += 250
                items.append(("Chow Mein", 1, 250))
            elif b == 5:
                total += 250
                items.append(("Momos", 1, 250))
            else:
                print("Invalid choice, please try again.")
    elif a == 4:
        while True:
            print("Italian")
            print("S.No.   Item                 Amt")
            print("1       Pizza                300")
            print("2       Pasta                300")
            print("3       Risotto              300")
            print("4       Tiramisu             300")
            print("5       Focaccia             300")
            print("6       Exit")
            b = int(input("Enter the S.no. that you would like to eat: "))
            if b == 6:
                break
            elif b == 1:
                total += 300
                items.append(("Pizza", 1, 300))
            elif b == 2:
                total += 300
                items.append(("Pasta", 1, 300))
            elif b == 3:
                total += 300
                items.append(("Risotto", 1, 300))
            elif b == 4:
                total += 300
                items.append(("Tiramisu", 1, 300))
            elif b == 5:
                total += 300
                items.append(("Focaccia", 1, 300))
            else:
                print("Invalid choice, please try again.")
    elif a == 5:
        while True:
            print("Dessert")
            print("S.No.   Item                 Amt")
            print("1       Cake                 200")
            print("2       Ice Cream            200")
            print("3       Chocolate            200")
            print("4       Brownie              200")
            print("5       Fruit Salad          200")
            print("6       Exit")
            b = int(input("Enter the S.no. that you would like to eat: "))
            if b == 6:
                break
            elif b == 1:
                total += 200
                items.append(("Cake", 1, 200))
            elif b == 2:
                total += 200
                items.append(("Ice Cream", 1, 200))
            elif b == 3:
                total += 200
                items.append(("Chocolate", 1, 200))
            elif b == 4:
                total += 200
                items.append(("Brownie", 1, 200))
            elif b == 5:
                total += 200
                items.append(("Fruit Salad", 1, 200))
            else:
                print("Invalid choice, please try again.")
    else:
        print("Invalid choice, please try again.")
final_items = {}
for item_name, qty, price in items:
    if item_name in final_items:
        final_items[item_name]['qty'] += qty
        final_items[item_name]['total'] += price
    else:
        final_items[item_name] = {'qty': qty, 'total': price}

print("Item           Qty         Total Amt")
print("------------------------------------")
for item_name, details in final_items.items():
    print(f"{item_name: <16}{details['qty']}         {details['total']}")
print("------------------------------------")
print("Total Amt =", total)
