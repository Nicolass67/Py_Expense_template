from PyInquirer import prompt
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user(*args):
    
    infos = prompt(user_questions)
    
    f = open("users.csv", "a")
    
    f.write(str(infos["name"]) + "\n")
    
    f.close

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("User Added !")
    # This function should create a new user, asking for its name
    return