
# =====importing libraries===========
# import datetime
from datetime import datetime
index = 0

# =========== Functions ===========
def check_user(username):
    read_file = open('user.txt', 'r')  #open file
    for line in read_file:  #for loop and split line for readability
        user = line.split(", ")
        if username == user[0]:
            return True
    read_file.close()  #close file
    return False

def edit_task(task_dict):
        Task_id_input = int(input("\nEnter Task ID :(Edit Task or Change Task Status) or ('-1')for main menu  : "))
        
        if task_dict[Task_id_input]["Task Assigned to"] != username_input:
            print("\nAccess denied, Task does not belong to current user")
            return

        if Task_id_input in task_dict.keys():
            edit_choice = input("Enter 'e' - Edit User Task or Enter 's' - Change Task Status : ")

            # change status of task specified 
            if edit_choice == 's':
                staus_edit = input("The Task is currently not complete, Would you like to Mark as complete ('Yes' or 'No') : ")

                if staus_edit == 'Yes': # user enters 'yes' status changes to 'yes'
                    task_dict[Task_id_input]["Task complete/status"] = staus_edit
                    print('Task Staus has been changed to Complete')
                    update_tasks(task_dict)
                    
                else:
                    print("Task Staus not Changed")
                                                
            # user selects 'e' then they will be allowed to edit task
            elif edit_choice == 'e':
                edit_task = input('Enter option to edit : \n"D" (Due Date) \n"UA" (User Assigned Task) : ')
                # user wants to change  due date of the task
                if edit_task == 'D':
                    task_due_date_edit = input("Enter the new due date dd/mm/yyyy for the task: ")
                    task_dict[Task_id_input]["Task Due date"] = task_due_date_edit
                    print('Task due date has been changed to Complete')
                    update_tasks(task_dict)

                # user wants to change the name of user assigned 
                elif edit_task == 'UA':
                    user_task_assigned_edit = input("Enter the Username Of the person you want to be assigned to task.") 
                    task_dict[Task_id_input]["Task Assigned to"] = user_task_assigned_edit
                    print('User assigned to task has been changed')
                    update_tasks(task_dict)

        else: # user enters -1 they will go back to main menu
            print('Returning back to main menu') 

def update_tasks(task_dict):
    task_file = open('tasks.txt', 'w')
    for task in task_dict.values():
        print(task.items())
        for key, value in task.items():
            print("val: "+value)

            if key == "Task complete/status":
                task_file.write(value.strip())

            else: 
                task_file.write(value + ", ")
        task_file.write("\n")
    task_file.close()

