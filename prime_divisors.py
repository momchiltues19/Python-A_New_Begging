n=int(input('Input positive n: '))
c=0
i=2
while (i<=n):
    if n%i==0:
        m=2
        while i%m!=0:
            m=m+1
        if i==m:
            print (i,' is a prime divider')
            c=c+1
    i=i+1
print ('the count of prime divisors is ', c)
