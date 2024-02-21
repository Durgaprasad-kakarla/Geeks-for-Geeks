//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
#define ll long long
const int mod = 1003;
class Solution{
public:
    int countWays(int n, string exp){
        // code here
        vector<vector<vector<ll>>> dp(n, vector<vector<ll>>(n, vector<ll>(2, 0)));
        
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j <= n - 1; j++) {
                // Base case 1: i > j is an invalid case, so continue.
                if (i > j) continue;
                
                for (int isTrue = 0; isTrue <= 1; isTrue++) {
                    // Base case 2: i == j, evaluate the single character.
                    if (i == j) {
                        if (isTrue == 1) dp[i][j][isTrue] = exp[i] == 'T';
                        else dp[i][j][isTrue] = exp[i] == 'F';
                        continue;
                    }
    
                    // Recurrence logic:
                    ll ways = 0;
                    for (int ind = i + 1; ind <= j - 1; ind += 2) {
                        ll lT = dp[i][ind - 1][1];
                        ll lF = dp[i][ind - 1][0];
                        ll rT = dp[ind + 1][j][1];
                        ll rF = dp[ind + 1][j][0];
    
                        if (exp[ind] == '&') {
                            if (isTrue) ways = (ways + (lT * rT) % mod) % mod;
                            else ways = (ways + (lF * rT) % mod + (lT * rF) % mod + (lF * rF) % mod) % mod;
                        }
                        else if (exp[ind] == '|') {
                            if (isTrue) ways = (ways + (lF * rT) % mod + (lT * rF) % mod + (lT * rT) % mod) % mod;
                            else ways = (ways + (lF * rF) % mod) % mod;
                        }
                        else {
                            if (isTrue) ways = (ways + (lF * rT) % mod + (lT * rF) % mod) % mod;
                            else ways = (ways + (lF * rF) % mod + (lT * rT) % mod) % mod;
                        }
                    }
                    dp[i][j][isTrue] = ways;
                }
            }
        }
        return dp[0][n - 1][1];
        }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string s;
        cin>>s;
        
        Solution ob;
        cout<<ob.countWays(n, s)<<"\n";
    }
    return 0;
}
// } Driver Code Ends