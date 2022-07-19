import math
import time
import random
import csv
from pysat.solvers import Solver
import argparse
from clauses import * 

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

def no_of_solution(sudoku_pair_solver, pre_filled):                     # Function for checking the number of solution of given sudoku
    found_sol=False                                                     # Assume there are no solution
    for x in sudoku_pair_solver.enum_models(assumptions = pre_filled):  # Use enum_models to go through the solutions
        if found_sol==True:                                                 
            return 2                                                    # return 2 for more than 1 solutions
        else:
            found_sol=True

    if found_sol==False:
        return 0                                                        # return 0 for no solution

    return 1                                                            # return 1 for unique solution


#-----------------------------------------------------------------------------------------------------------------------------------------------------#

def already_filled_values(sudoku_pair, n):                                              # Function returning a list of hashes of pre-determined value
    pre_filled=[]                                                                       # Initialise the empty list
    for sudoku_num in range(2):                                 
        for i in range(n):
            for j in range(n):
                for num in range(n):
                    if sudoku_pair[sudoku_num][i][j]:
                        if(sudoku_pair[sudoku_num][i][j]==num+1):                       # Iterate through the sudoku and check for given value and append their hashes
                            pre_filled.append(int(n*n*n*sudoku_num+n*n*i+n*j+num+1))
                        else:
                            pre_filled.append(int(-n*n*n*sudoku_num-n*n*i-n*j-num-1))
    
    return pre_filled

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

def print_solved_sudoku_pair(sudoku_pair_solver, n, pre_filled):        # Function for solving and printing sudoku pair
    found_sol=False
    for x in sudoku_pair_solver.enum_models(assumptions = pre_filled):  # Use enum_models to go through the possible solutions
        solved_sudoku_pair=[]
        found_sol=True
        print(".........................................\n")
        for sudoku_num in range(2):
            for i in range(n):
                cur_row=[]
                for j in range(n):
                    for num in range(n):
                        hash=int(n*n*n*sudoku_num+n*n*i+n*j+num)      # Again get hash to the corresponding variable, but don't add 1 to get index in the hash list
                        if x[hash]>0:                                 # A positive value represents truth
                            if num+1>9:                               # Check number of digits and correspondigly put spaces at the end
                                print(num+1, end="   ")
                            else:
                                print(num+1, end="    ")
                            
                            cur_row.append(num+1)

                solved_sudoku_pair.append(cur_row)
                print("\n")

            with open('solved_sudoku.csv', 'w', encoding='UTF8', newline="") as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerows(solved_sudoku_pair)

            print(".........................................\n")

        break

    if found_sol==False:
        print("None")

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

def generate_filled_random_sudoku_pair(n, clause_list, no_of_outputs):                 # Function to generate fully filled random sudoku

    temp_sudoku_pair_list=[]    
    generated_sudoku_pair_list=[]
    while len(generated_sudoku_pair_list)< no_of_outputs:

        s1=[]
        s2=[]
        for i in range(n):
            s1.append([0]*n)

        for i in range(n):
            s2.append([0]*n)                                            

        sudoku_pair=[]
        sudoku_pair.append(s1)
        sudoku_pair.append(s2)                                          # initialise with empty sudoku pair
        shift=random.randint(1, n-1)                                    # get a random shift for filling 2nd sudoku
        row_initial=[]
        for i in range(n):
            row_initial.append(i+1)

        random.shuffle(row_initial)
        random_row_num=random.randint(0, n-1)
        for j in range(n):                                              #randomly fill a row of both sudokus to get a random seed
            sudoku_pair[0][random_row_num][j]=row_initial[j]
            sudoku_pair[1][random_row_num][j]=((shift+sudoku_pair[0][random_row_num][j])%n)+1
        
        if sudoku_pair in temp_sudoku_pair_list:
            continue
        else:
            temp_sudoku_pair_list.append(sudoku_pair)

        pre_filled=already_filled_values(sudoku_pair, n)

        sudoku_pair_solver=Solver()                                     # Initialise the Solver
        sudoku_pair_solver.append_formula(clause_list)                  # Insert the clauses into solver
        
        for x in sudoku_pair_solver.enum_models(assumptions = pre_filled):  # Solve same as the print_solved_sudoku_pair
            generated_pair=[]
            for sudoku_num in range(2):
                cur_sudoku=[]
                for i in range(n):
                    cur_row=[]
                    for j in range(n):
                        for num in range(n):
                            hash=int(n*n*n*sudoku_num+n*n*i+n*j+num)
                            if x[hash]>0:
                                cur_row.append(num+1)

                    cur_sudoku.append(cur_row)

                generated_pair.append(cur_sudoku)

            generated_sudoku_pair_list.append(generated_pair)
            break
        
        
        sudoku_pair_solver.delete()
    return generated_sudoku_pair_list

#-----------------------------------------------------------------------------------------------------------------------------------------------------#