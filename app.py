print("Hello GitHub")

arr = [4,3,2,5,1]

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)