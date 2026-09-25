#include <stdio.h> //preprocessor directive to include the standard input-output header file

int add3(int a,int b, int c){
    int result = a + b + c;
    return result;
}

struct student{
    char name[20];
    int age;
    float gpa;
    
};

int main(){
    printf("Hello, World!\n");
    int s = add3(11,12,15);
    printf("%i",s);

    //char 1byte 255
    //short 2bytes 65535
    //int 4bytes 4294967295
    //long 8bytes 4294967295
    //long long 8bytes 2^64 -1

    return 0;
}