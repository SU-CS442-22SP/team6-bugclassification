package server.test;

class MultiThreadCapableClass {
    private final Object lock = new Object();
    private int sharedResource;

    public void increment() {
        synchronized (lock) {
            sharedResource++;
        }
    }

    public void decrement() {
        sharedResource--;
    }
}

