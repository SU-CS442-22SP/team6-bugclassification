package server.test;

import java.util.ArrayList;
import java.util.List;

class MyClass {
    private final List<String> priv_list = new ArrayList<>();

    public void modify() {
        priv_list.add("Modified");
    }
}

