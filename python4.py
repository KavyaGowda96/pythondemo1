#Sum Pairs
if __name__ == "__main__":
    arr = input().split()
    print(arr)
    target = int(input("enter the target value"))
    for i in arr:
        for j in arr:
            if i + j == target:
                print(i + j)
