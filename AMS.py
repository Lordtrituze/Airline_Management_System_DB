from models.aircraft import Aircraft
from models.passenger import Passenger
from models.flight import Flight
from models.booking import Booking
from repositories.aircraft_repository import AircraftRepository
from repositories.passenger_repository import PassengerRepository
from repositories.flight_repository import FlightRepository
from repositories.booking_repoaitory import BookingRepository

aircraft_repository = AircraftRepository()
flight_repository = FlightRepository()
passenger_repository = PassengerRepository()
booking_repository = BookingRepository()

def main():
    flag = True
    options = [1, 2, 3, 4]
    while flag:
        mainMenu()
        menuOption = int(input("\t-->  "))
        if menuOption == 0:
            exit()
        elif menuOption in options:
            subMenu(menuOption)
        else:
            print("Please Enter a valid option")
            main()

def mainMenu():
    print(f"""
            Airline Management Menu
            Enter (1) to Manage Aircrafts
            Enter (2) to Manage Flights
            Enter (3) to Manage Passengers
            Enter (4) to Manage Bookings
            Enter (0) to Exit Menu""")

def subMenu(menuOption):
    if menuOption == 1:
        print(f"""
                Aircraft Management Menu
                Enter (1) to Create Aircrafts
                Enter (2) to Search Aircrafts
                Enter (3) to Update Aircrafts
                Enter (4) to Delete Aircrafts
                Enter (5) to Print All Aircrafts
                Enter (0) to Exit to Main-Menu""")
        menuOption = int(input("\t-->  "))
        aircraftMenu(menuOption)
    elif menuOption == 2:
        print(f"""
                Flight Management Menu
                Enter (1) to Create Flight
                Enter (2) to Search Flight
                Enter (3) to Update Flight
                Enter (4) to Delete Flight
                Enter (5) to Print All Flights
                Enter (0) to Exit Main-Menu""")
        menuOption = int(input("\t-->  "))
        flightMenu(menuOption)
    elif menuOption == 3:
        print(f"""
                Passenger Management Menu
                Enter (1) to Create Passenger
                Enter (2) to Search Passenger
                Enter (3) to Update Passenger
                Enter (4) to Delete Passenger
                Enter (5) to Print All Passengers
                Enter (0) to Exit Main-Menu""")
        menuOption = int(input("\t-->  "))
        passengerMenu(menuOption)
    elif menuOption == 4:
        print(f"""
                Booking Management Menu
                Enter (1) to Create Booking
                Enter (2) to Search Booking
                Enter (3) to Update Booking
                Enter (4) to Delete Booking
                Enter (5) to Print All Bookings
                Enter (0) to Exit Main-Menu""")
        menuOption = int(input("\t-->  "))
        bookingMenu(menuOption)

# Aircraft
def aircraftMenu(menuOption):
    if menuOption == 1:
        name = input("Enter The name of the Aircraft \n :")
        model = input("Enter the model of the Aircraft \n :")
        capacity = input("Enter the capacity of the Aircraft \n :")
        reg_no = input("Enter the registration number of the Aircraft\n: ")
        aircraft = Aircraft(id=None, name=name, model=model, capacity=capacity, reg_no= reg_no, created_at=None)
        aircraft_repository.create(aircraft)
        # aircraftManager.createCraft(name, model, capacity)
        request()
        subMenu(1)
    elif menuOption == 2:
        reg_no = input('Enter the Registration number of the Aircraft \n: ')
        aircraft = aircraft_repository.find(reg_no=reg_no)
        print(aircraft)
        request()
        subMenu(1)
    elif menuOption == 3:
        aircraft_repository.showAll()
        id = int(input("Enter the id of the Aircraft you want to Update from Above \n :"))
        reg_no = input("Enter the new Registration Number of the Aircraft \n :")
        name = input("Enter The  new name of the Aircraft \n :")
        model = input("Enter the new model of the Aircraft \n :")
        capacity = int(input("Enter the new capacity of the Aircraft \n :"))
        aircraft = Aircraft(id=None, name=name, model=model, capacity=capacity, reg_no=reg_no, created_at=None)
        aircraft_repository.update(id=id, aircraft=aircraft)
        # aircraftManager.update(name, model, capacity, regNo)
        request()
        subMenu(1)
    elif menuOption == 4:
        # aircraft_repository.showAll()
        reg_no = input("Enter the Registration Number of the Aircraft you want to delete \n :")
        id = aircraft_repository.find_id(reg_no)
        if type(id) is int:
            aircraft = aircraft_repository.delete(id=id)
        else:
            aircraft = "Aircraft not found"
        print(aircraft)
        request()
        subMenu(1)
    elif menuOption == 5:
        aircraft_repository.showAll()
        request()
        subMenu(1)
    elif menuOption == 0:
        main()
    else:
        print("Please enter a valid option")
        subMenu(1)

