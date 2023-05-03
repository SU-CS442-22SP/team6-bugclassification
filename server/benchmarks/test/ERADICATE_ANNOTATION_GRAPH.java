package server.test;

import javax.annotation.Nullable;
import javax.annotation.Nonnull;

class Example {
    @Nonnull
    private String processString(@Nonnull String input) {
        return input.toUpperCase();
    }

    public void dosmth(@Nullable String value) {
        if (value != null) {
            String result = processString(value);
        }
    }

    public void dosmthalternative(@Nullable String value) {
        String result = processString(value);
    }
}
