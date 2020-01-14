package app;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BJ_11286();
    }
    
    public static void BJ_11286(){
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        PriorityQueue<Custonum> heap = new PriorityQueue<>();
        for(int i=0; i<n; i++){
            int m = Integer.parseInt(sc.nextLine());
            if (m == 0){
                if(heap.isEmpty()){
                    System.out.println(0);
                }else{
                    Custonum temp = heap.poll();
                    System.out.println(temp.num * (temp.sign ? 1: -1));
                }
            }else{
                heap.add(new Custonum(m) );
            }
        }
    }
    static class Custonum implements Comparable<Custonum>{

        int num;
        boolean sign;

        public Custonum(int num){
            this.num = Math.abs(num);
            this.sign = num >= 0 ? true: false;
        }

        @Override
        public int compareTo(Custonum n) {
            if(this.num > n.num){
                return 1 ;
            }else if(this.num == n.num){
                if(this.sign && !n.sign) return 1;
            }
            return -1;
        }
        
    }
    
    public static void BJ_1766() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        ArrayList<Integer>[] list = new ArrayList[N+1];
        for(int i = 1; i <= N; i++){
            list[i] = new ArrayList<Integer>();
        }
        int[] indegree = new int[N+1];
        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            list[x].add(y);
            indegree[y]++ ;
        }

        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int i = 1; i<=N; i++){
            if(indegree[i]== 0) heap.add(i);
        }

        StringBuffer ans = new StringBuffer();
        while(!heap.isEmpty()){
            int current = heap.poll();
            ans.append(current + " ");
            ArrayList<Integer> nextList = list[current];
            for(Integer next : nextList){
                indegree[next]--;
                if(indegree[next] == 0){
                    heap.add(next);
                }
            }
        }

        System.out.println(ans);
    }

    public static void BJ_11279(){
        Scanner sc = new Scanner(System.in);
        int n  = sc.nextInt();
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int i = 0; i < n; i ++){
            int num = sc.nextInt();
            if(num != 0){
                heap.offer(-num);
            }else{
                if(heap.size() == 0){
                    System.out.println(0);
                }else{
                    System.out.println(-heap.poll());
                }
            }
        }
    }

    public static void BJ_1927(){
        Scanner sc = new Scanner(System.in);
        int n  = sc.nextInt();
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int i = 0; i < n; i ++){
            int num = sc.nextInt();
            if(num != 0){
                heap.offer(num);
            }else{
                if(heap.size() == 0){
                    System.out.println(0);
                }else{
                    System.out.println(heap.poll());
                }
            }
        }
    }

}