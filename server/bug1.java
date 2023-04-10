int incr(int x) {
  return x + 1;
}

void foo_linear(int size) {
  int x = 10;
  for (int i = 0; i < size; i++) {
    incr(x);
  }
}

void symbolic_expensive_hoist(int size) {
  for (int i = 0; i < size; i++) {
    foo_linear(size);
  }
}