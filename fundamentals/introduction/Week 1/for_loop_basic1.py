# 1
for i in range(151):
    print(i)

# 2
for i in range(5, 1001, 5):
    print (i)

# 3
for i in range(1,101):
    if i%5 == 0:
        print("Coding Dojo")
    else:
        print(i)

# 4
sum = 0
for i in range(1, 500000+1, 2):
    sum+=i
print(sum)

# 5
x = 2018
while x >= 0:
    print(x)
    x -= 4

# 6
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1):
    if i%mult == 0:
        print(i)