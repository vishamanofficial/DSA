arr = [1,2,3,1,2,2,1]
def fn(number):
    global count 
    count = 0
    for i in arr:
        if (arr[i]==number):
            count = count + 1
        return count
print(count)
fn(1) 