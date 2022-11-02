from PyInquirer import prompt
import csv
import json

def show_status():
    
    f = open("expense_report.csv", "r")
    u = open("users.csv", 'r')
    
    myReaderU = csv.reader(u)
    users = []
    
    for elem in myReaderU:
        users.append(elem[0])

    myReader = csv.reader(f)

    line_number = 0        

    for row in myReader:
        participants = get_participants(line_number)

        spender = get_spender(line_number)
    
        price = get_price(line_number)
    
        doit_a = price/(len(participants) - 1)

        for elem in participants:
            if (elem != spender):
                print(elem + " doit " + str(doit_a) + " à " + spender)

        line_number += 1
        
    f.close
    
    return True

def get_participants(line_number):
    
    f = open("expense_report.csv", "r")

    myReader = csv.reader(f)

    participants = ""

    actual_line = 0

    for row in myReader:
        if (line_number == actual_line):
            participants += row[3]
        actual_line += 1
    
    participants_list = []
    for elem in participants.split("-"):
        participants_list.append(elem)
        

    f.close
    
    return participants_list

def get_spender(line_number):
    
    f = open("expense_report.csv", "r")

    myReader = csv.reader(f)

    spender = ""
    
    actual_line = 0

    for row in myReader:
        if (line_number == actual_line):
            spender += row[2]
        actual_line += 1

    f.close
    
    return spender


def get_price(line_number):
    
    f = open("expense_report.csv", "r")

    myReader = csv.reader(f)

    price = 0

    actual_line = 0

    for row in myReader:
        if (line_number == actual_line):
            price += int(row[0])
        actual_line += 1

    f.close
    
    return price