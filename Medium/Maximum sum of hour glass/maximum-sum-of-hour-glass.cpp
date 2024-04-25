//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int findMaxSum(int n, int m, vector<vector<int>> mat) {
        // code here
        int maxi = -INT_MAX;
    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < m; ++col) {
            int dr[] = {-1, -1, -1, 1, 1, 1};
            int dc[] = {-1, 0, 1, -1, 0, 1};
            int flag = 0;
            int sm = 0;
            for (int i = 0; i < 6; ++i) {
                int nrow = row + dr[i];
                int ncol = col + dc[i];
                if (nrow >= 0 && ncol >= 0 && nrow < n && ncol < m) {
                    sm += mat[nrow][ncol];
                } else {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                maxi = max(maxi, sm + mat[row][col]);
            }
        }
    }
    return maxi != -INT_MAX ? maxi : -1;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N, M, i, j;
        cin >> N >> M;
        vector<vector<int>> Mat(N, vector<int>(M));
        for (i = 0; i < N; i++)
            for (j = 0; j < M; j++) cin >> Mat[i][j];
        Solution ob;
        cout << ob.findMaxSum(N, M, Mat) << "\n";
    }
}
// } Driver Code Ends