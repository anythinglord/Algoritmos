import java.util.LinkedList;

public class Matrices {
    public int[][] one(int n){
        int [][] M = new int[n][n];
        for (int i = 0; i < n ; i++) {
            for (int j = 0; j < n; j++) {
                M[i][j] = 1;
            }
        }
        return M;
    }
    public int[][] zero(int m){
        int [][] M = new int[m][m];
        for (int i = 0; i < m ; i++) {
            for (int j = 0; j < m ; j++) {
                M[i][j] = 0;
            }
        }
        return M;
    }
    public double Sum(LinkedList<Double> l){
        int n = l.size();
        double suma = 0;
        for (int i = 0; i < n ; i++) {
            suma = suma + l.get(i);
        }
        return suma/10;
    }
    public double Dot(int[][] A ,int [][] B){
        double timeS = 0.0,timeO =0.0,timeF = 0.0;
        timeS = System.currentTimeMillis();
        int n = A.length;
        int a = 0;
        for (int i = 0; i < n ; i++) {
            for (int j = 0; j < n ; j++) {
                a = a +(A[i][j]*B[j][i]);
            }
        }
        timeF = System.currentTimeMillis();
        return timeF-timeS;
    }
    public static void main(String [] args) {
        double tiempo = 0.0;
        LinkedList<Double> lista = new LinkedList<Double>();
        Matrices m = new Matrices();
        for (int i = 1; i <= 500; i++) {
            int [][] A;
            int [][] B;
            A = m.one(i);
            B = m.zero(i);
            for (int j = 0; j < 10 ; j++) {
                tiempo = m.Dot(A,B);
                lista.add(tiempo);
            }
            System.out.println("Tiempo Promedio para Matriz["+i+"]["+i+"]: "+m.Sum(lista)+" MiliSeconds");
        }
    }

}
