from datetime import datetime
task_db = []
user_db = []
is_login = None
user_id = 0
task_id = 0

def create_task(title, description, duration, user_id):
    global task_id
    task_id += 1
    task = {
        "task_id": task_id,
        "title": title,
        "description": description,
        "duration": duration,
        "status": False,
        "user_id":  user_id,
        "created_at": datetime.now()
    }
    task_db.append(task)

def read_task(task_id,user_id):
    for i in task_db:
        if i["task_id"] == task_id and i["user_id"] == user_id:
            return f"""
Your task {i["task_id"]}:
Title: {i["title"]}
Description: {i["description"]}
Duration: {i["duration"]}
Status: {i["status"]}
"""
    else:
        return False
    
def update_task(task_id, title, descp, due, status, user_id):
    for i in task_db:
        if i["task_id"] == task_id and i["user_id"] == user_id:
            if title:
                i["title"] = title
            if descp:
                i["description"] = descp
            if due:
                i["duration"] = due
            if status:
                i["status"] = status
            return True

def delete_task(task_id, user_id):
    for i in task_db:
        if i["task_id"] == task_id and i["user_id"] == user_id:
            task_db.remove(i)
            return True
    else:
        return False

def regist(username, password):
    global user_id, is_login
    user_id+=1
    user = {
        "user_id": user_id,
        "username": username,
        "password": password,
        "create_at": datetime.now()
    }
    user_db.append(user)
    is_login = user

def login(username, password):
    global is_login
    for i in user_db:
        if i["username"] == username and i["password"] == password:
            is_login = i
            return True
    else:
        return False

def change_password(old_password, new_password):
    if is_login["password"] == old_password:
        is_login["password"] = new_password
        return True
    else:
        return False

while True:
    if is_login == None:
         n = int(input(
                "1) Registration\n"
                "2) Login\n"
                "0) Exit\n"
                "Choose one: "
            ))
         match n:
            case 1:
                username = input("Username: ")
                password = input("Password: ")
                regist(username, password)
            case 2:
                username = input("Username: ")
                password = input("Password: ")
                if login(username, password):
                    print("Login successful")
                else:
                    print("Wrong username or password")
            case 0:
                 print("Good bye")
                 break

    else:
        n = int(input(
        "1) Create Task\n"
        "2) Read Task\n"
        "3) Update Task\n"
        "4) Delete\n"
        "5) Change Password\n"
        "0) Exit\n"
        "Choose one: "
    ))
        match n:
            case 1:
                print("Start create task")
                name_user = input("User name: ")
                title = input("Title: ")
                descp = input("Description: ")
                durat = input("Duration: ")
                create_task(title, descp, durat, is_login["user_id"])
                print("Task created !!")
            case 2:
                k = int(input("Enter id task: "))
                print(read_task(k,is_login["user_id"]))
            case 3:
                print("Start update task:")
                k = int(input("Enter id task: "))
                if read_task(k,is_login["user_id"]):
                    name_user = input("User name: ")
                    title = input("Title or put enter for continue: ")
                    descp = input("Description or put enter for continue: ")
                    durat = input("Duration or put enter for continue: ")
                    status = bool(input("Status or put enter for continue: "))
                    update_task(k, title, descp, durat, status,is_login["user_id"])
                    print("Task updated !!")
                else:
                    print("This task denied")
            case 4:
                k = int(input("Enter id task: "))
                if delete_task(k,is_login["user_id"]):
                    print("Your task deleted")
                else:
                    print("This task denied")
            case 5:
                old_password = input("Old password: ")
                new_password = input("New password: ")
                if change_password(old_password, new_password):
                    print("Password changed successfully")
                else:
                    print("Wrong old password")
            case 0:
                print("Exit")
                break
            case _:
                print("Invalid input")
