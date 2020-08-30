
class matrix:
    rows = 0
    cols = 0
    data = []

    def __init__(self, rows=0, cols=0,data = None):
        self.rows = rows
        self.cols = cols
        for row in range(self.rows):
            self.data.append([0] * self.cols)
        return
    def adds(self,m1):
        result = matrix()
        result.rows = self.rows
        result.cols = self.cols
        result.data = []
        # for row in range(self.rows):
        #     self.data.append([0] * self.cols)
        
        for i in range(m1.rows):
            add_rows = []
            for j in range(m1.cols):
                add_rows.append(int(self.data[i][j] + m1.data[i][j]))
                # result.data[i][j] = self.data[i][j] + m1.data[i][j]
            result.data.append(add_rows)
            # print(result.data[i])
        return result

    def subs(self,m1):
            result = matrix()
            result.rows = self.rows
            result.cols = self.cols
            result.data = []
            # for row in range(self.rows):
            #     self.data.append([0] * self.cols)

            for i in range(m1.rows):
                add_rows = []
                for j in range(m1.cols):
                    add_rows.append(int(self.data[i][j] - m1.data[i][j]))
                    # result.data[i][j] = self.data[i][j] + m1.data[i][j]
                result.data.append(add_rows)
                # print(result.data[i])
            return result


matrix_1 = matrix()
matrix_2 = matrix()
matrix_3 = matrix()

rows = int(input('Rows : '))
cols = int(input('Columns : '))

matrix_1.rows = rows
matrix_2.rows = rows

matrix_1.cols = cols
matrix_2.cols = cols

print('Matrix 1')
for row in range(rows):
    add_rows = []
    for col in range(cols):
        print('Enter Matrix[', row,'][',col,'] : ')
        # matrix_1.data[row].append() = input(' > ')
        add_rows.append(int(input(' > ')))
    matrix_1.data.append(add_rows)

add_rows = None

matrix_2.data = []
print('Matrix 2')
for row1 in range(0,matrix_2.rows):
    add_rows2 = []
    for col1 in range(0,matrix_2.cols):
        print('Enter Matrix[', row1,'][',col1,'] : ')
        # matrix_2.data[row][col] = input(' > ')
        add_rows2.append(int(input(' > ')))
    matrix_2.data.append(add_rows2)

#-------------------------------------------------------



matrix_3.data= []
matrix_3 = matrix_1.adds(matrix_2)
print(matrix_3.data)

matrix_3.data= []
matrix_3 = matrix_1.subs(matrix_2)
print(matrix_3.data)



