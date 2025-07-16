import math
class Solution:
    def countNumbers(self, n):
        # code here
        def sieve_of_eratos(n):
            sieve=[1]*(n+1)
            sieve[0],sieve[1]=0,0
            i=2
            while i*i<=n:
                if sieve[i]==1:
                    j=i*i
                    while j<=n:
                        sieve[j]=0
                        j+=i
                i+=1
            primes=[]
            for i in range(n):
                if sieve[i]==1:
                    primes.append(i)
            return primes
        limit=int(math.sqrt(n))+2
        primes=sieve_of_eratos(limit)
        cnt=0
        for i in primes:
            if i**8<=n:
                cnt+=1
            else:
                break
        k=len(primes)
        for i in range(k):
            for j in range(i+1,k):
                if (primes[i]**2)*(primes[j]**2)<=n:
                    cnt+=1
                else:
                    break
        return cnt