# Coleman Petras
# SDEV 220
# M03 Lab - Case Study: Lists, Functions, and Classes

# A super class called Vehicle, which contains an attribute 
# for vehicle type such as car, truck, plane, boat, or broomstick

class Vehicles():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
    
# A class called Automobile which will inherit the attributes from
# Vehicle, and also contain the following attributes:
# year, make, model, doors (2 or 4), roof (solid or sun roof)

class Automobile(Vehicles):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def validate_doors(doors):
    if doors not in ['2', '4']:
        raise ValueError("Invalid input for doors. Please enter 2 or 4.")
    return doors

def validate_roof(roof):
    if roof.lower () not in ['solid', 'sun roof']:
        raise ValueError("Invalid input for roof type. Please enter eithe solid or sun roof.")
    return roof

def main():
    vehicle_type = input("Please enter the type of vehicle: ")
    
    while True:
        year = input("Please enter the year of your vehicle: ")
        if not year.isdigit():
            print("Invalid input for year. Please enter a valid year")
            continue
        make = input("Please enter the make of your car: ")
        model = input("Please enter the model of your car: ")

        doors = input("Please enter the amount of doors (2 or 4): ")
        try:
            doors = validate_doors(doors)
        except ValueError as ve:
            print(ve)
            continue

        roof = input("please enter the type of roof (solid or sun roof): ")
        try:
            roof = validate_roof(roof)
        except ValueError as ve:
            print(ve)
            continue
    
    # If all inputs are valid, break from the loop
        break

    # Create an instance of Automobile
    car = Automobile(vehicle_type, year, make, model, doors, roof)


    # Output vehicle information
    print("\nVehicle Information:")
    print(f" Vehicle type: {car.vehicle_type}")
    print(f" Year: {car.year}")
    print(f" Make: {car.make}")
    print(f" Model: {car.model}")
    print(f" Number of Doors: {car.doors}")
    print(f" Type of roof: {car.roof}")

if __name__ =="__main__":
    main()