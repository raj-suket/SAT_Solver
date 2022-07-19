def all_clauses(k):
    
    n=k*k
    clause_list=[]
    # each cell have at least one number
    for sudoku_num in range(2):
        for i in range(n):
            for j in range(n):
                temp_list=[]
                for num in range(n):
                    temp_list.append(int(n*n*n*sudoku_num+n*n*i+n*j+num+1))

                clause_list.append(temp_list)



    # each cell have at most one number
    for sudoku_num in range(2):
        for i in range(n):
            for j in range(n):
                for num1 in range(n):
                    for num2 in range(num1+1, n):
                        temp_list=[]
                        temp_list.append(int(-n*n*n*sudoku_num-n*n*i-n*j-num1-1))
                        temp_list.append(int(-n*n*n*sudoku_num-n*n*i-n*j-num2-1))
                        clause_list.append(temp_list)



    # each row have all the numbers
    for sudoku_num in range(2):
        for i in range(n):
            for num in range(n):
                temp_list=[]
                for j in range(n):
                    temp_list.append(int(n*n*n*sudoku_num+n*n*i+n*j+num+1))

                clause_list.append(temp_list)



    # each row have no number twice
    for sudoku_num in range(2):
        for i in range(n):
            for num in range(n):
                for j1 in range(n):
                    for j2 in range(j1+1, n):
                        temp_list=[]
                        temp_list.append(int(-n*n*n*sudoku_num-n*n*i-n*j1-num-1))
                        temp_list.append(int(-n*n*n*sudoku_num-n*n*i-n*j2-num-1))
                        clause_list.append(temp_list)



    # each column have all the numbers
    for sudoku_num in range(2):
        for j in range(n):
            for num in range(n):
                temp_list=[]
                for i in range(n):
                    temp_list.append(int(n*n*n*sudoku_num+n*n*i+n*j+num+1))

                clause_list.append(temp_list)



    # each column have no number twice
    for sudoku_num in range(2):
        for j in range(n):
            for num in range(n):
                for i1 in range(n):
                    for i2 in range(i1+1, n):
                        temp_list=[]
                        temp_list.append(int(-n*n*n*sudoku_num-n*n*i1-n*j-num-1))
                        temp_list.append(int(-n*n*n*sudoku_num-n*n*i2-n*j-num-1))
                        clause_list.append(temp_list)



    # each box have all the numbers
    for sudoku_num in range(2):
        for row in range(k):
            for col in range(k):
                for num in range(n):
                    temp_list=[]
                    for i in range(k*row, k*(row+1)):
                        for j in range(k*col, k*(col+1)):
                            temp_list.append(int(n*n*n*sudoku_num+n*n*i+n*j+num+1))
                
                    clause_list.append(temp_list)
    


    # each box have no number twice
    for sudoku_num in range(2):
        for row in range(k):
            for col in range(k):
                for num in range(n):
                    for i1 in range(k*row, k*(row+1)):
                        for j1 in range(k*col, k*(col+1)):
                            for i2 in range(k*row, k*(row+1)):
                                for j2 in range(k*col, k*(col+1)):
                                    if i1!=i2 or j1!=j2:
                                        temp_list=[]
                                        temp_list.append(int(-n*n*n*sudoku_num-n*n*i1-n*j1-num-1))
                                        temp_list.append(int(-n*n*n*sudoku_num-n*n*i2-n*j2-num-1))
                                        clause_list.append(temp_list)



    # both the sudokus have different numbers in same cell
    for i in range(n):
        for j in range(n):
            for num in range(n):
                temp_list=[]
                temp_list.append(int(-n*n*i-n*j-num-1))
                temp_list.append(int(-n*n*n-n*n*i-n*j-num-1))
                clause_list.append(temp_list)


    return clause_list