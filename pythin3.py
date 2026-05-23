s = "hello word"
s1 = {}
for i in s.split():
    count = 0
    for j in s.split():
        if i == j:
            count += 1
        s1[i] = count
    print(s1)