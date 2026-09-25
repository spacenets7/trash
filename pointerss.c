#include <stdio.h>

int main(){
    printf("Pointers\n");

    int a=76;
    int* ptra =&a;
    printf("the value of a is: %d\n",a);
    printf("the value of a is: %d\n",*ptra);  // prints the value of a
    printf("the value of a is: %x\n",ptra);   //address of the variable a
    printf("the value of a is: %x\n",&a);     // same as ptra i.e the address of a
    printf("the value of a is: %x\n",*ptra);  //derefrence the pointer as hexadecimal i.e prints the hexadecimal value of a
    printf("the value of a is: %x\n",&ptra);  //address of the pointer ptra 

    int *ptr = NULL;
    printf("something is here: %p\n ",ptr);

    return 0;
}