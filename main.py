#here is the importation of the functions
from functions import *



#this is the list where the dictionary has to be added
students_list =[]

#when running the app we charge the json data
charge_from_json(students_list)
#here is the option waiting for the value
option = ""

#using a while loop to run the program every time except the option six
while option != '6':
    
    #here is the menu
    menu()
    
    #here the user writes its option
    option = input('\nPlease, write the number of your option: ')

    #if the option is 1 it calls the function add_new_student and next the return is append to the list
    if option == '1':
        dictionary_data = add_new_student(students_list)
        students_list.append(dictionary_data)
        #then we add the list at the Data in JSON
        add_to_json(students_list)
    
    #if the option is 2 it calls the show_the_students function
    elif option == '2':
        show_the_students(students_list)
    
    #if option is 3 it calls consult_some_student function
    elif option == '3':
        consult_some_student(students_list)
    
    #if option is 3 it calls update_students_information function
    elif option == '4':
        update_students_information(students_list)
        #then we add the list again at the Data in JSON and overwrite it 'cause is new
        add_to_json(students_list)
    
    #if option is 3 it calls delete_student function
    elif option == '5':
        delete_student(students_list)
        #then we add the list again at the Data in JSON and overwrite it 'cause is new
        add_to_json(students_list)
    
    #if the option is 6 we break the loop
    elif option == '6':
        print('\nGOOD-BYE')
    
    #if there's a wrong value so we print that is not valid
    else:
        print("\nThe option is not valid")