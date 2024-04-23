//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++
class Solution
{
public:
    int ways(int x, int y)
    {
        //code here.
        const int MOD = 1000000007;
    vector<vector<int>> dp(x + 1, vector<int>(y + 1, 0));

    for (int i = 0; i <= x; i++) {
        for (int j = 0; j <= y; j++) {
            int up = 0, left = 0;
            if (i == 0 && j == 0) {
                dp[i][j] = 1;
                continue;
            }
            if (i > 0) {
                up = dp[i - 1][j];
            }
            if (j > 0) {
                left = dp[i][j - 1];
            }
            dp[i][j] = (up + left) % MOD;
        }
    }
    return dp[x][y];
    }
};


//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int x,y;
        cin>>x>>y;
        Solution ob;
        cout<<ob.ways(x,y)<<endl;
    }
	return 0;
}

// } Driver Code Ends