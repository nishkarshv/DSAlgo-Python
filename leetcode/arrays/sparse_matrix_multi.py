'''
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

'''
def multiply(A, B):
    '''
    if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        C = [[0 for _ in range(l)] for _ in range(m)]
        tableB = {}
        for k, row in enumerate(B):
            tableB[k] = {}
            for j, eleB in enumerate(row):
                if eleB: tableB[k][j] = eleB
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in tableB[k].iteritems():
                        C[i][j] += eleA * eleB
        return C
    '''
    
    if A is None or B is None:
        return None
    Arow,Acol = len(A), len(A[0])
    Brow, Bcol = len(B), len(B[0])
        
    if Brow!= Acol:
        raise Exception("Error")
    X = [[0 for _ in range(Bcol)] for _ in range(Arow)]
    print(X)
    tableB = {}
    for i, row in enumerate(B):
        tableB[i] = {}
        for j, Bval in enumerate(row):
            if Bval:
                tableB[i][j] = Bval
    for i, row in enumerate(A):
        for j, Aval in enumerate(row):
            if Aval:
                for k, Bval in tableB[j].items():
                    X[i][k]+=Aval*Bval
    return X

def multiply_Optimized(A, B):
    if A is None or B is None:
        return None
    mr = len(A)
    mc = len(A[0])
    nr = len(B)
    nc = len(B[0])
    if nr != mc:
        raise Exception("Error")
    X = [[0 for _ in range(nc)] for _ in range(mr)]
    for i, row in enumerate(A):
        for k, eleA in enumerate(row):
            if eleA:
                for j, eleB in enumerate(B[k]):
                    if eleB:
                        X[i][j]+=eleA*eleB
    return X
    
                
    
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

print(multiply(A, B))
print(multiply_Optimized(A, B))