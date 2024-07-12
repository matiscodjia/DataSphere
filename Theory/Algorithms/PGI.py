#Fonction diviser pour régner qui à l'aide d'une réduction simple permet d'obtenir l'indice du plus grand élémment
def pgi(A):
    if len(A) == 1:
        return 0
    else:
        i = A[len(A)-1]
        r = pgi(A[:-1])  # Updated line
        j = A[r]
        if i > j:
            return len(A) - 1
        else:
            return r

        
A = [1,2,5,4]
print(pgi(A))