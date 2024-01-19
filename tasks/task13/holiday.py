"""
Prompt user to enter followings:
City they will be flying to?
How many nights they will be staying at hotel?
How many days they want to hire a car for?
Use while loop and try except error handling method to prevent
user defined error.
"""

city_flight = input("""
                Which city are you flying to?
                Choose option from below:
                1. Rome
                2. Paris
                3. Newyork
                4. Prague
                5. Dubai
                :""").lower()

city_list = ["rome", "paris", "newyork", "prague", "dubai"]

while (city_flight not in city_list):
    print("Please enter valid city from list below")
    city_flight = input("""
                Which city are you flying to?
                Choose option from below:
                1. Rome
                2. Paris
                3. Newyork
                4. Prague
                5. Dubai
                :""").lower()

while True:
    try:
        num_nights = int(input("How many nights will you be planning to" +
                               " stay at a hotel?:"))
        break
    except ValueError:
        print("Please enter valid number")

while True:
    try:
        rentals_day = int(input("For how many days you" +
                                " will be hiring a car?:"))
        break
    except ValueError:
        print("Please enter valid number.")

"""
Define hotel cost function, calculate total hotel cost and return its value.
"""


def hotel_cost(num_nights):
    hotel_price_per_night = 100
    total_hotel_cost = hotel_price_per_night * num_nights
    return total_hotel_cost


"""
Define plane cost function, choose city, get flight cost and return value.
"""


def plane_cost(city_flight):
    city_flight_cost = 0
    if city_flight == "rome":
        city_flight_cost = 50
    elif city_flight == "paris":
        city_flight_cost = 80
    elif city_flight == "newyork":
        city_flight_cost = 300
    elif city_flight == "prague":
        city_flight_cost = 400
    elif city_flight == "dubai":
        city_flight_cost = 450
    return city_flight_cost


"""
Define car rental function and calculate total car rental cost,
then return its value.
"""


def car_rental(rentals_day):
    car_rentar_per_day = 50
    total_car_rental = car_rentar_per_day * rentals_day
    return total_car_rental


"""
Define holiday cost function which takes 3 arguments of already define
functions from above as parameters(hotel_cost, plane_cost, car_rental)
and calculates total cost of holiday.
"""


def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_holiday_cost = hotel_cost + plane_cost + car_rental
    print()
    print("*" * 50)
    print(f"Your total holiday cost will be £{total_holiday_cost}.".upper())
    print("*" * 50)
    print("Below is the breakdown of your cost.")
    print()
    print("Services", "\t", "Total Price in £")
    print("-" * 35)
    print("Flight", "\t\t\t", plane_cost)
    print("Hotel", "\t\t\t", hotel_cost)
    print("Car Rental", "\t\t", car_rental)


holiday_cost(hotel_cost(num_nights), plane_cost(city_flight),
             car_rental(rentals_day))
