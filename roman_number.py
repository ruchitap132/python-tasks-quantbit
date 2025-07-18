

def int_to_roman(num):
    val = [1000, 900, 500, 400,
           100, 90, 50, 40,
           10, 9, 5, 4, 1]
    
    syms = ['M', 'CM', 'D', 'CD',
            'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV', 'I']
    
    result = ''
    
    for i in range(len(val)):
        count = num // val[i]
        result += syms[i] * count
        num %= val[i]
    
    return result



print(int_to_roman(4))  
