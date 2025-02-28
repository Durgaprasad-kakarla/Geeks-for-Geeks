//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;


// } Driver Code Ends


class Solution {
    public int evaluate(String[] arr) {
        // code here
        int n = arr.length;
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            String token = arr[i];

            if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
                if (stack.size() > 1) {
                    int num1 = stack.pop();
                    int num2 = stack.pop();
                    
                    int result = 0;
                    switch (token) {
                        case "+":
                            result = num2 + num1;
                            break;
                        case "-":
                            result = num2 - num1;
                            break;
                        case "*":
                            result = num2 * num1;
                            break;
                        case "/":
                            result = num2 / num1; // Integer division
                            break;
                    }
                    stack.push(result);
                }
            } else {
                stack.push(Integer.parseInt(token)); // Convert operand to int
            }
        }
        return stack.peek();
    }
}


//{ Driver Code Starts.

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line = reader.readLine();
        int t = Integer.parseInt(line);
        while (t-- > 0) {
            line = reader.readLine();
            String[] arr = line.split(" ");
            Solution solution = new Solution();
            System.out.println(solution.evaluate(arr));
            System.out.println("~");
        }
    }
}

// } Driver Code Ends