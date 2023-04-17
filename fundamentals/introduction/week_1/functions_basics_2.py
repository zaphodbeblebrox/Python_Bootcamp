# 1
def countdown(num):
    countdown_list = []
    for i in range(num, -1, -1):
        countdown_list.append(i)
    return countdown_list

print(countdown(5))

# 2
def print_return(arr):
    print(arr[0])
    return arr[1]

print(print_return([1,2]))

# 3
def firstPlusLength(arr):
    return arr[0] + len(arr)

print(firstPlusLength([1,2,3,4,5]))

# 4
def greaterThanSecond(arr):
    numbersGreaterThanSecond = 0
    newArr = []
    if len(arr) < 2:
        return False
    for x in arr:
        if x > arr[1]:
            numbersGreaterThanSecond += 1
            newArr.append(x)
    print(numbersGreaterThanSecond)
    return newArr

print(greaterThanSecond([3]))
print(greaterThanSecond([5,2,3,2,1,4]))

# 5
def thisThat(size, value):
    arr = []
    for i in range(size):
        arr.append(value)
    return arr

print(thisThat(4,7))