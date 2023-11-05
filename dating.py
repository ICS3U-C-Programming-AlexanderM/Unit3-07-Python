#!/usr/bin/env python3
# Created By: Alex M
# Date: Oct 19, 2023
# This program checks if user can date my grand daughter 
def main():
    # get age from user
    print("Enter your age ")
    user_age_as_str = input("")
    # convert str to an int. if its not an integer
    try:
        user_age = int(user_age_as_str)
    except ValueError:
        print (f"{user_age_as_str} is not a valid age ")
        print("")
    else: 
        if user_age < 0:
            print(f"{user_age} is not a valid age ")
        else:
            if user_age < 40 and user_age >25:
                print(" YOU CAN DATE MY DAUGHTER. treat her well!!")
            elif user_age >40 :
                print("YOU ARE TOO OLD TO DATE MY DAUGHTER ")
            elif user_age < 25 :
                print("you are too young to date my daughter")
    finally:
        print("thankyou for trying :) !!!")


if __name__ == "__main__":
    main()
    