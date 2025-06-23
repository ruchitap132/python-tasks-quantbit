

def is_disarium(num):
    digits = str(num)
    total = 0
    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)
    return total == num


print(is_disarium(135))
print(is_disarium(175))  
print(is_disarium(89))   
print(is_disarium(123))

