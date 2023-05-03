package server.test;

class Class {
    public void method(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    System.out.println("i: " + i + ", j: " + j + ", k: " + k);
                }
            }
        }
    }

}
