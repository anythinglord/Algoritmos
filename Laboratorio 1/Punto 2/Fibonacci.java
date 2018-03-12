

public class Fibonacci {


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

        int a = 0;
        int t = 0;
        int c = 0;
        int d = 0;
        int l = 0;

        long b = 0;
        Fibonacci F = new Fibonacci();
        for (int i = 0; i < 150; i++) {
            b = F.lonFib(i);

            if (b > Byte.MAX_VALUE & a == 0){
                System.out.println("OverFlow in byte: "+i);
                a = 1;
            }
            if (b > Short.MAX_VALUE & t == 0){
                System.out.println("OverFlow in Short: "+i);
                t = 1;
            }
            if (b > Integer.MAX_VALUE & c == 0){
                System.out.println("OverFlow in int: "+i);
                c = 1;
            }
            if (b < 0 & l == 0){
                System.out.println("OverFlow in long: "+i);
                l = 1;
            }

        }
    }
}
