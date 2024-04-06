def selection (arr1):
    for i in range(len(arr1)-1):
        for j in range(i+1,len(arr1)):
            if(arr1[i]>arr1[j]):
                arr1[i], arr1[j] = arr1[j], arr1[i]
  

arr1 = [10,5,50,99,60,45]
selection(arr1)
print('sorted array is:', arr1)