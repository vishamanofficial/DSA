reverseNum = 0
x=44100
while( x != 0 ):
    lastdigit = x%10
    x//=10
    reverseNum = reverseNum*10 + lastdigit
print(reverseNum)