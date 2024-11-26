//{ Driver Code Starts
import java.io.*;
import java.util.*;

class Sorting {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int g = 0; g < t; g++) {
            String[] str = (br.readLine()).trim().split(" ");
            int arr[] = new int[str.length];
            for (int i = 0; i < str.length; i++) arr[i] = Integer.parseInt(str[i]);
            System.out.println(new Solution().circularSubarraySum(arr));
            // System.out.println("~");
        }
    }
}
// } Driver Code Ends


class Solution {

    // a: input array
    // n: size of array
    // Function to find maximum circular subarray sum.
    public int circularSubarraySum(int arr[]) {

        // Your code here
        int n = arr.length;

        // Step 1: Find the maximum subarray sum using Kadane's algorithm
        int sm = 0, maxi = 0;
        for (int i = 0; i < n; i++) {
            sm += arr[i];
            if (sm < 0) {
                sm = 0;
            }
            maxi = Math.max(maxi, sm);
        }

        // Step 2: Prepare prefix and suffix arrays
        int[] pref = new int[n];
        int[] suff = new int[n];
        int[] prefMax = new int[n];
        int[] suffMax = new int[n];

        pref[0] = arr[0];
        prefMax[0] = arr[0];
        suff[n - 1] = arr[n - 1];
        suffMax[n - 1] = arr[n - 1];

        // Step 3: Calculate prefix, suffix, and their maximums
        for (int i = 1; i < n; i++) {
            pref[i] = pref[i - 1] + arr[i];
            prefMax[i] = Math.max(prefMax[i - 1], pref[i]);

            suff[n - i - 1] = suff[n - i] + arr[n - i - 1];
            suffMax[n - i - 1] = Math.max(suffMax[n - i], suff[n - i - 1]);
        }

        // Step 4: Combine prefix max and suffix max for circular subarray
        for (int i = 1; i < n - 1; i++) {
            maxi = Math.max(maxi, prefMax[i - 1] + suffMax[i + 1]);
        }

        return maxi;
    }
}
