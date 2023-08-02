
def arraymap (func,array):
    return [func(element) for element in array]
def invert_sign(num):
    return -num
array = [1,2,3,-4,-9,-1]
inverted_sign = arraymap(invert_sign,array)
print(inverted_sign)


