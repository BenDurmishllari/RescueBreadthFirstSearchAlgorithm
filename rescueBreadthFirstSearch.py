###############################################
# Assigment: Professional Practice Week 2     #
# Module: CET313 - Artificial Intelligence    #
# Lecturer: Dr Kate MacFarlane                #
# Student: Arben Durmishllari                 #
# Student Code - bh19hd                       #
# Course: Computer Science - 3rd Year         #
###############################################



# '''
# imports
# no need to install any
# specific library
# '''
import csv
import os
import sys
import queue
import datetime

# '''
# boolean variables to manage
# the triggers of each method
# depended of the case that we want to run
# '''
people = False
animal = False
way_out = False

# '''
# counter to trigger the loop
# '''
counter = 0


# '''
# This method its read the txt file that its save
# on the same directory with the additional files and its create the maze, 
# through this method we have the ability o give the option to the 
# user to create a map instead to hardcode it into the code
# '''
def createMaze():

    # '''
    # variable that its 
    # save the path of the txt file
    # '''
    filepath = 'maze_map.txt'
    
    # '''
    # bellow its read  each line of the file
    # and its added to the maze list, through the loop we add all
    # the lines and we set a specif format with locations
    # as the rest methods of the scrips need specific locations
    # to do the additional acts for the implementations of the algorithm
    # '''
    with open(filepath, 'r') as file:
        lines = file.readlines()
        maze = []
        for item in lines:
            maze.append(item.rstrip('\n').rsplit(" "))
            
    return maze

# '''
# This method is used to print the maze 
# along the moves that it does the algorithm
# you'll find it bellow on the prints of the cases
# Source code for this method: https://techwithtim.net/tutorials/breadth-first-search/?fbclid=IwAR1QBlJ1scYV9DhsG-Oax2DZqJszQGlyNLf94naPvxklYVZ-lEgnsHK8XTc
# '''
def printMaze(maze, path=""):

    # '''
    # loop to search and find the x and pos ('position') 
    # using the enumerate class from the language and
    # to set a start
    # '''
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()

    # '''
    # loop to set each move on the path
    # '''
    for move in path:
        
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    # '''
    # loop for each row and colum 
    # of the maze to add the pointer of the steps
    # '''
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+", end="")
            else:
                print(col + " ", end="")
        print()
# '''
# This method is used to validate the maze 
# and to recognize the # that are the walls-limits
# of the map
# Source code for this method: https://techwithtim.net/tutorials/breadth-first-search/?fbclid=IwAR1QBlJ1scYV9DhsG-Oax2DZqJszQGlyNLf94naPvxklYVZ-lEgnsHK8XTc
# '''
def valid(maze, moves):
    
    # '''
    # loop to search and find the x and pos ('position') 
    # using the enumerate class from the language and
    # to set a start
    # '''
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0

    # '''
    # loop to check each move on the path
    # '''
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        # '''
        # if statments to check the # on the map
        # '''
        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True

# '''
# This method is used to set the algorithm to search 
# for the exit of the map that is the position 'X'
# the logic has been taken from the link bellow but 
# the logic and the implemenations has been changed
# Source code for this method: https://techwithtim.net/tutorials/breadth-first-search/?fbclid=IwAR1QBlJ1scYV9DhsG-Oax2DZqJszQGlyNLf94naPvxklYVZ-lEgnsHK8XTc
# '''
def findExit(maze, moves):
     
    # '''
    # boolean global variables for to change
    # the status and to recognize the algorithm
    # that the exit has been found and to finish
    # '''
    global way_out 
    global counter

    # '''
    # local variable to
    # count the steps that 
    # has been done till to achive 
    # the target
    # '''
    exit_counter = 0

    # '''
    # local variable for the 
    # timestamp of the action
    # '''
    timeStamp = datetime.datetime.utcnow()
    
    # '''
    # loop to search and find the x and pos ('position') 
    # using the enumerate class from the language and
    # to set a start
    # '''
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0

    # '''
    # loop to check and set each move 
    # '''
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        # '''
        # increasment counter to
        # count the steps
        # '''
        exit_counter += 1
    
    # '''
    # if statment to check if we achieve the
    # target and to print all the addition
    # informations along with the boolean variable
    # to change the status and to inform the system 
    # for the addition  steps
    # '''
    if maze[j][i] == "X" and way_out == False :
        print()
        print("========= Given Action =========")
        print()
        print(" Rescue Team have found the exit")
        print()
        print(" Found Directions: " + moves)
        print()
        print(" Execution Moves: " + (str(exit_counter)))
        print()
        print(" Action Time Stamp: " + str(timeStamp))
        print()
        print("========= Maze Visualization =========")
        print()
        printMaze(maze, moves)
        counter += 1
        finish = True
        print()
        print("-----------------------------------")
        print()
        
    return False


