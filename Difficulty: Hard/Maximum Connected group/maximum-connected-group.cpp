//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++


class DisjointSet {
public:
    vector<int> parent, size;

    DisjointSet(int n) {
        parent.resize(n);
        size.resize(n);
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    int findUParent(int node) {
        if (node == parent[node]) {
            return node;
        }
        return parent[node] = findUParent(parent[node]);
    }

    void unionBySize(int u, int v) {
        int pu = findUParent(u);
        int pv = findUParent(v);
        if (pu != pv) {
            if (size[pu] < size[pv]) {
                swap(pu, pv);
            }
            parent[pv] = pu;
            size[pu] += size[pv];
        }
    }
};
class Solution {
  public:
    int MaxConnection(vector<vector<int>>& mat) {
        // code here
        int n = mat.size();
    int m = mat[0].size();
    DisjointSet ds(m * n);
    vector<vector<int>> vis(n, vector<int>(m, 0));
    int dr[] = {-1, 0, 1, 0};
    int dc[] = {0, -1, 0, 1};

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (mat[i][j] == 1 && !vis[i][j]) {
                int node = i * m + j;
                vis[i][j] = 1;
                for (int x = 0; x < 4; ++x) {
                    int nrow = i + dr[x];
                    int ncol = j + dc[x];
                    if (nrow >= 0 && ncol >= 0 && nrow < n && ncol < m && vis[nrow][ncol]) {
                        int new_node = nrow * m + ncol;
                        if (ds.findUParent(node) != ds.findUParent(new_node)) {
                            ds.unionBySize(node, new_node);
                        }
                    }
                }
            }
        }
    }

    int maxi = *max_element(ds.size.begin(), ds.size.end());
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (!vis[i][j]) {
                int node = i * m + j;
                int tot = 0;
                set<int> st;
                for (int x = 0; x < 4; ++x) {
                    int nrow = i + dr[x];
                    int ncol = j + dc[x];
                    if (nrow >= 0 && ncol >= 0 && nrow < n && ncol < m && vis[nrow][ncol]) {
                        int new_node = nrow * m + ncol;
                        int parent = ds.findUParent(new_node);
                        if (st.find(parent) == st.end()) {
                            tot += ds.size[parent];
                            st.insert(parent);
                        }
                    }
                }
                maxi = max(maxi, tot + 1);
            }
        }
    }

    return maxi;
    }
};


//{ Driver Code Starts.
int main() {

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> grid(n, vector<int>(n));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> grid[i][j];
            }
        }

        Solution obj;
        cout << obj.MaxConnection(grid) << "\n";
    }
}

// } Driver Code Ends