A = 14741
X = 1
C = 757
M = 77777677777

def rand(mod):
    global A, X, C, M
    X = (A*X + C) % M
    return X%mod