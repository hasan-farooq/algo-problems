

def multiply_matrices(matrix_a,matrix_b,index=0,result=[]):
    if (index < len(matrix_a[1])):
        answer = [0]
        i = 0 
        for data in matrix_a[index]:
            answer[0] = answer[0] + data * matrix_b[i]
            i += 1
        result.append(answer)
        index += 1
        return multiply_matrices(matrix_a,matrix_b,index)
    else:
        return result

matrix_X = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

matrix_Theta = [1,1,1]
ans = multiply_matrices(matrix_X,matrix_Theta)
# print("The result is a ", len(ans), " x ", len(ans[0]), " Matrix" )
# for row in ans:
#     print(row)

