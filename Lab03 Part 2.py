#student name:      Liam Foster
#student number:    40199382

import multiprocessing as mp

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    unique = set()
    for i in range(len(puzzle)):                        #loop through the values in column
        unique.add(puzzle[i][column])                   #add each value to the set since it ignores duplicates
    if len(unique) < 9:                                 #check if the set has less than 9 values
        print("Column " + str(column) + " not valid")
    else:
        print("Column " + str(column) + " valid")
        
def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    unique = set()
    for i in range(len(puzzle)):                    #loop through the values in row
        unique.add(puzzle[row][i])                  #add each value to the set
    if len(unique) < 9:                             #check if the set has less than 9 values
        print("Row " + str(row) + " not valid")
    else:
        print("Row " + str(row) + " valid")

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    unique = set()
    #the nested loop below adds each value in subgrid to the set
    for i in range(0,3):
        for j in range(0,3):
            #casting the result of the division to int truncates the decimal
            unique.add(puzzle[int(subgrid/3)*3+i][(subgrid%3)*3+j])
    #check if the set has less than 9 values
    if len(unique) < 9:
        print("Subgrid " + str(subgrid) + " not valid")
    else:
        print("Subgrid " + str(subgrid) + " valid")


if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5]
            ]
    testrow = [ [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2, 2, 2, 2],
                [3, 3, 3, 3, 3, 3, 3, 3, 3],
                [4, 4, 4, 4, 4, 4, 4, 4, 4],
                [5, 5, 5, 5, 5, 5, 5, 5, 5],
                [6, 6, 6, 6, 6, 6, 6, 6, 6],
                [7, 7, 7, 7, 7, 7, 7, 7, 7],
                [8, 8, 8, 8, 8, 8, 8, 8, 8],
                [9, 9, 9, 9, 9, 9, 9, 9, 9]
              ]
        
    testcase = testrow   #modify here for other testcases

    SIZE = 9
    procs = []

    #append all column check processes to procs
    for col in range(SIZE):
        procs.append(mp.Process(target=checkColumn, args=(testcase, col)))

    #append all row check processes to procs
    for row in range(SIZE):
        procs.append(mp.Process(target=checkRow, args=(testcase, row)))

    #append all subgrid check processes to procs
    for subgrid in range(SIZE):
        procs.append(mp.Process(target=checkSubgrid, args=(testcase, subgrid)))
    
    for p in procs:     #start all processes in procs
        p.start()
    for p in procs:     #join all processes in procs
        p.join()
    