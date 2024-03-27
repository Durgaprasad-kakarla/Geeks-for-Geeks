//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution
{
public:
    int findShortestPath(vector<vector<int>> &mat)
    {
       // code here
        int n = mat.size();
    int m = mat[0].size();

    // Marking cells adjacent to zeros as -1
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (mat[i][j] == 0) {
                if (i > 0)
                    mat[i - 1][j] = -1;
                if (j > 0)
                    mat[i][j - 1] = -1;
                if (i < n - 1)
                    mat[i + 1][j] = -1;
                if (j < m - 1)
                    mat[i][j + 1] = -1;
            }
        }
    }

    // Resetting marked cells to 0 and creating visited array
    vector<vector<int>> vis(n, vector<int>(m, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (mat[i][j] == -1) {
                mat[i][j] = 0;
                vis[i][j] = 1;
            }
        }
    }

    // Priority queue for Dijkstra's algorithm
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;

    // Pushing cells in the first column with value 1 into the priority queue
    for (int i = 0; i < n; ++i) {
        if (mat[i][0] == 1) {
            pq.push({0, i, 0}); // distance, row, column
            vis[i][0] = 1;
        }
    }

    // Dijkstra's algorithm
    while (!pq.empty()) {
        auto curr = pq.top();
        pq.pop();
        int d = curr[0];
        int row = curr[1];
        int col = curr[2];

        if (col == m - 1)
            return d + 1;

        int dr[] = {-1, 0, 1, 0};
        int dc[] = {0, -1, 0, 1};
        for (int i = 0; i < 4; ++i) {
            int nrow = row + dr[i];
            int ncol = col + dc[i];
            if (nrow >= 0 && nrow < n && ncol >= 0 && ncol < m && mat[nrow][ncol] == 1 && !vis[nrow][ncol]) {
                vis[nrow][ncol] = 1;
                pq.push({d + 1, nrow, ncol});
            }
        }
    }
    return -1;
    }
};

//{ Driver Code Starts.

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int R, C;
        cin >> R >> C;
        vector<vector<int>> mat(R, vector<int>(C));
        for (int i = 0; i < R; i++)
        {
            for (int j = 0; j < C; j++)
            {
                cin >> mat[i][j];
            }
        }

        Solution ob;
        int ans = ob.findShortestPath(mat);
        cout << ans << "\n";
    }
    return 0;
}

// } Driver Code Ends