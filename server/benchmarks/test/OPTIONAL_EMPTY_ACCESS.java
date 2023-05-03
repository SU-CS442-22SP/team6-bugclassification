package server.test;
import java.util.Optional;

class MyClass {
    private Optional<String> str = Optional.empty();

    public String getString() {
        return str.get();
    }

}
