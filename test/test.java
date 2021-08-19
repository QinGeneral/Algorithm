package test;

public class test {
    public static String getString(int a) {
        if (a < 10) {
            return a + "";
        } else {
            return (char) (Character.getNumericValue('A') + (a - 10)) + "";
        }
    }

    public static void main(String[] args) {
        System.out.println(getString(9));
    }
}
