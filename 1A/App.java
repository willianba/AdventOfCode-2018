import java.util.Scanner;

public class App {
    private static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
        int result = 0;

        while(in.hasNext()){
            result += in.nextInt();
        }

        System.out.println(result);
    }
}
