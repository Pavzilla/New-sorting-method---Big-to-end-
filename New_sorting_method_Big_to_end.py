list1 = [1, 5, 4, 8, 6, 20, 100, 4, 50, 255, 41, 758, 0 ]
n=len(list1)

while True:
    per = False
    for i in range(n-1):
        if list1[i] > list1[i+1]:
             list1.append(list1[i])
             list1.pop(i)               
             per = True
    if not per:
        break
print(list1)

