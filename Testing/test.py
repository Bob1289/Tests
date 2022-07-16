
import math

if __name__ == '__main__':
    nums = [21,4,7]
    res = 0
    count = 0
    numbers = []

    for num in nums:
        for i in range(1, math.floor(math.sqrt(num)) + 1):
            if num % i == 0:
                numbers.append(num//i)
                if i != (num//i):
                    numbers.append(i)
            if len(numbers) > 4:    
                break
                    
        if len(numbers) == 4:
            res += sum(numbers)
            numbers = []

    return res