def generate_report():
    with open("tasks.txt", 'r') as e:
        count_overdue = 0  # counts number of tasks that are over-due
        count_no = 0  # ccounts number of tasks that are not complete
        count_yes = 0 # counts number of tasks that are complete
        task_dict = {} # empty dictionary 
        i = 1  # count for each task 
        for line in e: # for loop goes over every line in text creating a dict
            listDetails = line.strip().split(', ')
            task_dict[i] = {"user_task_assigned": listDetails[0]}
            task_dict[i].update({"task_title": listDetails[1]})
            task_dict[i].update({"task_description": listDetails[2]})
            task_dict[i].update({"task_assigned_date": listDetails[3]})
            task_dict[i].update({"task_due_date": listDetails[4]})
            task_dict[i].update({"task_status": listDetails[5]})
            i+=1

            # total number of tasks
            Number_of_tasks = len(task_dict)
            
            # total number of tasks completed 
            completed_tasks = listDetails[5] == "Yes" 
            if completed_tasks == True: # if true task meets conditions 
                count_yes += 1 # counting completed tasks
           
            # tasks not completed 
            not_completed_tasks = listDetails[5] == "No"
            if not_completed_tasks == True:  # if true task meets conditions   
                count_no += 1  # counting number of incomplete tasks 

             # the total number of tasks that are incomplete and overdue  
            due_date_convert = datetime.strptime(listDetails[4], '%d/%m/%Y') # converts due dates 
            current_date = datetime.today().strftime('%d/%m/%Y') # calculates current date 
            curr_date = datetime.strptime(current_date, '%d/%m/%Y') # converts current date 

            overdue_tasks = listDetails[5] == "No" and due_date_convert < curr_date 
            if overdue_tasks == True: # overdue = true task meets conditions 
                count_overdue += 1
                
            
            # the percentage of tasks incomplete
            percent_incompleted = ((count_no / Number_of_tasks) * 100 )

            # percentage of tasks overdue
            percent_overdue = ((count_overdue / Number_of_tasks) * 100 )

        # print statements for info calculated
        print("Task Overview report on all tasks below: \n")
        print("Number of tasks Created                       : " + str(Number_of_tasks))
        print("Number of tasks not completed                 : " + str(count_no))
        print("Number of tasks completed                     : " + str(count_yes))        
        print("Number of tasks overdue                       : " + str(count_overdue))
        print("Percentage of tasks that are incomplete (%)   : " + str(int(percent_incompleted)))
        print("Percentage of tasks overdue/not completed (%) : " + str(int(percent_overdue)))

        with open("task_overview.txt", 'w') as gr:
            gr.write("Please report on all tasks below: ")
            gr.write("\nNumber of tasks Created                       : " + str(Number_of_tasks))
            gr.write("\nNumber of tasks not completed                 : " + str(count_no))
            gr.write("\nNumber of tasks completed                     : " + str(count_yes))
            gr.write("\nNumber of tasks overdue                       : " + str(count_overdue))
            gr.write("\nPercentage of tasks that are incomplete (%)   : " + str(int(percent_incompleted)))
            gr.write("\nPercentage of tasks overdue/not completed (%) : " + str(int(percent_overdue)))

        gr.close() # close file 

    (user(task_dict)) # call next function 
    
    e.close() #close file

def user(task_dict):
    #  print stats for user and the task assigned to them 
    print('\n')
    print("User Overview report on all tasks below: \n")
    with open('User.txt', 'r') as Userfile: 
        user_dict = {}  # empty dictionary 
        u = 1   # count for each task
        user_data_report = ""
        
        for line in Userfile:  
            userlistDetails = line.strip().split(', ')
            user_dict[u] = {"username": userlistDetails[0]}
            user_dict[u].update({"password": userlistDetails[1]})
            u+= 1
            
            # list of variables 
            total_tasks = len(task_dict)
            total_users = len(user_dict)
            user_task_count = 0
            complete_count = 0
            not_complete_count = 0
            not_complete_overdue = 0
            percent_not_complete = 0
            percent_overdue_notcomplete = 0
                            
            # loop that runs through task_dict values and stores them in 'task'
            for task in task_dict.values():
                # importing the current data and the task due dates and converting to 1 format
                today = datetime.today().strftime('%d/%m/%Y') 
                curr_date = datetime.strptime(today, '%d/%m/%Y')
                due_date_convert = datetime.strptime(task["task_due_date"], '%d/%m/%Y') 

                if task["user_task_assigned"] == userlistDetails[0]:
                    user_task_count += 1
                    if user_task_count != 0:  # if task count is greater than 0
                        if task["task_status"].lower() == "yes":
                            complete_count += 1
                        if task["task_status"].lower() == "no":
                            not_complete_count += 1        
                        if task["task_status"].lower() == "no" and curr_date > due_date_convert: 
                            not_complete_overdue += 1        
                    else: 
                        percent_not_complete = 0
                        percent_overdue_notcomplete = 0
                        percent_complete_count = 0

            # formulas calculate user and task statistics                  
            total_percent = int((user_task_count/total_tasks) * 100)    
            if complete_count < 1: 
                percent_complete_count = 0
            else: 
                percent_not_complete = int((not_complete_count / user_task_count) * 100)

            
            if not_complete_overdue < 1: 
                percent_overdue_notcomplete = 0
            else: 
                percent_overdue_notcomplete = int((not_complete_overdue / user_task_count) * 100)
                       
            # print out all data for user on screen 
            print("\n" + (userlistDetails[0].upper()))  # print list of users
            print(" Number of tasks assigned:  " + str(user_task_count))  # number of tasks assigned to each user
            print(" Percentage of total tasks assigned to each user: " + str(total_percent) + "%")
            print(" Percentage of tast that is completed: " + str( percent_complete_count)+ "%")
            print(" Percentage of tast that must still be completed: " + str(percent_not_complete) + "%")
            print(" Percentage of tasks not complete and overdue: " + str(percent_overdue_notcomplete) + "%")

            user_data_report += ("\n" + (userlistDetails[0].upper())
                     +("\nNumber of tasks assigned:  " + str(user_task_count))
                     +("\nPercentage of total tasks assigned to each user: " + str(total_percent) + "%")
                     +("\nPercentage of tast that is completed: " + str( percent_complete_count)+ "%")
                     +("\nPercentage of tast that must still be completed: " + str(percent_not_complete) + "%")
                     +("\nPercentage of tasks not complete and overdue: " + str(percent_overdue_notcomplete) + "%")
                     +("\n")
                      )

        print("\nTotal number Of task created  : " + str(total_tasks))
        print("Total number Of users created : " + str(total_users))

        with open("user_overview.txt", 'w') as uo:  # open file
            uo.write(user_data_report)
            uo.write(("\nTotal number Of task created  : " + str(total_tasks)))
            uo.write("\nTotal number Of users created : " + str(total_users))
                                
        uo.close()  # close file 
        
    Userfile.close()  # close file

