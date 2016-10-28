def general_poly (L):
    
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    import math

    def calculate_polynomial(base):

        length = len(L)
        sum = 0

        for i in range(0, length):
            k = length-1-i;
            sum += L[i]*math.pow(base, k)

        if sum.is_integer():
            return int(sum)
        else:
            return sum

    
    return calculate_polynomial




# test cases

L= [1,2,3,4]
base = 10
print(general_poly(L)(base))

L= [5,0]
base = 16
print(general_poly(L)(base))

L= [1,0,1,1]
base = 2
print(general_poly(L)(base))


L= [1,2,3,4]
base = 1.3
print(general_poly(L)(base))

L= [11,12,13]
base = 0.5
print(general_poly(L)(base))
