def function(path, param):
    n = param['noNodes']
    matrix = param['matrix']
    sum = 0
    for i in range(1,n):
        sum += matrix[path[i-1]][path[i]]
    sum += matrix[path[0]][path[n-1]]
    return sum
