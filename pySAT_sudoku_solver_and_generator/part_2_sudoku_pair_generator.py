from functions import *


parser = argparse.ArgumentParser()
parser.add_argument("-k", "--number", type=int, default=3)
parser.add_argument("-o", "--outputs", type=int, default=1)
args = parser.parse_args()

k = args.number                                             # The dimension of sudoku i.e. (k x k sudoku)
o = args.outputs                                            # Number of random sudoku to be generated

start=time.time()

n=k*k                                                       # n is the overall dimension of sudoku


clause_list=all_clauses(k)                                          # Get the list of all clauses corresponding to given k

sudoku_pairs=generate_filled_random_sudoku_pair(n, clause_list, o)  # Generate the sudoku pairs according to number of outputs to be generated

solved_sudoku_pairs=[]                                      # Initialised the final list

num=1                                                       # The index of sudoku pair to be solved, initialise with 1

for sudoku_pair in sudoku_pairs:

    random_indices=[]                                       # Using random list of hashes for traversing the sudoku pair in a randomised manner 
    for i in range(2*n*n):
        random_indices.append(i)
    
    random.shuffle(random_indices)

    for ind in random_indices:

        sudoku_num=ind//(n*n)                               # un-hash the values of sudoku_num, i, j from the hashed value
        ind%=(n*n)
        i=ind//n
        j=ind%n
        
        temp_var=sudoku_pair[sudoku_num][i][j]                      # Temporarily store the value in this cell
        
        sudoku_pair[sudoku_num][i][j]=int(0)                        # Empty the cell
        
        pre_filled_new=already_filled_values(sudoku_pair, n)        # Generate the determined value according to this sudoku
        
        sudoku_pair_solver=Solver()                                 # Initialise the SAT solver
        
        sudoku_pair_solver.append_formula(clause_list)              # Insert the clauses into the solver
        
        no_sol=no_of_solution(sudoku_pair_solver, pre_filled_new)   # Calculate the number of solutions of this sudoku
        
        if no_sol==2:
            sudoku_pair[sudoku_num][i][j]=temp_var                  # If the new sudoku don't have unique solution, restore the removed value

        sudoku_pair_solver.delete()
    

    end=time.time()     # All sudoku pairs have been generated, so note the end time

    file='sudoku'+str(num)+'.csv'                               # The file name in which generated sudoku will be  printed
    num+=1
    with open(file, 'w', encoding='UTF8', newline="") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(sudoku_pair[0])
        writer.writerows(sudoku_pair[1])

    solved_sudoku_pairs.append(sudoku_pair)

print(f"Time Taken : {end-start} seconds in generating {o} pairs of sudoku")     # Print the time taken in generating the sudoku pairs