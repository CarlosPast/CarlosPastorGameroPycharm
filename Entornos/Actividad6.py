

def actividad6():

    a = [[1,2,3],[4,5,6]]
    b = [[-1,0],[0,1],[1,1]]
    print(" / " + str(a[0]) + ' \ ')
    print(' \ ' + str(a[1]) + " /")
    print("")
    print(" / " + str(b[0]) + ' \ ')
    print("|  " + str(b[1]) + "  |")
    print(' \ ' + str(b[2]) + " /")
    result = [[0,0],[0,0]]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    for i in range(len(result)):
        result[i] = tuple(result[i])
    result = tuple(result)

    print("")
    print(" / " + str(result[0]) + ' \ ')
    print(' \ ' + str(result[1]) + " /")


actividad6()