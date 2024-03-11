#include <stdio.h>
#include <stdint.h>

void test1() { printf("hello1!\n"); }
void test2() { printf("hello2!\n"); }
void test3() { printf("hello3!\n"); }

uintptr_t test(int a) {
    switch (a) {
    case 1:
        return (uintptr_t)test1;
    case 2:
        return (uintptr_t)test2;
    default:
        return (uintptr_t)test3;
    }
}

int main() {
    int a = 0;
    scanf("%d", &a);

    void (*selectedFunction)() = (void (*)())test(a);
    selectedFunction();  // 调用选择的函数

    return 0;
}
