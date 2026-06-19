class Solution:
    def optimalArray(self, arr):
        # code here
        n = len(arr)

        # Prefix sums
        pref = [0] * n
        pref[0] = arr[0]

        for i in range(1, n):
            pref[i] = pref[i - 1] + arr[i]

        ans = []

        for i in range(n):
            k = i // 2
            med = arr[k]

            sumL = pref[k - 1] if k > 0 else 0
            sumR = pref[i] - pref[k]

            left_cost = med * k - sumL
            right_cost = sumR - med * (i - k)

            ans.append(left_cost + right_cost)

        return ans