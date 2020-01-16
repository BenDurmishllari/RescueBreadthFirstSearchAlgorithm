import csv
import os
import sys
import queue

people = False
pet = False
finish = False
counter = 0
def createMaze():
    filepath = 'maze_map.txt'
    
    with open(filepath, 'r') as file:
        lines = file.readlines()
        maze = []
        for item in lines:
            maze.append(item.rstrip('\n').rsplit(" "))
            # maze.append(" ".join(item.rstrip('\n')))
    
    return maze

# print(maze)
# print(maze[0])
# print(maze[1])
# print(maze[2])
# print(maze[3])
# print(maze[4])
# print(maze[5])
# print(maze[6])
# print(maze[7])
# print(maze[8])


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
    global people 
    global pet 
    global finish 
    global counter

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
    
    # if maze[j][i] == "X":
    #     print("Rescue Team have found the exit")
    #     print(moves)
    #     printMaze(maze, moves)
    #     return True
    if maze[j][i] == "X" and finish == False :
        print("Rescue Team have found the exit")
        #print(moves)
        printMaze(maze, moves)
        # finish = True

        counter += 1
        finish = True

    return False



def findpet(maze, moves):
    global people 
    global pet 
    global finish 
    global counter

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

    # if maze[j][i] == "$": 
    #     print("Rescue Team have found animal")
    #     print("Found: " + moves)
    #     printMaze(maze, moves)
    #     return True
    if maze[j][i] == "$" and pet == False: 
        print("Rescue Team have found animal")
        # print("Found: " + moves)
        printMaze(maze, moves)
        # pet = True

        counter += 1
        pet = True
    return False



def findPeople(maze, moves):
    global people 
    global pet 
    global finish 
    global counter
    
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
    
    if maze[j][i] == "@" and people == False:
        print("Rescue Team have found people")
        # print("Found: " + moves)
        printMaze(maze, moves)
        # people = True

        counter += 1
        people = True
        print("-----------------------------------")
        
        
        
         
        
    # elif maze[j][i] == "$" and pet == False: 
    #     print("Rescue Team have found animal")
    #     # print("Found: " + moves)
    #     printMaze(maze, moves)
    #     # pet = True

    #     counter += 1
    #     pet = True
        
        
        
    # elif maze[j][i] == "X" and finish == False :
    #     print("Rescue Team have found the exit")
    #     #print(moves)
    #     printMaze(maze, moves)
    #     # finish = True

    #     counter += 1
    #     finish = True
        
        
        
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
        # nums.task_done()
        break

        
            


# while not findpet(maze, add): 
#     add = nums.get()
#     print(add)
#     for j in ["L", "R", "U", "D"]:
#         put = add + j
#         if  valid(maze, put):
#             nums.put(put)

        
# while not findEnd(maze, add): 
#     add = nums.get()
#     print(add)
#     for j in ["L", "R", "U", "D"]:
#         put = add + j
#         if  valid(maze, put):
#             nums.put(put)