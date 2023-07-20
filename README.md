# Restaurant Picker
    #### Video Demo:  https://youtu.be/MGYv0nYesbA
    #### Description:
This script helps users choose a restaurant to eat at based on cuisine and time of day. It allows users to add restaurants to a list and filter the list based on cuisine and time of day to find a random restaurant to eat at.

## Background

My project is for anyone who is indecisive on where to eat. I often find myself hungry and uncertain of what I want to eat in the moment. Hours and hours will go by without a decision made and therefore furthering my hunger and frustration. I personally have at times resorted to not eating at all due my severe indecision. This program was created to help anyone make a decision and mitigate time wasted on making that decision by outputting a random restaurant based on a series of parameters.

## Challenges

What started off as a simple concept quickly evolved into a much more complex idea. I was afraid that inputting and outputting a restaurant name would not be sufficient as final project. The initial draft included the option to cook at home, so the program would have also included inputting recipes and outputting recipes. I also considered inputting the hours of operation for each restaurant, so that if they were closed during the time of picking then those restaurants would be filtered out. It was only when I began to code that I realized that what I thought was a simple function of outputting a random restaurant required more code than I originally intended. I ran into many “what if” scenarios in my head that altered how the program would run. For example: What if I accidentally meant to respond “no” instead of “yes”? Would I have to run the program all over again? Would I lose all the data that I inputted for a restaurant? How do I resolve this issue? I was surprised to find that even running one function required an extra week of just troubleshooting minor details. And so before I knew it, my very simple idea became a lengthy but very detailed code. Something I learned from my design background is that it’s very difficult to know when to stop designing because everything can always be better. Once I had spent significant time and effort on the foundation of my code I realized I had my final project. I feel proud of what I have produced and I hope you will too.

## Dependencies

This script requires the following libraries:
- `datetime`: for handling the current time
- `pytz`: for handling time zones
- `pathlib`: for handling file paths
- `json`: for reading and writing to a JSON file
- `random`: for picking a random restaurant

## Data Storage

The list of restaurants is stored in a JSON file called RList.json. The program loads the data from this file when it starts, and saves any updates to the file when a new restaurant is added or the program exits.

## Classes

The script contains two main classes: `RestaurantData` and `LibraryInput`.

### RestaurantData

This class contains methods for handling the list of restaurants, including:
- `load`: loads the list of restaurants from a JSON file
- `save`: saves the list of restaurants to a JSON file
- `get_all_cuisines`: returns a list of all the unique cuisines in the list of restaurants
- `filter_by_cuisine`: returns a list of restaurants with a given cuisine
- `filter_by_time_of_day`: returns a list of restaurants that are open at a given time of day
- `random_restaurant`: returns a random restaurant from a given list
- `add_restaurant`: adds a new restaurant to the list of restaurants

### LibraryInput

This class contains methods for handling user input and interacting with the `RestaurantData` class, including:
- `input_restaurant`: prompts the user to input a new restaurant and adds it to the list of restaurants
- `get_name`: prompts the user to input a name for the new restaurant
- `get_cuisines`: prompts the user to input the cuisine(s) of the new restaurant
- `get_times`: prompts the user to input the time(s) of day that the new restaurant is open

## Usage

To get started on running the program, simply execute python project.py in the terminal window. Follow the prompts to pick a random restaurant, add a new restaurant to the list of restaurants to choose from later, or to exit the program. To use the script, create an instance of the `LibraryInput` class and call the `input_restaurant` method. This will prompt the user to input a new restaurant and add it to the list of restaurants. The list of restaurants can then be filtered by cuisine and time of day using the `filter_by_cuisine` and `filter_by_time_of_day` methods of the `RestaurantData` class, and a random restaurant can be chosen from the filtered list using the `random_restaurant` method.
