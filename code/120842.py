#120842
def solution(num_list, n):
    cols = len(num_list) // n
    rows = n
    
    x = [[0 for _ in range(rows)] for _ in range(cols)]
    
    col_index = 0
    row_index = 0
    
    for num in num_list:
        x[col_index][row_index] = num
        row_index += 1
        if rows == row_index:
            row_index = 0
            col_index += 1
    
    return x