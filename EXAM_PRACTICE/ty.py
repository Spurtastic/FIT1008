
def rev_int(num: int):
    last_digit = num %10
    print(last_digit)
    rev_num = 0
    while num !=0:
        if last_digit %2>0:
            rev_num+=rev_num*10+last_digit
            print(rev_num)
        num = num/10
    return rev_num
print(rev_int(1234))