def reg_user():
    if username_input == "admin":  # if user is admin allow for registration of new user
            UserfileAdd = open('user.txt', 'a')  # open file
            new_username = str(input("Please create a new username: "))  # input username
            new_password = str(input("Please enter a new password: "))  # input password
            confirm_password = str(input("Please confirm password: "))  # confirm password

            user_exists = check_user(new_username)
            while user_exists == True:
                print("Username already exists. Please enter a different username.\n")
                new_username = str(input("Please create a new username: "))  # input username
                new_password = str(input("Please enter a new password: "))  # input password
                confirm_password = str(input("Please confirm password: "))  # confirm password
                user_exists = check_user(new_username)

            while new_password != confirm_password:  # if passwords do not match, re-enter info
                print("Passwords do not match!")
                new_password = str(input("Please enter a new password: "))
                confirm_password = str(input("Please confirm password: "))

            if new_password == confirm_password:  # if everything entered is correct, write in file
                print("Registration Complete!")
                UserfileAdd.write("\n" + new_username + ", " + new_password)
            UserfileAdd.close()  # close file
    else : 
        print("\nError: You dont have permission to add a user!")

def add_task():
    add_task = open('tasks.txt', 'a')  # open file and request inputs
    assign_username = str(
        input("Enter the username the task will be assigned to: "))  
    task_title = str(input("Enter the title of the task: "))
    task_description = str(input("Enter a description of the task: "))
    task_due = str(input("Enter the task due date: "))
    current_date = datetime.today()  #.strftime('%d/%m/%Y')
    task_completion = "No"

    add_task.write("\n" + assign_username + ", ")  # write all inputs into file
    add_task.write(task_title + ", ")
    add_task.write(task_description + ", ")
    add_task.write(task_due + ", ")
    add_task.write(current_date + ", ")
    add_task.write(task_completion)

    print("\nYour task has been added, to view please select option 'va' or 'vm' ")  # once all inputs are entered, print
    add_task.close()  # close file

