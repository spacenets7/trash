#include <stdio.h>

int main(){
    int arr[] = {1,2,3,4,5,6,7,11};
    printf("%d \n",&arr[0]);  //prints only the address of arr[i]
    printf("%d \n",&arr[1]);
    printf("%d \n",&arr[2]);

    printf("%d \n",arr); //prints the first element i.e is present in 0th index
    printf("%d \n",arr+1);  //prints the 2nd element
    
    printf("%d \n",*(&arr[0])); // prints the value that is there in the ith position
    printf("%d \n",*(&arr[1]));

    printf("%d \n",*(arr)); // same as above
    printf("%d \n",*(arr+1));

    int* arrayptr = arr;
    arrayptr++;
    


    return 0 ;

}