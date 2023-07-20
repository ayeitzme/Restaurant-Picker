from datetime import datetime
import pytz
from pathlib import Path
import json
import random

# Project Infomartion
# Project Name: Restaurant Picker
# Name: Amy Ehara
# Location: San Francisco, CA, USA

JSON_LIST = Path("RList.json")

class RestaurantData:
    def __init__(self):
        self.restaurants = []

    def load(self):
        with JSON_LIST.open("r") as file:
            self.restaurants = json.load(file)

    def save(self):
        with JSON_LIST.open("w") as file:
            json.dump(self.restaurants, file, indent = 6)

    def get_all_cuisines(self):
        cuisines = set()
        for restaurant in self.restaurants:
            cuisines = cuisines | set(restaurant["cuisine"])
        cuisines = list(cuisines)
        random.shuffle(cuisines)
        return cuisines

    def filter_by_cuisine(self, picked_cuisine):
        # list of restaurants with picked_cuisine
        filtered_by_cuisine = []
        # for one dictionary in list of dictionaries:
        for restaurant in self.restaurants:
            # if dictionary contains picked_cuisine as cuisine key
            if picked_cuisine in restaurant["cuisine"]:
                # add the restaurant to the filtered_restaurants list
                filtered_by_cuisine.append(restaurant)
        return filtered_by_cuisine

    def filter_by_time_of_day(self, filtered_restaurants, current_hour):
        further_filtered_list = []
        for restaurant in filtered_restaurants:
            if current_hour < 12:
                if "Breakfast" in restaurant["ToD"]:
                    further_filtered_list.append(restaurant)
            elif 12 <= current_hour < 18:
                if "Lunch" in restaurant["ToD"]:
                    further_filtered_list.append(restaurant)
            else:
                if "Dinner" in restaurant["ToD"]:
                    further_filtered_list.append(restaurant)
        return further_filtered_list

    def random_restaurant(self, further_filtered_list):
        picked_restaurant = (random.choice(further_filtered_list))
        return (picked_restaurant["name"])

    def add_restaurant(self, name, cuisines, times):
        newRest_dict = {"cuisine": cuisines, "name": name, "ToD": times}
        (self.restaurants).append(newRest_dict)

class LibraryInput():
    def __init__(self):
        self.res_data = RestaurantData()

    def input_restaurant(self):
        name = self.get_name()
        cuisines = self.get_cuisines()
        times = self.get_times()
        self.res_data.add_restaurant(name, cuisines, times)

    def get_name(self):
        restaurant_list = []
        name = input("What's the name of the restaurant? ").title()
        for restaurant in self.res_data.restaurants:
            restaurant_list.append(restaurant['name'])
        if name in restaurant_list:
            response = input("Uh oh, you already inputted this restaurant. Did you want to add a different restaurant? " )
            if response == "yes":
                name = input("What's the name of the restaurant? ").title()
            elif response == "no":
                print("No? Okay... Goodbye :>")
            else:
                print("Uh oh, that wasn't a real response. Try again! Say \"yes\" or \"no\"")
        return name
    def get_cuisines(self):
        cuisines_list = []
        cuisines_list.append(input("What's the cuisine? ").title())
        while True:
            response = input("Does another cuisine apply? yes/no? ")
            if response.lower() == "yes":
                print("If you meant no, just type 'jk'. ")
                response = input("What's the other cuisine that applies? ").title()
                if response.lower() == "jk":
                    break
                else:
                    cuisines_list.append(response)
            elif response.lower() == "no":
                print("No? Okay....")
                break
            else:
                print("Uh oh, that wasn't a real response. Try again! Say \"yes\" or \"no\"")
        return cuisines_list


    def get_times(self):
        ToD_list = []
        response = input("What time is this food for? Breakfast, Lunch, or Dinner? ").title()
        while True:
            if response in ["Breakfast", "Lunch", "Dinner"]:
                ToD_list.append(response)
                if len(ToD_list) == 3:  # all times have been added to the list
                    break
                response = ""
                # Verify response to be valid
                while response not in ["yes", "no", "jk"]:
                    response = input("Does another time apply? yes/no? ").lower()
                if response.lower() == "yes":
                    print("If you meant no, just type 'jk'. ")
                    response = input("When is the other time? ").title()
                else:
                    print("No? Okay....")
                    break
            elif response.lower() == "jk":
                break
            else:
                print("Please input Breakfast, Lunch or Dinner.")
                response = input("What time is this food for? Breakfast, Lunch, or Dinner? ").title()
        return ToD_list


    def add_library(self):
        print("Awesome, let's add a new restaurant to pick from later!")
        self.res_data.load()
        self.input_restaurant()
        while True:
            response = input("Do you have another restaurant you want to add? yes/no? ")
            if response.lower() == "yes":
                self.input_restaurant()
                pass
            elif response.lower() == "no":
                print("No? Okay... Thanks for the input!")
                break
            else:
                print("Uh oh, that wasn't a real response. Try again! Say \"yes\" or \"no\"")
        self.res_data.save()

def main():
    # Say proper greeting depending on what time of day!
    hour = get_hour()
    print(greeting(hour))
    # Choose a restaurant / Input a restaurant / Exit?
    action()

def get_hour():
    # Get Pacific time
    pacific = datetime.now(pytz.timezone('America/Los_Angeles'))
    # Isolate hour to integer
    hour = int(pacific.strftime('%H'))
    return hour

def greeting(hour):
    if hour < 12:
        return("Good morning!\n")
    elif hour < 18:
        return("Good afternoon!\n")
    else:
        return("Good evening!\n")

def action():
    while True:
        # Choose a restaurant / Input a restaurant / Exit?
        task = input('What would you like to do? \nA: Choose a restaurant \nB: Input a restaurant \nC: Exit\n')
        if task.capitalize() == 'A':
            pick()
            break
        elif task.capitalize() == 'B':
            lib_input = LibraryInput()
            lib_input.add_library()
            break
        elif task.capitalize() == 'C':
            print('Okay, goodbye! :)')
            break
        else:
            print('Try again, please enter \'A\' or \'B\' or \'C\'.')

def pick():
    res_data = RestaurantData()
    res_data.load()
    picked_cuisine = None
    print("Deep sigh~ Can't decide on what to eat again? Don't worry, I gotchu.")
    for c in res_data.get_all_cuisines():
        while True:
            print(f"How about {c}?")
            response = input("yes/no? ")
            if response.lower() == "yes":
                picked_cuisine = c
                break
            elif response.lower() == "no":
                print("No? Okay...")
                break
            else:
                print("Uh oh, that wasn't a real response. Try again! Say \"yes\" or \"no\"")
        if picked_cuisine is not None:
            break
    if picked_cuisine is None:
        print("THEN GO AHEAD AND STARVE!!")
        return
    else:
        # list of restaurants based on picked cuisine
        filtered_by_cuisine = res_data.filter_by_cuisine(picked_cuisine)
        # list of restaurants based on picked cuisine and current hour
        filtered_by_time_of_day = res_data.filter_by_time_of_day(filtered_by_cuisine, get_hour())
        if len(filtered_by_time_of_day) == 0:
            print(f"Sorry there are no restaurants for {picked_cuisine} during this time. Try again or try later!")
        else:
            # randomly selects one restaurant from filtered_by_time_of_day list
            restaurant = res_data.random_restaurant(filtered_by_time_of_day)
            print(f"Congratulations, you're eating at {restaurant}!")

if __name__ == "__main__":
    main()