class Solution:
    def countPrimes(self, n: int) -> int:
        """
        go through every integer from 0 to N and check if it is prime, if it is then we increment our count
            issue: the way we check for prime
            
            # we can skip even numbers except 2 since they are all not prime
            
            method 1: is to go up to num / 2 to see if num % (every number less than num / 2) is 0
            we do this for every number so that is N^2 still
            
            method 2: is to go up to sqrt(num) since obviously anything greater wont work
            N^1.5 is still bad
            
            method3 :kekW:
            
            starting with the multiples up to sqrt(N) we check if numbers are already prime
                generate multiples of the prime and mark them off
            we can use memory (array) to see if we marked off already
            
            then we count primes in our memory
        """
        
        # 0 and 1 are not prime
        isPrime = [False if i == 0 or i == 1 else True for i in range(n)]
        
        # while we are less than sqrt(n)
        i = 2
        while i * i < n:

            # if the current value is prime then we check the every i interval to mark off numbers that are multiples of that prime
            if isPrime[i]:
                j = i * i
                while j < n:
                    isPrime[j] = False
                    j += i
                    
            i += 1
        
        # we are done checking, lets get the count
        prime_count = 0
        for curr in range(len(isPrime)):
            if isPrime[curr] == True:
                prime_count += 1
        
        return prime_count
