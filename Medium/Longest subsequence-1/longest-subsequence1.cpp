//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

class Array {
  public:
    template <class T>
    static void input(vector<T> &A, int n) {
        for (int i = 0; i < n; i++) {
            scanf("%d ", &A[i]);
        }
    }

    template <class T>
    static void print(vector<T> &A) {
        for (int i = 0; i < A.size(); i++) {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends

class Solution {
  public:
    int longestSubseq(int n, vector<int> &arr) {
        // code here
        vector<int> pre(n + 1, 0);
    for (int ind = 1; ind <= n; ++ind) {
        std::vector<int> curr(n + 1, 0);
        for (int prev = -1; prev < n; ++prev) {
            int l = 0;
            if (prev == -1) {
                l = 1 + pre[ind];
            } else if (std::abs(arr[ind - 1] - arr[prev]) == 1) {
                l = 1 + pre[ind];
            }
            int r = pre[prev + 1];
            curr[prev + 1] = std::max(l, r);
        }
        pre = curr;
    }
    return pre[0];
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {

        int n;
        scanf("%d", &n);

        vector<int> a(n);
        Array::input(a, n);

        Solution obj;
        int res = obj.longestSubseq(n, a);

        cout << res << endl;
    }
}

// } Driver Code Ends