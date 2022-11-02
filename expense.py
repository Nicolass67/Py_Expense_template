from PyInquirer import prompt
import csv
import json

def get_participants_list(answers):
    
    f = open("users.csv","r")
    
    myReader = csv.reader(f)
    
    participants = []

    for row in myReader:
        participants.append(str(row).replace("[","").replace("]","").replace("\'",""))
    
    return participants

def get_spender_list(answers):
    
    f = open("users.csv","r")
    
    myReader = csv.reader(f)
    
    spender = []

    for row in myReader:
        spender.append({'name': str(row)})
    
    return spender

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"Expense Tracker v0.1",
        "choices":get_participants_list,
    },
    {
        "type":"checkbox",
        "name":"participants",
        "message":"Expense Tracker v0.1",
        "choices": get_spender_list,
    },

]

def new_expense(*args):
    infos = prompt(expense_questions)
    
    f = open("expense_report.csv", "a")
    
    participants = ""
    
    for participant in infos["participants"]:
        print(participant)
        participants += str(participant).replace("[","").replace("]","").replace("\'","")
        participants += "-"
        
    str_participants = str(participants)
    
    if not infos["spender"] in str_participants:
        str_participants +=  infos["spender"] + "-"
    
    f.write(str(infos["amount"]) + "," + str(infos["label"]) + "," + str(infos["spender"]) + "," + str_participants[:len(str_participants)-1] + "\n")
    
    f.close

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True


