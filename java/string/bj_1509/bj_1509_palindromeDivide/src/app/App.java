package app;
import java.util.Scanner;

public class App {

    public static boolean[][] answerAry;
	
    public static void main(String[] args) {
        String s = (new Scanner(System.in)).nextLine().trim();
        int n = s.length();
        
        s = " " + s;
        answerAry = new boolean[n+1][n+1];

        for(int i = 1; i <= n; i++) {
            answerAry[i][i] = true;			
        }

        for(int i = 1; i < n; i++) {
            if(s.charAt(i) == s.charAt(i+1))
                answerAry[i][i+1] = answerAry[i+1][i] = true;
        }		
		
        for(int i = 2; i < n; i++) {
            for(int j = 1; j <= n - i; j++) {
                if(s.charAt(j) == s.charAt(j+i) && answerAry[j+1][j+i-1]) {
                    answerAry[j][j+i] = answerAry[j+i][j] = true;
                }	
            }
        }

        int[] dp = new int[n+1];
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= i; j++) {
                if(answerAry[j][i]) {
                    if(dp[i] == 0 || dp[i] > dp[j-1] + 1) {
                        dp[i] = dp[j-1] + 1;
                    }
                }
            }
        }
        System.out.println(dp[n]);
    }
}