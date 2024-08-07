"""
PROJECT DESCRIPTION

THIS PROJECT HELPS US KEEP THE DATA OF PEOPLE STAYING IN YOUR HOME IN RENT
SIMPLY, YOU SPECIFY ROOM NO TO EACH OF THE ROOM IN YOUR HOME
AND GIVE DATA OF THE PAYMENTS MADE,
LATER YOU MAY DISPLAY THE DATA OF PAYMENTS MADE
"""

'''
BEFORE RUNNING THE PROGRAM MAKE SURE YOU HAVE data.csv WITHIN THE SAME FOLDER
WHICH CAN BE DOWNLOADED FORM THE SAME REPOSITERY IN GITHUB
OR
TO CREATE data_account.csv FILE:
1) GO TO FILE WHERE YOU ARE RUNNING THE CODE
2) CREATE A NEW FILE CALLED data.csv
3) COPY AND PASTE THE FOLLOWING INTO THE .csv FILE'S 1ST LINE
 " room_no,name,date,amount,reason "

NOW YOU MAY RUN THE PROGRAM
'''

import csv
import sys

data = []
room = []


def main():
    global data
    global room
    data = []
    room = []
    store_data()
    store_room()
    while True:
        try:
            choice = int(input("CHOOSE:\n1)VIEW DATA\n2)ADD DATA\n3)EXIT\n"))
            if choice == 1:
                view_data()
            elif choice == 2:
                Room_no = input("ROOM NUMBER: ")
                add_data(Room_no)

            elif choice == 3:
                sys.exit(0)
            else:
                print("\nChoose between 1 or 2 or 3\n")
                main()

        except ValueError:
            print("\nChoose between 1 or 2 or 3\n")
            main()

        if "y" in input("DO YOU WANT TO CONTINUE?(y/n)").lower():
            main()
        else:
            sys.exit(0)


def store_data():
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(
                {
                    "room_no": row["room_no"].strip(),
                    "name": row["name"].strip(),
                    "date": row["date"].strip(),
                    "amount": row["amount"].strip(),
                    "reason": row["reason"].strip(),
                }
            )


def add_data(Room_no):
    x = 0
    for i in data:
        if Room_no == i["room_no"]:
            name = i["name"]
            date = input("DATE: ")
            amount = input("AMOUNT: ")
            reason = input("REASON: ")
            x = 1
            break

    if x != 1:
        name = input("NAME: ")
        date = input("DATE: ")
        amount = input("AMOUNT: ")
        reason = input("REASON: ")

    with open("data.csv", "a") as file:
        writer = csv.DictWriter(
            file, fieldnames=["room_no", "name", "date", "amount", "reason"]
        )
        writer.writerow(
            {
                "room_no": Room_no,
                "name": name,
                "date": date,
                "amount": amount,
                "reason": reason,
            }
        )



def view_data():
    Room_no = input("\nROOM NUMBER: ")
    print_data(Room_no)


def print_data(r):
    x = 0
    name = ""
    for j in data:
        if r == j["room_no"]:
            x = 1
            name = j["name"]
            break

    if x == 1:
        print(f"Owner Name: {name}")
        print("DATE   ", end="")
        print_space(7)
        print("AMOUNT", end="")
        print_space(8)
        print("REASON", end="")
        print("\n", end="")
        for i in data:
            if r == i["room_no"]:
                print(i["date"].strip(), end="")
                print_space(14 - len(i["date"]))
                print(i["amount"].strip(), end="")
                print_space(14 - len(i["amount"]))
                print(i["reason"].strip())
    else:
        if room == []:
            print(f"\nDATA OF ROOM NUMBER {r} IS NOT SAVED")
        else:
            print(f"WE HAVE NO DATA OF ROOM NUMBER {r}")
            print("CHOOSE AMONG ROOM NO: ", end="")
            for i in room:
                print(f"\t{i}", end="")
            print("\nOR")
        print(f"DO YOU WANT TO ADD DATA FOR ROOM NUMBER {r}")
        if room == []:
            while True:
                choice = input("(y/n) :").lower()
                if 'y' in choice:
                    add_data(r)
                    break
                elif 'n' in choice:
                    break
        else:
            while True:
                choice = input("(choose/add) :").lower()
                if 'add' in choice:
                    add_data(r)
                    break
                elif 'choose' in choice:
                    view_data()
                    break



def print_space(n):
    for _ in range(n):
        print(" ", end="")


def store_room():
    for i in data:
        if i["room_no"] not in room:
            room.append(i["room_no"])


if __name__ == "__main__":
    main()

