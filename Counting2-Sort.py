length = int(input())
numbers = [int(x) for x in raw_input().split()]
numbers.sort()
print(' '.join(map(str, numbers)))