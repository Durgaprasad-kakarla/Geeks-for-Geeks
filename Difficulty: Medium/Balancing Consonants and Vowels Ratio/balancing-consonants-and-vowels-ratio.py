from collections import defaultdict
class Solution:
    def countBalanced(self, arr):
        vowels = set("aeiou")
        prefix_balances = defaultdict(int, {0: 1})
        curr_balance = count = 0
        for word in arr:
            curr_balance += len(word) - 2 * sum(c in vowels for c in word)
            count += prefix_balances[curr_balance]
            prefix_balances[curr_balance] += 1
        return count
        
