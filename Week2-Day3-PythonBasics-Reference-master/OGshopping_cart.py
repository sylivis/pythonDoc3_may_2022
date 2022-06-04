
running = True
cart = {}
print("What would you like to do?")
print("Show Cart (Type: 'show') \nRemove an Item in your cart (Type: 'remove') \nadd new item to cart(Type: 'add') \nQuit(Type: 'quit')\n")


while running == True:
    request = input("I would like to...\n").lower()

    #Show Cart
    if request == "show":
        if len(cart) < 1: #gotcha
            print("Sorry! You have no items in your cart. \nTry adding some...")
        else:
            total = sum(cart.values())
            print("Your Cart:\n")
            for i in cart:
                if cart[i] > 0:
                    print(i + " : " + str(cart[i]))
            print("Your Total is " + str(total))

    #Add to Cart   
    if request == "add":
        item = str(input("Whould item would you like to add to your cart?"))
        item_num = 1
        og_len = len(item)
        for i in cart:
            if item == i:
                item_num += 1
                item = "".join(c for c in item if c.isalpha())
                item = item + str(item_num)
        try:
            price = float(input("how much does it cost?")) 
            cart[item] = price
            price_list = cart.values()
            total = sum(price_list)
            print("Item Added!")
            print("your new total is " + str(total))
        except:
            print("Try entering your price as number please :)") #gotcha

            
    #Remove from Cart
    if request == "remove":
        if len(cart) < 1: #gotcha
            print("Sorry! You have no items in your cart. \nTry adding some...")
        else:
            item_count = 0
            cart_key_list = []
            for i in cart:
                item_count += 1
                cart_key_list.append(i)
                print(str(item_count) + ":" + i)
            try:
                item_number = int(input("Which Item Would you like to remove? \n (try typing the number to the left of the item)"))
                if item_number > item_count or item_number < 0:
                    print("Next time, try useing a number. \n(specifically one on the list...)")
                    break
                del cart[cart_key_list[item_number - 1]]
                print("Item Removed.")
            except:
                print("Next time, try useing a number. \n(specifically one on the list)")
             
    #Quit Program
    if request == "quit":
        running = False
        
    #error
    if request != "quit" and request != "show" and request != "remove" and request != "add":
        print("That doesnt seem right...")
        print("Try one of these: \n")
        print("Show Cart (Type: 'show') \nRemove an Item in your cart (Type: 'remove') \nadd new item to cart(Type: 'add') \nQuit(Type: 'quit')\n")


total = sum(cart.values())
if len(cart) < 1: #gotcha
    print("You never added any items to your cart.")
else:
    total = sum(cart.values())
    print("Your Cart:\n")
    for i in cart:
        if cart[i] > 0:
            print(i + " : " + str(cart[i]))
    print("Your Total is " + str(total))
print("Byeeee")