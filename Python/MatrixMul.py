a = [[1,2],
     [3,4]]
b = [[1,2],
     [3,4]]

c = [[0,0],
     [0,0]]

# Validate the number of rows in a -- Helpful to ensure we cover all rows in a
for i in range(len(a)):
    # Validate the number of columns in b -- Helpful to ensure we are multiplying a with all columns in b
    for j in range(len(b[0])):
        # Validate the number of rows in b -- Helpful to ensure we cover all rows in b
        for k in range(len(b)):
            # c[i][j] -- we are keeping the result as c[i][j] because all the row column mul
            # must happen after addition of all the elements. j will get updated only after
            # all elements in k has been multiplied
            c[i][j] += a[i][k] * b[k][j] # b[k] because columns should be multipled say 00,10,20 ..etc j will only be updated after the whole column is completed

print c