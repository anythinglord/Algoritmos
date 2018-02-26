import java.util.Scanner;

public class Fibonacci {

    public int intFib(int n) {
        int before = 0, actual = 1, after = 0;
        for (int i = 0; i < n; i++) {
            after = actual + before;
            actual = before;
            before = after;
        }
        return after;
    }

    public byte byFib(int n) {
        byte before = 0, actual = 1, after = 0;
        for (int i = 0; i < n; i++) {
            after = (byte) (actual + before);
            actual =  before;
            before = after;
        }
        return after;

    }

    public short shFib(int n) {
        short before = 0, after = 0;
        short actual = 1;
        for (int i = 0; i < n; i++) {
            after = (short) (actual + before);
            actual = before;
            before = after;
        }
        return after;

    }

    public long lonFib(int n){
        long before = 0,actual = 1,after = 0;
        for (int i = 0; i < n ; i++) {
            after = actual + before;
            actual = before;
            before = after;
        }
        return after;
    }




    public static void main(String [] args){

        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        Fibonacci F = new Fibonacci();
        if (F.intFib(num) >= Integer.MIN_VALUE && F.intFib(num) <=Integer.MAX_VALUE){
            System.out.println("[int]Fibonacci("+num+"): "+F.intFib(num));
        }else{
            System.out.println("Overflow.");
        }

        System.out.println("[short]Fibonacci("+num+"): "+F.shFib(num));
        System.out.println("[byte]Fibonacci("+num+"): "+F.byFib(num));
        System.out.println("[long]Fibonacci("+num+"): "+F.lonFib(num));
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Short.MAX_VALUE);
        System.out.println(Byte.MAX_VALUE);
        System.out.println(Long.MAX_VALUE);

    }
}
