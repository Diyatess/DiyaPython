n=input("Enter a string:")
dict1={}
lis=n.split(' ')
print(lis)
for i in lis:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
for k, v in dict1.items():
    print(k, v)
