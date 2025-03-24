n=int(input("enter the value :"))
def fn(n):
    if (n<1):
        return
    print(n)
    fn(n-1)
fn(n)