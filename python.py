#Second largest in array
def second_largest(arr):
    largest = arr[0]
    second_largest = arr[0]
    for i in range(0,len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    for i in range(0,len(arr)):
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    return second_largest
if __name__ == "__main__":
    arr = [3,1,4,1,5,9,2,6,20]
    print(second_largest(arr))







