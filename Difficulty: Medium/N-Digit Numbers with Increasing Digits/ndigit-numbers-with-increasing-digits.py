class Solution:
    def increasingNumbers(self, n):
        # code here
        def dfs(digit: int=1, remaining: int=n, acc: int=0, output: list[int]=[]):
            if remaining == 0:
                output.append(acc)
                return output
            remaining -= 1
            acc *= 10
            for curr_digit in range(digit, 9 + 1 - remaining):
                dfs(curr_digit + 1, remaining, acc + curr_digit)
            return output

        return dfs(0 if n == 1 else 1)
