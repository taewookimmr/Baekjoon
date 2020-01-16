package app;

import java.util.Scanner;

public class Bj1371 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        char[] arr = new char[26];
        int max = 0;
        while(sc.hasNextLine()){
            char[] input = sc.nextLine().toCharArray();
            System.out.println(input);
            for(int i = 0; i<input.length; i++){
                if(input[i] != ' '){
                    max = Math.max(max, ++arr[input[i]-'a']);
                }
            }
        }
        for (int i =0; i < arr.length;i++){
            if(arr[i]==max){
                sb.append((char)('a' + i));
            }
        }
        sb.append(System.lineSeparator());
        System.out.println(sb.toString());
    }
}