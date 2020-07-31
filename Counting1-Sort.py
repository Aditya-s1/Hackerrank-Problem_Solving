def count_values(length, numbers, counts):
    for i in range(length):
        number = numbers[i]
        counts[number] += 1
    return counts    

length = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort()
counts = [0] * 100
count_values(length, numbers, counts)
print(' '.join(map(str, counts)))