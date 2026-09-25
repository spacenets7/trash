#include <stdio.h>

int main(){
    printf("pointer arithmetic");

    int a = 34;
    int *ptra = &a;
    printf("%d \n",ptra);     //can use x in place of d
    printf("%d \n",ptra+1);
    // printf("%d \n",ptra++);
    printf("%d \n",*ptra);
    printf("%d \n",*ptra+1);


    return 0;
}