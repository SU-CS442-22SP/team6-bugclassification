package server.test;

class MyClass {
    public static final int VALUE = Helper.getValue();
    public static final Helper HELPER = new Helper();

    static class Helper {
        public int getValue() {
            return 42;
        }
    }
}
