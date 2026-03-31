#we import the library json and call the os
import json
import os

#here is the variable with the name of the file
carpeta_data = 'data'
#here we join two components to create a path
DATA = os.path.join(carpeta_data, 'database.json')

#here is an function that checks if the file exists , if not it creates it
def create_file_if_doesnt_exist():
    if not os.path.exists(carpeta_data):
        os.makedirs(carpeta_data)

#-----PERSISTENCE FUNCTIONS---------

#in this function we write the json archive
def add_to_json(students_list):
    create_file_if_doesnt_exist()
    with open(DATA, 'w', encoding='utf-8') as archive:
        json.dump(students_list, archive, indent=4, ensure_ascii=False)

#here we bring all the information in the json archive to the list in main
def charge_from_json(students_list):
    if not os.path.exists(DATA):
        return []
    try:
        with open(DATA, 'r', encoding='utf-8') as archive:
            data_json = json.load(archive)
            for student in data_json:
                students_list.append(student)
    except json.JSONDecodeError:
        print('\nThere was something wrong')


#-----APP FUNCTIONS-----------
#here the function menu to print the menu is defined
def menu():
    
    #here inside is the string value to print, it's the menu
    menu_print = """

---Wellcome to the system---

1. Register a new student
2. Show the students
3. Consult some student
4. Update a student's information
5. Delete a student
6. Go out
"""
    print(menu_print)

#here is defined the function for add new students
def add_new_student(students_list):
    
    #these are variables that will be used for break the while loops
    first_while_breaker= 0
    second_while_breaker= 0
    third_while_breaker = 0
    fourth_while_breaker = 0
    fifth_while_breaker = 0
    
    #first while loop used for repeat if the data typed is wrong
    while first_while_breaker != 1:
        
        #a flag to check existence
        exist = False
        
        #the input asking for the ID
        ID_student = input('\nWrite an ID of 4 digits for the student: ')

        #here we are checking if ID exists already and if its len is 4 as we ask for
        for i in students_list:
            if ID_student == i['id']:
                exist = True
                break
        if exist:
            print('\nThe ID is already used')
        elif not ID_student.isdigit():
            print('\nYou can only write numbers here')
        elif len(ID_student) != 4:
            print('\nOnly has to be 4 digits')
        else:
            #if the other situations are not, we break the loop
            first_while_breaker = 1
    
    #this is the second while loop for the name
    while second_while_breaker != 1:

        name_student = input('\nWrite the name of the student: ').strip().replace(" ","_").lower()
        
        #here we use a flag to check existence of numbers and a for to go through the name
        #and check if there's a number
        numbersearcher = False
        for i in name_student:
            if i.isdigit():
                numbersearcher = True
        if numbersearcher == True:
            print("\nThe name can't have numbers")
        else:
            #if the other situations are not, we break the loop
            second_while_breaker = 1
    
    #this is the third while loop for the age
    while third_while_breaker != 1:
        #we use try and except to catch the errors
        try:
            age_student = int(input('\nWrite the age of student: '))
            
            #we say if the age is less than 3 is too young
            if age_student <= 3:
                print("\nWith that age the student can't be at the institution")
            else:
                #if the other situations are not, we break the loop
                third_while_breaker = 1
        except:
            print('\nThe data is invalid')
    
    #this is the fourth while loop
    while fourth_while_breaker != 1:
        #the levels that exist
        grades = """
The levels are:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
"""
        print (grades)

        #Here we ask for the level
        grade_student = input("\nWrite the level of the student: ")

        #then, we create a comparation if the options are right
        if grade_student == '1' or grade_student == '2' or grade_student == '3' or grade_student == '4' or grade_student == '5' or grade_student == '6' or grade_student == '7' or grade_student == '8' or grade_student == '9' or grade_student == '10' or grade_student == '11':
            fourth_while_breaker = 1
        else:
            print("\nThe level doesn't exist")
    
     #the fourth while loop to check if the option are active or inactive and assign the status
    while fifth_while_breaker != 1:

        status_student = input('\nWrite the status of the student, ¿is active or inactive?: ').strip().replace(" ","").lower()

        if status_student == 'active' or status_student == 'inactive':
            fifth_while_breaker = 1
        else:
            print('\nThe data is invalid')

    #then, we return the dictionary with the information of the student    
    return {'id': ID_student, 'name': name_student, 'age': age_student, 'level': grade_student, 'status':status_student}

