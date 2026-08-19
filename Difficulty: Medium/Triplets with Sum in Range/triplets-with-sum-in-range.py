class Solution:
   
    def countTriplets(self, arr: list[int], low: int, high: int) -> int:
        # code here
        n = len(arr)
        arr.sort()

        def at_most(max_sum: int) -> int:
            count = 0

            for i in range(n - 2):
                j = i + 1
                k = n - 1

                while j < k:
                    total = arr[i] + arr[j] + arr[k]

                    if total <= max_sum:
                        count += k - j
                        j += 1
                    else:
                        k -= 1

            return count

        return at_most(r) - at_most(l - 1)