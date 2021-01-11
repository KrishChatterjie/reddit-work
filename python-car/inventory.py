class Car:
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage
    
    def update_car(self, attribute, value):
        if attribute == 1:
            self.__make = value
        elif attribute == 2:
            self.__model = value
        elif attribute == 3:
            self.__color = value
        elif attribute == 4:
            self.__year = value
        elif attribute == 5:
            self.__mileage = value

    def values(self):
        return (self.__make, self.__model, self.__color, self.__year, self.__mileage)



inventory = []
choice = 0


def add(inventory):
    print("Enter make: ")
    make = input()
    print("Enter model: ")
    model = input()
    print("Enter color: ")
    color = input()
    while True:
        print("Enter year: ")
        try:
            year = int(input())
        except:
            print("Please enter an integer")
            continue
        break
    while True:
        print("Enter mileage: ")
        try:
            mileage = int(input())
        except:
            print("Please enter an integer")
            continue
        break
    inventory.append(Car(make, model, color, year, mileage))
    return inventory

def enter_choice(inventory):
    i = 1
    for car in inventory:
        print(i, car.values())
        i += 1
    
    while True:
        print('Enter the car number to choose: ')
        try:
            car_no = int(input())
        except:
            print("Please enter an integer")
            continue
        if car_no not in range(1,len(inventory)+1):
            print('Please enter a valid number')
            continue
        break
    return car_no


def remove(inventory):
    choice = enter_choice(inventory)
    inventory.pop(choice-1)
    return inventory


def update(inventory):
    car_choice = enter_choice(inventory)

    while True:
        print('Press 1 to edit make')
        print('Press 2 to edit model')
        print('Press 3 to edit color')
        print('Press 4 to edit year')
        print('Press 5 to edit mileage')
        try:
            attribute_choice = int(input())
        except:
            print("Please enter an integer")
            continue
        if attribute_choice not in range(1,6):
            print("Please input a number between 1-5")
            continue
            
        if attribute_choice == 1:
            print("Enter make: ")
            value = input()
        if attribute_choice == 2:
            print("Enter model: ")
            value = input()
        if attribute_choice == 3:
            print("Enter color: ")
            value = input()
        if attribute_choice == 4:
            while True:
                print("Enter year: ")
                try:
                    value = int(input())
                except:
                    print("Please enter an integer")
                    continue
                break
        if attribute_choice == 5:
            while True:
                print("Enter mileage: ")
                try:
                    value = int(input())
                except:
                    print("Please enter an integer")
                    continue
                break
        break
        
    inventory[car_choice-1].update_car(attribute_choice, value)
    return inventory



while choice != 4:
    print('\n\n----MENU----')
    print('Press 1 to add new car')
    print('Press 2 to remove car from inventory')
    print('Press 3 to update values of a car')
    print("Press 4 to display the cars, output to 'inventory.txt' and exit")
    try:
        choice = int(input())
    except:
        print("Please input a number")
        continue
    if choice not in range(1,5):
        print("Please input a number between 1-4")
        continue
    
    if choice == 1:
        inventory = add(inventory)
        print('Car added!')
    elif choice == 2:
        inventory = remove(inventory)
        print('Car removed!')
    elif choice == 3:
        inventory = update(inventory)
        print('Inventory updated!')
    elif choice == 4:
        with open('inventory.txt', 'w') as f: 
            for car in inventory:
                f.write(str(car.values())+'\n')
