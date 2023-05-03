package server.test;
import java.util.*;

class AClass {
    public void example() {
        List<String> immutableList = Collections.unmodifiableList(new ArrayList<>());
        List<String> mutableList = (List<String>) immutableList;
    }
}

