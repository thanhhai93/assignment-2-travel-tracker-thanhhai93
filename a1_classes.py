"""
Name: NGUYEN THANH HAI
Date: 27/09/2020
Brief Project Description:
GitHub URL:https://github.com/JCUS-CP1404/assignment-1-travel-tracker-thanhhai93/blob/master/assignment1.py
"""

from place import Place
import csv

name = "places.csv"


def main():
    # MAIN FUNCTION - to call menu & function based on menu
    print("Travel Tracker 1.0 - by <Nguyen Thanh Hai>")
    print(readfile(), "Places loaded from places.csv")
    callmenu = menu()
    # VARIABLE FOR CALLING MENU #
    while callmenu != "Q":
        if callmenu == "L":
            open1()
            callmenu = menu()
        elif callmenu == "A".upper():
            add()
            callmenu = menu()
        elif callmenu == "M".upper():
            visitplace = readfile1()
            if visitplace>0:
                open1()
                visit()
                callmenu = menu()
            else:
                print("No Unvisited Place")
                callmenu = menu()
        else:
            print("Invalid menu choice")
            callmenu = menu()

    print(readfile(), "Places saved in places.csv")
    print("Have a nice day :) ")
    sortcsvfile()

def menu():
    # MENU FUNCTION - to display menu and input choice of menu
    menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit
>>>""").upper()
    return menuinput

def open1():
    # read&display csv function- open csv file and display
    import csv
    with open('places.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        datasort = sorted(reader, key=lambda row:(row[3],(int(row[2]))))
        count = 0
        row_count = sum(1 for row in datasort)
        row_count1 = 0
        for row in datasort:
            if row[3] == 'n':
                row_count1 = row_count1 + 1
            count= count + 1
            notvis = row[3].replace('n', '*').replace('v', ' ')
            #notvis is * / none to show visit / unvisited place
            print(notvis, '{:>1}'.format(count),'{:>0}'.format('.'), '{:<10}'.format(row[0]), "in", '{:<20}'.format(row[1]), "Priority",'{:<10}'.format(row[2]))
        if row_count1 == 0:
            print(row_count, "Places, No places left to visit. Why not add a new place?")
        else:
            print(row_count, "Places, you still want to visit", row_count1, "places")

    csvFile.close()

def add():
    # ADD FUNCTION - to append and add new line data in csv
    import csv
    while True:
        x = input("Name: ")
        #to input name of place
        if x.isalpha() or '':
            break
        print("Input can not be blankl")
    while True:
        y = input("Country: ")
        #to input name of country
        if y.isalpha() or '':
            break
        print("Input can not be blank")

    class NotPositiveError(UserWarning):
        pass

    while True:
        z = input("Priority: ")
        #to input priority
        try:
            number = int(z)
            if number <= 0:
                raise NotPositiveError
            break
        except ValueError:
            print("Invalid input; enter a valid number")
        except NotPositiveError:
            print("Number must be > 0")

    vn = "n"
    #vn = mark non-visited , n = mark visisted
    print(x, "in", y, ("Priority", z), "Has been added to travel tracker")
    newrow = [x, y, z, vn]
    #to make input to a list

    with open('places.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(newrow)
    csvFile.close()

def visit():
    # visit FUNCTION -to mark unvisited place to visited
    import csv
    with open('places.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        datasort = sorted(reader, key=lambda row: (row[3], (int(row[2]))))

    while True: #ERROR CHECKING
        try:
            x = int(input("Enter the number of a place to mark as visited"))
            if x > sum(1 for row in datasort):
                print("Invalid place number!")
                continue
            elif x <= 0:
                print("Number must be > 0")
                continue
        except ValueError:
            print("Invalid! Enter a valid number")
            continue
        else:
            break

    with open('places.csv', 'w', newline='') as csvFile1:
        writer = csv.writer(csvFile1)
        num = 0
        for row in datasort:
            num = num+1
            if num == x:
                if row[3] is "v":
                    print("Place is already visited")
                else:
                    row[3] = "v"
                    print(row[0], "in",row[1], "is visited")

            writer.writerow(row)

    csvFile.close()
    csvFile1.close()

def readfile():
    # COUNT LINES CSV FUNCTION - to sum lines in csv
    import csv
    with open('places.csv', 'r') as csvfile2:
        reader = csv.reader(csvfile2)
        row_count = sum(1 for row in reader)
    return row_count
    csvfile2.close()

def readfile1():
    # mark no unvisited place left function
    import csv
    with open('places.csv', 'r') as csvfile2:
        reader = csv.reader(csvfile2)
        visit = 0
        for row in reader:
            if row[3] == 'n':
                visit = visit + 1
            else:
                visit = visit
    csvfile2.close()
    return visit

def sortcsvfile():#        Function to sort csv file and write it to final places.csv          #
    import csv
    with open("places.csv", "r") as csvfile3:
        data = csv.reader(csvfile3)
        sortedlist = sorted(data, key=lambda row:(row[3], int(row[2])))
    with open("places.csv", "w", newline='') as f:
        fileWriter = csv.writer(f)
        for row in sortedlist:
            fileWriter.writerow(row)
    csvfile3.close()
    f.close()

main()

