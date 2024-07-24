"""
PROJECT DESCRIPTION

THIS PROJECT HELPS US KEEP THE DATA OF PEOPLE STAYING IN YOUR HOME IN RENT
SIMPLY, YOU SPECIFY ROOM NO TO EACH OF THE ROOM IN YOUR HOME
AND GIVE DATA OF THE PAYMENTS MADE,
LATER YOU MAY DISPLAY THE DATA OF PAYMENT
"""

"""
BEFORE RUNNING THE PROGRAM MAKE SURE YOU HAVE data_account.csv
WHICH CAN BE DOWNLOADED FORM THE SAME REPOSITERY IN GITHUB
OR

TO CREATE A .csv FILE:
1) GO TO FILE WHERE YOU ARE RUNNING THE CODE
2) CREATE A NEW FILE CALLED data_account.csv
3) COPY AND PASTE THE FOLLOWING INTO THE .csv FILE'S 1ST LINE
 " room_no,name,date,amount,reason "

NOW YOU MAY RUN THE PROGRAM
"""

import csv
import sys

data = []
room = []


def main():
    while True:
        try:
            choice = int(input("CHOOSE:\n1)VIEW DATA\n2)ADD DATA\n3)EXIT\n"))
            if choice == 1:
                view_data()
            elif choice == 2:
                add_data()

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
    with open("data_account.csv", "r") as file:
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


def add_data():
    x = 0
    Room_no = input("ROOM NUMBER: ")
    for i in data:
        if Room_no == i["room_no"]:
            name = i["name"]
            date = input("DATE: ")
            amount = input("AMOUNT: ")
            reason = input("REASON: ")
            x = 1

    if x != 1:
        name = input("NAME: ")
        date = input("DATE: ")
        amount = input("AMOUNT: ")
        reason = input("REASON: ")

    with open("data_account.csv", "a") as file:
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

    return Room_no


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
        print("ROOM NUMBER INVALID")
        print("CHOOSE AMONG ROOM NO: ", end="")
        for i in room:
            print(f"\t{i}", end="")
        view_data()


def print_space(n):
    for _ in range(n):
        print(" ", end="")


def store_room():
    for i in data:
        if i["room_no"] not in room:
            room.append(i["room_no"])


if __name__ == "__main__":
    store_data()
    store_room()
    main()
