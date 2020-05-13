def insertion_sort(arr):
    for i in range(1, len(arr)):
        #print(i)
        if arr[i] < arr[i-1]:
            #print(f"swapping {arr[i]}")
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break

if __name__ == "__main__":
    print("Test")
    arr1=[3,1,5,2]
    insertion_sort(arr1)
    print(arr1, len(arr1))
    import random
    arr2 = random.sample(range(0, 30), 10)
    print(arr2)
    insertion_sort(arr2)
    print(arr2)