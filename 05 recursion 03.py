# sum of first n numbers

print("sum of first n numbers")
def fn( i , sum):
    if (i<1):
        print(sum)
        return
    fn(i-1, sum + i)
fn(10,0)


def fn1(n):
    if (n==0):
        return 0
    return n + fn1(n-1)
print(fn1(5))
