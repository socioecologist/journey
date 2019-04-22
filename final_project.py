## Project title: Simple Student Grade Database Portal
## Author: Siham Afatta K. Taruc
## Date completed: 22 April 2019
## Description:
'''
Final project for the Python Programming for Beginners course
at the Stone River eLearning (https://stoneriverelearning.com)
'''

# Function for asking user to input username and password
def askUser():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    # Move to the checkPass function with username/password as the inputs
    checkPass(username, password)

# Function for checking matching between username/password input
# with the pre-defined username and password
def checkPass(use, pwd):
    if use == 'administrator' and pwd == 'password':
        login(use)
    else:
        print ('Your username and/or password was incorrect')
        askUser()

# Function to display message that login successful        
def login(use):
    print ('Welcome',use)
    print ('You have successfully logged in at the Grade Central!')
    askCom()

# Define the dictionary
global dict
dict = {}

# Function asking user which activity she/he prefer    
def askCom():
  
    print('What do you want to do?')
    print('[1] - Add student and grade')
    print('[2] - Remove student and grade')
    print('[3] - Student average grades')
    print('[4] - Display student grades')
    print('[5] - Exit')
    command = input('Enter your command: ')

    if command == '1':
        menuOne()
    elif command == '2':
        menuTwo()
    elif command == '3':
        menuThree()
    elif command == '4':
        menuFour()
    else:
        menuFive()

# Function for adding new student and the associated grade to the dictionary
def menuOne():
    keyStudent = input('Enter student name:')
    valGrade = input('Enter student grade:')
    newDict = {}
    newDict[keyStudent] = valGrade
    dict.update(newDict)
    print('The current grade data is:')
    print(dict)
    askCom()

# Function for removing new student and the associated grade to the dictionary
def menuTwo():
    keyStudent = input('Enter student name to be removed:')
    dict.pop(keyStudent, None)
    print('The current grade data is:')
    print(dict)
    askCom()

# Function for calculating the average grade if the current database state
def menuThree():
    # Check the list of values in the database/dictionary
    # However, the grades are in string not numbers (int/float)
    gradeValueList = list(dict.values())
    print('The values in the database are:')
    print(gradeValueList)

    # Convert the grade strings into floats
    gradeValues = [float(i) for i in gradeValueList]
    print('The list of values extracted from the databales is:')
    print(gradeValues)

    # Use the mean function from the built-in statistics module
    from statistics import mean
    def averageGrade():
        return mean(gradeValues)
    print('The average grade is:', averageGrade())
    print()
    askCom()

# Presents latest grades
def menuFour():
    print('The latest grade data is:')
    print(dict)

# Asks user to logout or return to main menu
def menuFive():
    command = input('Do you want to [1] quit or [2] return to menu?')
    if command == '1':
        askUser()
    else:
        askCom()
        
askUser()
