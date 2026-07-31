class Solution:
    def countSubsets(self, arr):
        # code here
        MOD = 10**9 + 7

 

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        freq = [0] * 31

        for x in arr:

            if x <= 30:

                freq[x] += 1


        mask = [-1] * 31

        mask[1] = 0

 

        for num in range(2, 31):

            x = num

            m = 0

            ok = True

            for i, p in enumerate(primes):

                if x % (p * p) == 0:

                    ok = False

                    break

                if x % p == 0:

                    m |= (1 << i)

            if ok:

                mask[num] = m

 

        dp = [0] * (1 << 10)

        dp[0] = 1

 

        for num in range(2, 31):

            if freq[num] == 0 or mask[num] == -1:

                continue

 

            m = mask[num]

            for s in range((1 << 10) - 1, -1, -1):

                if (s & m) == 0:

                    dp[s | m] = (dp[s | m] + dp[s] * freq[num]) % MOD

 

        ans = 0

        for s in range(1, 1 << 10):

            ans = (ans + dp[s]) % MOD

 

        # Each 1 can be included/excluded independently

        ans = ans * pow(2, freq[1], MOD) % MOD

 

        return ans

