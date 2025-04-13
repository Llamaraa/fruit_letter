import time # importing time module for adding delays

def fruit_main():
        """
        ask user to input a fruit name and print the corresponding letter based on list index
        """
        print("Welcome! Type in a fruit name, and the program will tell you which letter it corresponds to in a pre-defined list.")
        print("Type in a fruit name here:")

        fruit_input = input().lower() # get user input and convert to lowercase for consistency


        fruits = ["apple", "banana", "grapes", "pear"] # predefined list of fruits
        
        # check if input is in list
        if fruit_input in fruits:
                index = fruits.index(fruit_input) # find index of fruit
                letter = chr (97 + index) # convert index to letter (97 is ASCII for 'a')
                print(f"The fruit '{fruit_input}' corresponds with letter '{letter}' .")
        else:
                # if fruit is not found, prompt user to try again
                print("Fruit not in list. Please try again.")

def fruit_retry():
    """
    keep running fruit_main() until user decides to quit
    """
        while True:
                fruit_main() # run main fruit lookup program
                user_input = input("Do you want to try again? (y/n/):").lower() # get user choice to continue or quit

                if user_input == 'n':
                        print("Quitting...")
                        time.sleep(5) # wait 5 seconds before quitting
                        break
                elif user_input != 'y':
                        print("Invalid input, type 'y' or 'n' to continue.") # show error if user input is not 'y' or 'n'
                        
# start retry loop
fruit_retry()
                        
