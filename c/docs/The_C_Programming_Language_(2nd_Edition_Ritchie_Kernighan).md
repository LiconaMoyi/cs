# The C Programming Language

## Chapter 1 Basic Content

### 一 、vaiables,constants,input,output,functions

#### 1.hello world

```c
#include <stdio.h>
main() {
    printf("hello, wolrd\n");
}
```

### 二、operators,conditional expressions

### 三、control flow(if-else,switch,goto)

### 四、pointers

## Chapter 2 make

## Chapter 3 c open-source project

#### 1.basic demo

```c
#include <stdio.h>

#define LOWER 0        /* lower limit of table */
#define UPPER 300    /* upper limit */
#define STEP 20        /* step size */

/* print Fahreheit-Celsius table */
main()
{
    int fahr;
    for(fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
        printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
}
```

```c
#include <stdio.h>

/* copy input to output */
main()
{
    int c;
    c = getchar();
    while(c != EOF) {
        putchar(c);
        c = getchar();
    }
}
```

#### 2.CMake

​    CMake is an open-source, cross-platform family of tools designed to build, test and package software.

##### 2.1.use third party library

```shell
mkdir build
cd build
cmake ..
cmake --build
cmake --install
```

add follow code in CMakeLists.txt

```shell
find_package(Libevent REQUIRED core)
target_link_libraries(你的可执行目标 libevent::core)
```

[CMake官方教程地址](https://cmake.org/cmake/help/latest/guide/tutorial/A%20Basic%20Starting%20Point.html)