#Flight
def flightMenu(menuOption):
    if menuOption == 1:
        aircraft = input("Enter the Registration Number of the Aircraft for the Flight \n :")
        aircraft_id = aircraft_repository.find_id(aircraft)
        if type(aircraft_id) is int:
            pass
        else:
            print("No Aircraft with the Registration Number you entered was found")
            request()
            subMenu(2)
        takeoff_location = input(
            "Enter the takeoff_location of the Flight \n :")
        destination = input(
            "Enter the destination of the Flight \n :")
        takeoff_time = input("Enter the take-off time \n :")
        arrival_time = input("Enter the arrival time \n :")
        flight_no = input("Enter the Flight")
        flight = Flight(id=None, aircraft_id=aircraft_id, takeoff_location=takeoff_location, destination=destination, takeoff_time=takeoff_time, arrival_time=arrival_time, flight_no=flight_no, created_at=None)
        flight_repository.create(flight)
        request()
        subMenu(2)
    elif menuOption == 2:
        flight_no = input('Enter the Flight Number \n: ')
        flight = flight_repository.find(flight_no=flight_no)
        print(flight)
        request()
        subMenu(2)

    elif menuOption == 3:
        passenger_repository.showAll()
        id = int(input("Enter the ID of the Flight you want to Update \n :"))
        aircraft_id = input("Enter The Aircraft ID for the Flight \n :")
        takeoff_location = input("Enter The Takeoff Location of the Flight \n :")
        destination = input("Enter The Destination of the Flight \n :")
        takeoff_time = input("Enter Takeoff Time of the Flight \n :")
        arrival_time = input("Enter Arrival Time of the Flight \n :")
        flight_no = input("Enter the Flight Number of The Flight \n :")
        flight = Flight(id=None, aircraft_id=aircraft_id, takeoff_location=takeoff_location, destination=destination, takeoff_time=takeoff_time, arrival_time=arrival_time, flight_no=flight_no, created_at=None)
        flight_repository.update(id=id, flight=flight)
        request()
        subMenu(2)
    elif menuOption == 4:
        flight_no = input("Enter the Flight Number of the Flight you want to delete \n :")
        id = flight_repository.find_id(flight_no)
        if type(id) is int:
            flight = flight_repository.delete(id=id)
        else:
            flight = "Aircraft not found"
        print(flight)
        request()
        subMenu(2)
    elif menuOption == 5:
        flight_repository.showAll()
        request()
        subMenu(2)
    elif menuOption == 0:
        main()
    else:
        print("Please enter a valid option")
        subMenu(2)

#Passenger
def passengerMenu(menuOption):
    if menuOption == 1:
        first_name = input("Enter The First Name of the Passenger \n :")
        last_name = input("Enter The Last Name of the Passenger \n :")
        email = input("Enter the email of the Passenger \n :")
        address = input("Enter the address of the Passenger \n :")
        reg_no = input("Enter the Registration Number \n :")
        passenger = Passenger(id=None, first_name= first_name, last_name=last_name, email=email, address=address, reg_no=reg_no, created_at=None)
        passenger_repository.create(passenger)
        request()
        subMenu(3)
    elif menuOption == 2:
        reg_no = input("Enter the Registration Number or Name of the Passenger you're looking for \n :")
        result = passenger_repository.find(reg_no)
        print(result)
        request()
        subMenu(3)
    elif menuOption == 3:
        passenger_repository.showAll()
        id = int(input("Enter the ID of the Passenger you want to Update \n :"))
        first_name = input("Enter The First Name of the Passenger \n :")
        last_name = input("Enter The Last Name of the Passenger \n :")
        email = input("Enter the new email of the Passenger \n :")
        address = input("Enter the new address of the Passenger \n :")
        reg_no = input("Enter the Registration Number of the Passenger \n :")
        passenger = Passenger(id=None, created_at=None, first_name=first_name, last_name=last_name, email=email, address=address, reg_no=reg_no)
        passenger_repository.update(id=id, passenger=passenger)
        request()
        subMenu(3)
    elif menuOption == 4:
        reg_no = input("Enter the Registration Number of the Passenger you want to delete \n :")
        id = passenger_repository.find_id(reg_no)
        if type(id) is int:
            passenger = passenger_repository.delete(id=id)
        else:
            passenger = "Passenger not found"
        print(passenger)
        request()
        subMenu(3)
    elif menuOption == 5:
        passenger_repository.showAll()
        request()
        subMenu(3)
    elif menuOption == 0:
        main()
    else:
        print("Please enter a valid option")
        subMenu(3)

