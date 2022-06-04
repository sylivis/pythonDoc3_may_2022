import Exercise_module

running = True
print("what would you like to do? \nCalculate square footage of a house (type: SquareFootage) \nCalculate the circumference of a circle (type: circumference) \nQuit(type: quit)")
while running == True:
    response = input("I would like to...").lower()

    #squarefoot
    if response == "squarefootage":
        try:
            room_number = int(input("How many rooms in the house?"))
            room_area_list = []
            for n in range(room_number):
                width = int(input("what is the width of room " + str(n+1) + " in feet?"))
                length = int(input("what is the length of room " + str(n+1) + " in feet?"))
                room_area_list.append(Exercise_module.square_footage(width, length))
            print ("the square footage is " + str(sum(room_area_list)))
        except:
            print("next time try using a whole number")
    if response == "circumference":
        try:
            radius = float(input("What is the radius of the circle?"))
            if radius <= 0:
                print("Are you sure the circle is real?")
                break
            print("The circumference is " + str(Exercise_module.circumference_of_circle(radius)))
        except:
            print("next time try using a number")

    if response == "quit":
        running = False

    if response != "quit" and response != "circumference" and response != "squarefootage":
        print("Thats not right... Try one of these")
        print("Calculate square footage of a house (type: SquareFootage) \nCalculate the circumference of a circle (type: circumference) \nQuit(type: quit)")
print("Good Bye")