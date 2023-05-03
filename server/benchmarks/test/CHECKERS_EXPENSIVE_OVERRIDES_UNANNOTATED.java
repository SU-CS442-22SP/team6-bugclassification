package server.test;

class Computation {
    public long compute(long n) {
        if (n <= 1) {
            return 1;
        } else {
            return n * compute(n - 1);
        }
    }
}

class SubComputation extends Computation {
    @Override
    public long compute(long n) {
        long result = 1;
        for (long i = 1; i <= n; i++) {
            result *= i;
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Computation computation = new SubComputation();
        System.out.println("Result: " + computation.compute(5)); // Unaware of the expensive nature of the overridden method
    }
}

