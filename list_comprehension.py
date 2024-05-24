# num = [0,1,2,3,4,5] 
# squares = [] 
# for x in num: squares.append(x ** 2) 
# print(squares) 

# num = [0,1,2,3,4,5] 
# squares = [X ** 2 for X in num] 
# print(squares) 

num = [0,1,2,3,4,5]
even_squares = [X ** 2 for X in num if X % 2 == 0] 
print(even_squares) 