# armstrong numbers
      
n = 371
dup = n
sum = 0
while (n>0):
      ld = n%10
      sum = sum + (ld*ld*ld)
      n//=10
if(sum==dup):
      print("Armstrong")
else:
      print("Not a Armstrong")