def view_all():
    read_file = open('tasks.txt', 'r')  #open file
    for line in read_file:  #for loop file and split line for readability
            r_assign_username, r_task_title, r_task_description, r_task_due,  r_current_date,  r_task_completion = line.split(
                ", ")
            print("\n")
            print("Task: " + r_task_title)
            print("Assigned to: " + r_assign_username)
            print("Date assigned: " + r_current_date)
            print("Due date: " + r_task_due)
            print("Task description: " + r_task_description)
            print("Task complete?: " + r_task_completion)
    read_file.close()  #close file

def view_mine():
    user_task_dict = {} # empty Dictionary
    record_keys = 1

    user_file = open('tasks.txt', 'r+')  # open file
    #  Track if any records were found
    foundRecord = False

    for line in user_file:
        u_assign_username, u_task_title, u_task_description, u_task_due,  u_current_date,  u_task_completion = line.split(", ")  #loop over lines and split
        # if u_assign_username == username_input:   
        # foundRecord = True
        user_task_dict[record_keys] = {"Task Assigned to": u_assign_username , "Task title": u_task_title, "Task description": u_task_description,
        "Task Date assigned": u_current_date, "Task Due date": u_task_due, "Task complete/status": u_task_completion}
        record_keys = record_keys + 1


    # loop over dict items 
    for task_id, task_info in user_task_dict.items():
        if task_info["Task Assigned to"] == username_input: 
            foundRecord = True
            print("\nTask ID:", task_id)

            for task_key in task_info:
                print(task_key + ':', task_info[task_key])

    if foundRecord == False:
            print("No tasks for user.")
    else : 
        edit_task(user_task_dict)

    user_file.close()  # close file

# ====Login Section====
# Part 1 validate the user

is_authenticated = False

while is_authenticated == False:
    username_input = str(input("Please enter username: ")).strip()  # input username and strip spaces
    password_input = str(input("Please enter password: ")).strip()  # input password and strip spaces
    with open("user.txt") as f:  # open file
        userinputFile = f.readlines()

    for line in userinputFile:  # loop over users and passwords
        username, password = line.split(", ")  # split line into username and password seperate with ,
        if username == username_input and password.strip() == password_input:  # if username and password IS found
            is_authenticated = True
            print("Welcome " + username_input +
                  " you have succssfully logged in! \n")
            break

    if is_authenticated == False:  # if username and password not found
        print("\nIncorrect details please try again\n")
    f.close()  # close file

# ====Logged in Section====

while is_authenticated == True:
    # check if user is admin, if so add extra menu item 
    if username_input == "admin":  # if user is admin they get 's' option
        menu = input('''\nSelect one of the following Options below:
                r - Registering a user
                a - Adding a task
                va - View all tasks
                vm - view my task
                gr - generate reports
                ds - display statistics
                e - Exit 
            ''')
    else:        
        menu = input('''\nSelect one of the following Options below:
                r - Registering a user
                a - Adding a task
                va - View all tasks
                vm - view my task
                e - Exit 
            ''')

    if menu == 'r':
        pass
        reg_user()

    elif menu == 'a':
        pass
        add_task()

    elif menu == 'va':
        pass
        view_all()

    elif menu == 'vm':
        pass
        view_mine()

    elif menu == 'ds' and username_input == "admin" :
            s = open('tasks.txt', 'r') # opens txt file in read only 
            print("\nNumber of Tasks Created:")
            number_of_tasks = len(s.readlines(  )) # counts the number of lines in the txt file,
            print(str(number_of_tasks) + " Tasks created")

            u = open('User.txt', 'r') # opens txt file in read only 
            print("\nNumber Of Users Registered : ")
            number_of_users = len(u.readlines(  )) # counts the number of lines in the txt file,
            print(str(number_of_users) + " users registered")

            print("\n")
            generate_report()
            
            s.close()  # close files
            u.close()
    
    elif menu == "gr" and username_input == "admin": # view stats
        generate_report()

    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
