#include <stdio.h>

int main(){
    printf("%s","hello\n");
    printf("\n%10s","hello\n");// print the character upto 10 spaces since hello has 5 other blank will have 5
    printf("%d",printf("%s","Hello world\n "));


    char c = 255;
    c = c + 10;
    printf("%d\n",c);

    signed int i;
    signed j; //compiler will assume interger implictly this and above statement are the same   
    unsigned k;

    long a;
    long int b;
    long long o; // all are the same
    //pritnf(j);

    unsigned h = 1;
    int l = -4;
    printf("\n%d\n",h+l);
    printf("\n%u\n",h+l);


    return 0;
}