#Booking
def bookingMenu(menuOption):
    if menuOption == 1:
        passenger = input("Enter the Registration Number of the Passenger Booking the Flight \n :")
        passenger_id = passenger_repository.find_id(passenger)
        if type(passenger_id) is int:
            pass
        else:
            print("No Passenger with the Registration Number you entered was found")
            request()
            subMenu(4)
        flight = input("Enter the Flight Number of the Flight the Passenger is Booking \n :")
        flight_id = flight_repository.find_id(flight)
        if type(flight_id) is int:
            pass
        else:
            print("No Flight with the Flight Number you entered was found")
            request()
            subMenu(4)
        booking_type = input("Which Type of Ticket does the Passenger want to Book? \n (ONE-WAY) or (RETURN): ")
        flight_class = input("Which Class of ticket is the Passenger Booking? \n (FIRST CLASS), (BUSINESS CLASS), or (ECONOMY): ")
        booking_no = input("Enter the Booking Number \n :")
        booking_date = input("Enter the date of Booking \n :")
        seat_no = input("Enter the Seat Number \n :")
        booking = Booking(id=None, passenger_id= passenger_id, flight_id= flight_id, booking_type= booking_type, flight_class= flight_class, booking_no= booking_no, booking_date= booking_date, seat_no= seat_no, created_at=None)
        booking_repository.create(booking)
        request()
        subMenu(4)
    elif menuOption == 2:
        booking_no = input("Enter the Booking Number of the Booking you're looking for \n :")
        result = booking_repository.find(booking_no)
        print(result)
        request()
        subMenu(4)
    elif menuOption == 3:
        booking_repository.showAll()
        id = int(input("Enter the ID of the Booking you want to Update \n :"))
        passenger = input("Enter the Registration Number of the Passenger Booking the Flight \n :")
        passenger_id = passenger_repository.find_id(passenger)
        if type(passenger_id) is int:
            pass
        else:
            print("No Passenger with the Registration Number you entered was found")
            request()
            subMenu(4)
        flight = input("Enter the Flight Number of the Flight the Passenger is Booking \n :")
        flight_id = flight_repository.find_id(flight)
        if type(flight_id) is int:
            pass
        else:
            print("No Flight with the Flight Number you entered was found")
            request()
            subMenu(4)
        booking_type = input("Which Type of Ticket does the Passenger want to Book? \n (ONE-WAY) or (RETURN): ")
        flight_class = input(
            "Which Class of ticket is the Passenger Booking? \n (FIRST CLASS), (BUSINESS CLASS), or (ECONOMY): ")
        booking_no = input("Enter the Booking Number \n :")
        booking_date = input("Enter the date of Booking \n :")
        seat_no = input("Enter the Seat Number \n :")
        booking = Booking(id=None, passenger_id= passenger_id, flight_id= flight_id, booking_type= booking_type, flight_class= flight_class, booking_no= booking_no, booking_date= booking_date, seat_no= seat_no, created_at=None)
        booking_repository.update(id=id, booking=booking)
        request()
        subMenu(4)
    elif menuOption == 4:
        booking_no = input("Enter the Booking Number of the Booking you want to delete \n :")
        id = booking_repository.find_id(booking_no)
        if type(id) is int:
            booking = booking_repository.delete(id=id)
        else:
            booking = "Booking not found"
        print(booking)
        request()
        subMenu(4)
    elif menuOption == 5:
        booking_repository.showAll()
        request()
        subMenu(4)
    elif menuOption == 0:
        main()
    else:
        print("Please enter a valid option")
        subMenu(4)

def request():
    answer = input(f"""Do you want to continue ?
                   (y/n) : """)
    if answer == 'y':
        pass
    elif answer == 'n':
        exit()
    else:
        print("Please enter a valid answer")
        request()

main()
