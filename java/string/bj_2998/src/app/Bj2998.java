package app;

import java.util.Scanner;

public class Bj2998 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        String numstr = sc.nextLine();
        int strlen = numstr.length();
        switch(strlen%3){
            case 1:
                numstr = "0".concat(numstr);
            case 2:
                numstr = "0".concat(numstr);
                break;
        }

        String answer = "";
        for(int i = 0; i < numstr.length(); i+=3){
            int digit = 4*(numstr.charAt(i)-'0');
            digit += 2*(numstr.charAt(i+1)-'0');
            digit += 1*(numstr.charAt(i+2)-'0');
            
            answer += digit;
        }

        System.out.println(answer);
        sc.close();
    }
}