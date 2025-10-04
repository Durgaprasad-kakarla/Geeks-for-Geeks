class Solution:
    def findExpr(self, s, target):
        # code here
        ans = []
        n = len(s)

        def dfs(ind, expr, cur_val, last_val):
            # If end of string reached
            if ind == n:
                if cur_val == target:
                    ans.append("".join(expr))
                return
            
            # Extend number one digit at a time
            num = 0
            for i in range(ind, n):
                # skip numbers with leading zeros
                if i > ind and s[ind] == "0":
                    break
                num = num * 10 + int(s[i])
                num_str = s[ind:i+1]

                if ind == 0:
                    # first number, no operator
                    dfs(i+1, [num_str], num, num)
                else:
                    # +
                    dfs(i+1, expr + ["+", num_str], cur_val + num, num)
                    # -
                    dfs(i+1, expr + ["-", num_str], cur_val - num, -num)
                    # *
                    dfs(i+1, expr + ["*", num_str], cur_val - last_val + last_val * num, last_val * num)

        dfs(0, [], 0, 0)
        return ans
                    
                
        