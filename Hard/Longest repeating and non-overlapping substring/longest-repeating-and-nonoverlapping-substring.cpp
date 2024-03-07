//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    string longestSubstring(string s, int n) {
        // code here
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
    string res = "";
    int res_length = 0;
    int index = 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            if (s[i - 1] == s[j - 1] && dp[i - 1][j - 1] < j - i) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
                if (dp[i][j] > res_length) {
                    res_length = dp[i][j];
                    index = max(i, index);
                }
            } else {
                dp[i][j] = 0;
            }
        }
    }

    if (res_length > 0) {
        for (int i = index - res_length + 1; i <= index; ++i) {
            res += s[i - 1];
        }
    }

    return (res == "") ? "-1" : res;

    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        string S;

        cin >> N;
        cin >> S;

        Solution ob;
        cout << ob.longestSubstring(S, N) << endl;
    }
    return 0;
}
// } Driver Code Ends