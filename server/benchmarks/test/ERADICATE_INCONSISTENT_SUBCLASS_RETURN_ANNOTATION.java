package server.test;

class Parent {
    public @Nullable String method() {
        return null;
    }
}

class Child extends Parent {
    @Override
    public @NonNull String method() {
        return "I am the child";
    }
}