# '''
# This method is used to set the algorithm to search 
# for the animal on the map that is the position '$'
# '''
def findAnimal(maze, moves):
    
    # '''
    # boolean global variables to change
    # the status and to recognize the algorithm
    # that the animal has been found and to go 
    # on the next target
    # '''
    global animal  
    global counter

    # '''
    # local variable to
    # count the steps that 
    # has been done till to achive 
    # the target
    # '''
    animal_counter = 0

    # '''
    # local variable for the 
    # timestamp of the action
    # '''
    timeStamp = datetime.datetime.utcnow()
   
    # '''
    # loop to search and find the x and pos ('position') 
    # using the enumerate class from the language and
    # to set a start
    # '''
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0

    # '''
    # loop to check and set each move 
    # '''
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        # '''
        # increasment counter to
        # count the steps
        # '''
        animal_counter += 1

    # '''
    # if statment to check if we achieve the
    # target and to print all the addition
    # informations along with the boolean variable
    # to change the status and to inform the system 
    # for the addition  steps
    # '''
    if maze[j][i] == "$" and animal == False:
        print()
        print("========= Given Action =========")
        print()
        print(" Rescue Team have found animal")
        print()
        print(" Found Directions: " + moves)
        print()
        print(" Execution Moves: " + (str(animal_counter)))
        print()
        print(" Action Time Stamp: " + str(timeStamp))
        print()
        print("========= Maze Visualization =========")
        print()
        printMaze(maze, moves)
        counter += 1
        animal = True
        print()
        print("-----------------------------------")
        print()
    return False


# '''
# This method is used to set the algorithm to search 
# for the people on the map that is the position '@'
# '''
def findPeople(maze, moves):

    # '''
    # boolean global variables  to change
    # the status and to recognize the algorithm
    # that the people has been found and to go 
    # on the next target
    # '''
    global people 
    global counter

    # '''
    # local variable to
    # count the steps that 
    # has been done till to achive 
    # the target
    # '''
    people_counter = 0

    # '''
    # local variable for the 
    # timestamp of the action
    # '''
    timeStamp = datetime.datetime.utcnow()

    # '''
    # loop to search and find the x and pos ('position') 
    # using the enumerate class from the language and
    # to set a start
    # '''
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0

    # '''
    # loop to check and set each move 
    # '''
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        # '''
        # increasment counter to
        # count the steps
        # '''
        people_counter += 1

    # '''
    # if statment to check if we achieve the
    # target and to print all the addition
    # informations along with the boolean variable
    # to change the status and to inform the system 
    # for the addition  steps
    # '''
    if maze[j][i] == "@" and people == False:
        print()
        print("========= Given Action =========")
        print()
        print(" Rescue Team have found people")
        print()
        print(" Found Directions: " + moves)
        print()
        print(" Execution Moves: " + (str(people_counter)))
        print()
        print(" Action Time Stamp: " + str(timeStamp))
        print()
        print("========= Maze Visualization =========")
        print()
        printMaze(maze, moves)
        counter += 1
        people = True
        print()
        print("-----------------------------------")
        print()
       
        
    return False



# '''
# main algorithm, variables for queue and for the
# setting of the tasks on queues along with the variable 
# tha we save the maze into
# the logic has been taken from the link bellow 
# Source code for this method: https://techwithtim.net/tutorials/breadth-first-search/?fbclid=IwAR1QBlJ1scYV9DhsG-Oax2DZqJszQGlyNLf94naPvxklYVZ-lEgnsHK8XTc
# '''
nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze()

# '''
# while loop that its running when the script run,
# it trigger through the counter variable that it increase 
# into the methods of the (people,animal,exit) and its stop
# when its inform that all the steps have been done
# '''
while counter <= 3:
    # '''
    # calling the methods to run each task
    # '''
    findPeople(maze, add)
    findAnimal(maze, add)
    findExit(maze, add)
    
    # '''
    # get the queues and saving on variable
    # '''
    add = nums.get()

    # '''
    # if you uncomment the print
    # you'll see the steps that the algorithm
    # does during the running
    # '''
    #print(add)

    # '''
    # loop for the tasks along with the
    # if statment that its validate the steps
    # if are done
    # Source code for this method: https://techwithtim.net/tutorials/breadth-first-search/?fbclid=IwAR1QBlJ1scYV9DhsG-Oax2DZqJszQGlyNLf94naPvxklYVZ-lEgnsHK8XTc
    # '''
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if  valid(maze, put):
            nums.put(put)
    
    # '''
    # if statment to check if the algorithm
    # have done and finish the target to stop
    # the script
    # '''
    if counter == 3:
            break