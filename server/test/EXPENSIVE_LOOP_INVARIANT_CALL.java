package server.test;

class Class {
    private int returnLuckyNumber() {
        return 42;
    }

    public void dosmthNtimes(int n) {
        for (int i = 0; i < n; i++) {
            int constant = returnLuckyNumber();
            System.out.println("Constant: " + constant);
        }
    }
}
