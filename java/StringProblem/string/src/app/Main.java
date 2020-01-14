package app;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws Exception {
        BJ_1152();
    }

    public static void BJ_1032(){
        Scanner sc = new Scanner(System.in);
        int count = Integer.parseInt(sc.nextLine());
        String[] words = new String[count];
        for(int i = 0; i < count; i++){
            words[i] = sc.nextLine();
        }

        int len = words[0].length();
        ArrayList<Integer> answer  = new ArrayList<>();
        for(int i = 0; i < len; i++){
            char temp = words[0].charAt(i);
            for(String word: words){
                if (temp != word.charAt(i)){
                    answer.add(i);
                }
            }
        }

        char[] temp = words[0].toCharArray();
        for(Integer n : answer){
            temp[n] = '?';
        }
        for(int i = 0; i < temp.length; i++){
            System.out.print(temp[i]);
        }
    }
    
    public static void BJ_1100() throws Exception {
        Scanner sc = new Scanner(System.in);
        int count = 0;
        for(int i = 0; i < 8; i++){
            String str = sc.nextLine();
            for(int j = i%2; j < 8; j+=2){
                if(str.charAt(j) == 'F'){
                    count ++;
                }
            }
        }

        System.out.println(count);
    }

    public static void BJ_1152(){
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine().trim();
        if(str.isEmpty()){
            System.out.println(0);
        } else{
            System.out.println(str.split(" ").length);
        }
    }

    public static void BJ_1152_modi(){
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine().trim();
        if(str.isEmpty()){
            System.out.println(0);
        }else{
            String[] results = str.split("\\s+");
            for(String element : results){
                System.out.printf("%s ", element);
            }
        }
    }

    public static void BJ_1157(){
        Scanner sc = new Scanner(System.in);
        String s = sc.next().toLowerCase();
        int[] alpha = new int[26];
        for(int i = 0; i < s.length(); i++){
            alpha[s.charAt(i)-'a']++;
        }

        int maxValue = -1;
        int maxIndex = -1;
        for(int i = 0; i <alpha.length; i++){
            if (maxValue == alpha[i]){
                maxIndex = -1;
            }else if(maxValue < alpha[i]){
                maxIndex = i;
                maxValue = alpha[i];
            }
        }
        if (maxIndex == -1){
            System.out.println("?");
        }else{
            System.out.println((char)(maxIndex + 'A'));
        }
    }

    public static void BJ_1316(){
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int count = 0;
        for(int i =0; i < n; i++){
            String word = sc.nextLine();
            HashMap<Character, Integer> dic = new HashMap<>();
            for (int j = 0; j < word.length(); j++){
                if ( dic.containsKey(word.charAt(j))){
                        if( j > 0 && word.charAt(j) != word.charAt(j-1)){
                            count -= 1;
                            break;
                        }
                }else{
                    dic.put(word.charAt(j), 0);
                }
            }
            count += 1;
        }
        System.out.println(count);
    }


    public static int conv(int a){return 15-a;}

    public static void BJ_1475(){
        Scanner sc = new Scanner(System.in);
        String numword = sc.nextLine();
        int[] bank = new int[10];
        int pack = 1;
        
        for(int i = 0; i < 10; i++) bank[i] = 1;

        for(int i = 0; i < numword.length(); i++){
            int tindex = Integer.parseInt(numword.substring(i, i+1));
            if (tindex == 6 || tindex == 9){
                if (bank[tindex]> 0){
                    bank[tindex]-=1;
                }else{
                    if (bank[conv(tindex)]>0){
                        bank[conv(tindex)]-=1;
                    }
                    else{
                        for(int k = 0; k < 10; k++) bank[k] += 1;
                        bank[tindex] = 0;
                        pack++;
                    }
                }
            }else{
                if (bank[tindex]> 0){
                    bank[tindex]-=1;
                }else{
                    for(int k = 0; k < 10; k++) bank[k] += 1;
                    bank[tindex] = 0;
                    pack++;
                }
            }
        }

        System.out.println(pack);
    }

    

    public static void BJ_1764(){
        Scanner sc = new Scanner(System.in);
        int[] temp= Arrays.stream(sc.nextLine().split(" ")).mapToInt(s->Integer.parseInt(s)).toArray();
        Set<String> unheard = new HashSet<String>();
        Set<String> unseen  = new HashSet<String>();
        for(int i = 0; i <temp[0]; i++)unheard.add(sc.nextLine().trim());
        for(int i = 0; i <temp[1]; i++)unseen.add(sc.nextLine().trim());


        Iterator<String> it = unseen.iterator();
        Set<String> share = new HashSet<>();
        while(it.hasNext()){
            Object a = it.next();
            if(unheard.contains(a)){
                share.add((String)a);
            }
        }

        
        List<String> answer = new ArrayList<String>(share);
        Collections.sort(answer);
        System.out.println(answer.size());
        for(String s : answer){
            System.out.println(s);
        }
    }

    public static void BJ_2902(){
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split("-");
        for(String s : str) System.out.printf("%c", s.charAt(0));
    
    }

    public static void BJ_2908(){
                Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(String s : str){
            int temp = Integer.parseInt((new StringBuffer(s)).reverse().toString());
            heap.add(-temp);
        }
    }

    public static void BJ_2941(){
        String[] part = {"c=" , "c-", "dz=", "d-", "lj", "nj", "s=","z="};

        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        int count = 0;
        for(int i = 0; i < part.length; i++){
            word = word.replace(part[i], "x");
        }
        System.out.println(word.length());

    }


    public static void BJ_10808(){
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        int[] answer = new int[26];
        for (int i = 0; i < 26; i++) answer[i] = 0;
        for (int i = 0; i < word.length(); i++){
            answer[word.charAt(i) - 'a'] += 1;
        }

        System.out.printf("%d", answer[0]);
        for(int i = 1; i < answer.length; i ++){
            System.out.printf(" %d", answer[i]);
        }
    }

    public static void BJ_10809(){
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        int n = word.length();
        int count = 0;
        for(int i = 0; i < n/2; i++){
            if (word.charAt(i) != word.charAt(n-1-i)){
                count++;
                break;
            }
        }
        System.out.println(1-count);
    }

    public static void BJ_10809_2(){
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        String rword = (new StringBuffer(word)).reverse().toString();
        if (word.equals(rword)){
            System.out.println(1);
        }else{
            System.out.println(0);
        }
    }

    public static void BJ_11654(){
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int answer = str.charAt(0);

        System.out.println(answer);
    }

    public static void BJ_2789(){
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        String filter = "CAMBRIDGE";    
        char[] filters = filter.toCharArray();
        for(int i = 0; i < word.length(); i++){
            int count = 0;
            for(int j = 0; j < filters.length; j++){
                if (word.charAt(i) == filters[j]){
                    count ++;
                }
            }
            if (count == 0){
                System.out.print(word.charAt(i));
            }
        }        
    }


    public static void BJ_5598(){
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        for(int i = 0; i < word.length(); i++){
            int a = word.charAt(i) - 65;
            a =  a - 3 + 26;
            a %= 26;
            a += 65;
            System.out.print((char)a);
        }
    }

    public static void BJ_1120(){
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        String target  = input[1];
        String source  = input[0];
        List<Integer> list =  new ArrayList<>();
        for(int k = 0; k < target.length()-source.length()+1; k++){
            String temp = target.substring(k, k+source.length());
            int count = 0;
            for(int i = 0; i < temp.length(); i++){
                if (temp.charAt(i) != source.charAt(i)) count++;
            }
            list.add(count);
        }
        Collections.sort(list);
        System.out.println(list.get(0));
  
    }

 
    public static void BJ_10987(){
        String[] consonant = {"a","e","i","o","u"};
        Set<String> set = new HashSet<>(Arrays.asList(consonant));
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        int n = word.length();
        int count = 0;
        for(int i = 0; i < n ; i++){
            if (set.contains(word.subSequence(i, i+1))){
                count ++;
            }
        }
        System.out.println(count);
    }


    public static void BJ_2864_dif56(){
        Scanner sc = new Scanner(System.in);
        String[] nums = sc.nextLine().split(" ");
        int maxim = (Integer.parseInt(nums[0].replace("5", "6"))
                             + Integer.parseInt(nums[1].replace("5", "6"))) ;
        int minim = (Integer.parseInt(nums[0].replace("6", "5"))
                             + Integer.parseInt(nums[1].replace("6", "5"))) ;    
                             
        System.out.println(minim + " " + maxim);
    }

    public static void BJ_11656_prefixArray(){
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        Set<String> set = new  HashSet<String>();
        int n = word.length();
        for(int i = 0; i< n; i++){
            set.add(word.substring(i, n));
        }
        List<String> answer = new ArrayList<>(set);
        Collections.sort(answer);
        for(String s : answer){
            System.out.println(s);
        }
    }

    public static void ModulusTest(){
        for(int i = -10; i <= 10; i++){
            System.out.println(i%5);
        }
    }



}