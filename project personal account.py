"""
PROJECT DESCRIPTION

THIS PROJECT HELPS US KEEP ACCOUNT OF YOUR PERSONAL DATA
SIMPLY,YOU ENTER WEATHER ITS YOUR GAIN OR EXPENDITURE SPECIFING THE DATE, AMOUNT AND REASON 
LATER YOU MAY DISPLAY THE DATA OF YOU EXPENDITURE AND GAIN
"""

'''
BEFORE RUNNING THE PROGRAM MAKE SURE YOU HAVE personal.csv WITHIN THE SAME FOLDER
WHICH CAN BE DOWNLOADED FORM THE SAME REPOSITERY IN GITHUB
OR
TO CREATE personal.csv FILE:
1) GO TO FILE WHERE YOU ARE RUNNING THE CODE
2) CREATE A NEW FILE CALLED personal.csv
3) COPY AND PASTE THE FOLLOWING INTO THE .csv FILE'S 1ST LINE
 "t,date,amount,reason"

NOW YOU MAY RUN THE PROGRAM
'''

import csv
import sys

data = []


def main():
    global data
    data = []
    store_data()
    while True:
        try:
            choice = int(input("CHOOSE\n1)ADD DATA\n2)VIEW DATA\n3)EXIT\n"))
            if choice == 1:
                add_data()
            elif choice == 2:
                view_data()
            elif choice == 3:
                sys.exit(0)
            else:
                print("\nCHOOSE 1 ,2 OR 3\n")
                main()

        except ValueError:
            print("\nCHOOSE 1 ,2 OR 3\n")
            main()
        if "y" in input("DO YOU WANT TO CONTINUE?(y/n): "):
            main()
        else:
            sys.exit(0)


x = 0
date = ""


def add_data():
    try:
        global x, d
        choose = int(input("\n\n1)EXPENDITURE\n2)GAIN\n"))
        if choose == 1:
            type = "e"
        elif choose == 2:
            type = "g"
        else:
            print("CHOOSE EITHER 1 OR 2 ")
            add_data()
        if x == 1:
            date = d
            x = 0
        else:
            print("NOTE:   DATE SHOULD STRICTLY BE WRITTEN IN YYYY-MM-DD FORMAT SEPERATED BY ' - '): ")
            date = input("DATE: ")
        amount = input("AMOUNT: ")
        reason = input("REASON: ")
        with open("personal.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["t", "date", "amount", "reason"])
            writer.writerow(
                {"t": type, "date": date, "amount": amount, "reason": reason}
            )
        if "y" in input("DO YOU WANT TO ADD DATA ON SAME DAY?(y/n)): "):
            x = 1
            d = date
            add_data()
    except ValueError:
        print("CHOOSE EITHER 1 OR 2 ")
        add_data()


def store_data():
    with open("personal.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in sorted(reader, key=lambda x: x["date"]):
            data.append(row)


def initial_table(j):
    print("\n\n")
    if j == "e":
        print("EXPENDITURE TABLE:\n")
    else:
        print("GAIN TABLE:\n")

    print("DATE", end="")
    print_space(8)
    print("AMOUNT", end="")
    print_space(4)
    print("REASON")


eamount = 0
gamount = 0


def view_data():
    global eamount, gamount
    choose = input("VIEW DATA:\n1)MONTHLY\n2)ALL DATA\n")
    if choose == "1":
        x = int(input("WHICH MONTH (IN NUMBER): "))
    for j in ["e", "g"]:
        if choose == "1":
            initial_table(j)
            print_data(x, j)
        elif choose == "2":
            initial_table(j)
            for i in range(12):
                print_data(i + 1, j)
    print(f"\n\nTOTAL EXPENDITURE: {eamount}\nTOTAL GAIN: {gamount}\nYOU HAVE {gamount-eamount} LEFT\n")
    eamount = 0
    gamount = 0


def print_data(n, t):
    global eamount, gamount
    to = 0
    dat = ''
    for i in data:
        if n == int((i["date"].split("-"))[1]) and i["t"] == t:
            print(f"{i['date']}", end="")
            print_space(12 - len(i["date"]))
            print(f"{i['amount']}", end="")
            print_space(10 - len(i["amount"]))
            print(f"{i['reason']}")
            if t == "e":
                eamount += int(i["amount"])
                to += int(i["amount"])
            else:
                gamount += int(i["amount"])
            if dat != i["date"] and t == "e":
                print("-"*15,to,"-"*15)
                to = 0
            dat = i['date']


def print_space(n):
    for i in range(n):
        print(" ", end="")


if __name__ == "__main__":
    main()