#here is the function to show the full list of students
def show_the_students(students_list):
    #we go through to check if the length is 0 or more
    if len(students_list) == 0:
        print("\nThere's no students yet")
    #if there are students so print them
    else:
        for i in students_list:
            print(f'\nID:{i['id']} | nombre:{i['name']} | age:{i['age']} | level:{i['level']} | status:{i['status']}')

#this is the function to consult some student
def consult_some_student(students_list):
    name_search_input = input("\nWrite the name of te student: ").strip().replace(" ","_").lower()
    exist = False

    for i in students_list:
        if name_search_input == i['name']:
            print(f'\nID:{i['id']} | nombre:{i['name']} | age:{i['age']} | level:{i['level']} | status:{i['status']}')
            exist = True
    
    if not exist:
        print("\nThe student hasn't found")

#this is the function to change the information of one student
def update_students_information(students_list):
    student_to_update = input("\nWrite the name of the student you want to update: ")

    exist= False
    
    #the for loop to go through the list where are the students and chek if the student exists
    for i in students_list:
        if student_to_update == i['name']:
            exist = True
            print(f"\nYou will update: ID:{i['id']} | nombre:{i['name']} | age:{i['age']} | level:{i['level']} | status:{i['status']}')")
            print("\nYou can't change de ID becouse is unique")

            #while breakers
            first_breaker = 0
            second_breaker = 0
            third_breaker = 0
            fourth_breaker = 0

            #first while loop to check if the input is right and reassign the name
            while first_breaker != 1:
                new_name_student = input("\nWrite the new name: ")
                numberfinder= False
                for x in new_name_student:
                    if x.isdigit():
                        numberfinder = True
                if numberfinder == True:
                    print("\nThe name can't have numbers")
                else:
                    i['name']= new_name_student
                    first_breaker = 1

            #second while loop to check if the input age is right and reassign the age
            while second_breaker != 1:
                try:
                    new_age_student = int(input('\nWrite the new age: '))
                    if new_age_student <= 3:
                        print("\nWith that age the student can't be at the institution")
                    else:
                        i['age']= new_age_student
                        second_breaker = 1
                except:
                    print("\nThe data is invalid")

            #the third while loop to check the option and reassign the level
            while third_breaker != 1:

                #the levels that exist
                grades = """
The levels are:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
"""
                print (grades)

                new_grade_student = input("\nWrite the level of the student: ")

                if new_grade_student == '1' or new_grade_student == '2' or new_grade_student == '3' or new_grade_student == '4' or new_grade_student == '5' or new_grade_student == '6' or new_grade_student == '7' or new_grade_student == '8' or new_grade_student == '9' or new_grade_student == '10' or new_grade_student == '11':
                    i['level'] = new_grade_student
                    third_breaker = 1
                else:
                    print("\nThe level doesn't exist")

            #the fourth while loop to check if the option are active or inactive and reassign the status          
            while fourth_breaker != 1:

                new_status_student = input("\nWrite the new status of the student, ¿is active or inactive?: ")
                if new_status_student == 'active' or new_status_student == 'inactive':
                    i['status'] = new_status_student
                    fourth_breaker = 1
                else:
                    print("\nWrite a valid data")

            
            print(f"\nYou have updated: ID:{i['id']} | nombre:{i['name']} | age:{i['age']} | level:{i['level']} | status:{i['status']}")

#The function to delete a student
def delete_student(students_list):
    breaker = 0 #this is a breaker to control the while loop
    #the while loop to find and student by the ID and check if there's right and exists
    while breaker != 1:
        consult_student = input("\nTo find the student write its ID: ")
        if not consult_student.isdigit():
            print("\nThere only has to be numbers")
        elif len(consult_student) != 4:
            print('\nThere only has to be 4 digits')
        else:
            breaker = 1
    
    #a flag to catch the position of the student
    student_found = None
    
    #going through the list to find the student
    for i in students_list:
        if i['id'] == consult_student:
            student_found = i #the flag variable takes the value, its the position of the student
    
    if student_found:
        print(f"\nThe student {student_found['name']} has been deleted")
        students_list.remove(student_found) #here the student is deleted already
    
    else:
        print("\nThe student hasn't been found")


