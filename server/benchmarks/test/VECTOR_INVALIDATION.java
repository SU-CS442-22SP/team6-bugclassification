package server.test;

import java.util.ArrayList;
import java.util.List;

class MyClass {
    public void dosmth() {
        List<String> list = new ArrayList<>();
        list.add("Hello");
        list.add("World");
        list.remove(0);
        String value = list.get(0); // IndexOutOfBoundsException
    }
}
