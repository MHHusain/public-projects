def print_digit(start, end):
    count = [0,0,0,0,0,0,0,0,0,0]
    for each_number in range(start,end +1):
        while each_number > 0:
            
            remainder = each_number % 10
            count[remainder] += 1
            each_number //= 10
            print(f"{remainder} ",end="")
    return count
print(print_digit(120,136))
