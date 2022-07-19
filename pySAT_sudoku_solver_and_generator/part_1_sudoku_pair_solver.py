from functions import *

parser = argparse.ArgumentParser()
parser.add_argument("-input", "--file", type=str, default='sudoku.csv')
parser.add_argument("-k", "--number", type=int, default=0)
args = parser.parse_args()
sudoku=args.file
k=args.number

start=time.time()

#taking input from file

_sudoku_ = open(sudoku, 'r')
reader = csv.reader(_sudoku_, delimiter=',')
a=[]
for row in reader:
    a.append(row)


n=k*k

# In case of no argument provided for k, figure out k from csv input
if n==0:
    n=int(len(a)/2)
    k=int(math.sqrt(n))


#storing values in data structures
s1=[]
s2=[]
for i in range(n):
    temp_list=[]
    for num in a[i]:
        temp_list.append(int(num))
    s1.append(temp_list)

for i in range(n):
    temp_list=[]
    for num in a[i+n]:
        temp_list.append(int(num))
    s2.append(temp_list)

sudoku_pair=[]                                                  # Initialise sudoku pair
sudoku_pair.append(s1)                                          # Append sudoku1
sudoku_pair.append(s2)                                          # Append sudoku2
        
sudoku_pair_solver=Solver()                                     # Initialise Solver

clause_list=all_clauses(k)                                      # Get clause list according to value of k

sudoku_pair_solver.append_formula(clause_list)                  # Insert clause list into solver

pre_filled=already_filled_values(sudoku_pair, n)                # Get list of hashes of already determined values

print_solved_sudoku_pair(sudoku_pair_solver, n, pre_filled)     # Print the solved sudoku

end=time.time()
print(f"Time Taken : {end-start}")                              # Print time taken in solving the sudoku