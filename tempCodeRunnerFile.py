i=1
n=int(input("enter the value :"))
def fn(i,n):
    if (i>n):
        return
    print("aman")
    fn(i+1, n)
fn(i,n)