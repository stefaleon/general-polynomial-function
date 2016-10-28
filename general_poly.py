def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    import math

    def polynomial(x):
        length = len(L)
        sum = 0
        for i in range(0, length):
            k = length-1-i;
            sum += L[i]*math.pow(x, k)
        if sum.is_integer():
            return int(sum)
        else:
            return sum
    
    return polynomial



L=[1,2,3,4]
print(len(L))

print(general_poly(L)(10))
