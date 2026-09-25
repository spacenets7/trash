#include <stdio.h>
#include <string.h> 


struct Student{
    int id;
    int marks;
    char fav_char;
    char name[34];

};

int main(){
    struct Student siddu, sidd, sus;
    sidd.id= 90;
    siddu.id = 100;
    sus.id = 10;

    siddu.marks = 100;
    sidd.marks = 90;
    sus.marks = 80;

    sidd.fav_char = 'a';
    siddu.fav_char = 'b';
    sus.fav_char = 'c';
    strcpy(siddu.name,"Siddu");

    printf("%s got %d marks: ",siddu.name,siddu.marks); 

    return 0;

}