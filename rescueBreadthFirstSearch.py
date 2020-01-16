import csv
import os
import sys
import queue
import datetime

people = False
animal = False
way_out = False
counter = 0



def createMaze():
    filepath = 'maze_map.txt'
    
    with open(filepath, 'r') as file:
        lines = file.readlines()
        maze = []
        for item in lines:
            maze.append(item.rstrip('\n').rsplit(" "))
            
    return maze


def printMaze(maze, path=""):


    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
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
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    global moves_counter
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
     
    global way_out 
    global counter

    exit_counter = 0

    timeStamp = datetime.datetime.utcnow()
    
    
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        exit_counter += 1

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



def findpet(maze, moves):
    
    global animal  
    global counter

    animal_counter = 0

    timeStamp = datetime.datetime.utcnow()
   

    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        animal_counter += 1

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



def findPeople(maze, moves):
    global people 
    global counter

    people_counter = 0

    timeStamp = datetime.datetime.utcnow()

    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1
        elif move == "R":
            i += 1
        elif move == "U":
            j -= 1
        elif move == "D":
            j += 1
        people_counter += 1

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



# MAIN ALGORITHM
nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze()


while counter <= 3:
    findPeople(maze, add)
    findpet(maze, add)
    findEnd(maze, add)
    
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if  valid(maze, put):
            nums.put(put)
        
    if counter == 3:
            break