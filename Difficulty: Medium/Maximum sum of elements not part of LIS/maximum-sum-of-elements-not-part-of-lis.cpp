class Solution {
  public:
    int nonLisMaxSum(vector<int>& arr) {
        // code here
        int n = arr.size();
    vector<int> dp(n, 1);
    int maxi = 1;
    
    // Compute LIS
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (arr[i] > arr[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
                maxi = max(maxi, dp[i]);
            }
        }
    }

    // Total sum
    int sm = 0;
    for (int val : arr)
        sm += val;

    // Subtract elements that contributed to LIS
    for (int i = n - 1; i >= 0; --i) {
        if (dp[i] == maxi) {
            sm -= arr[i];
            maxi--;
        }
    }

    return sm;
    }
};