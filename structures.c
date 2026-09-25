#include <stdio.h>
#include <string.h>

#define MAX 3

typedef struct{
    int id;
    char name[30];

}Student;

typedef struct{
    Student array[MAX];
    int top;
}StudentStack;

void initStack(StudentStack*s){
    s->top=-1;
}

void push(StudentStack*s,Student newStudent){
    if(s->top==MAX-1){
        printf("Stack Overflow!");
        return;
    }

    s->top++;
    s->array[s->top] = newStudent;
    printf("Pushed: %s\n",newStudent.name);
}

Student pop(StudentStack*s){
    Student emptyStudent = {-1,"Empty"};
    if(s->top==-1){
        printf("Stack underflow!\n");
        return emptyStudent;
    }

    Student poppedStudent = s->array[s->top];
    s->top--;
    return poppedStudent;
}

void displayStack(StudentStack*s){
    if(s->top==-1){
        printf("Stack is empty.\n");
        return;
    }

    printf("\n Current Stack(top to bottom)\n");
    for(int i = s->top;i>=0;i--){
        printf("ID: %d|Name: %s\n",s->array[i].id,s->array[i].name);
    }
}

int main(){
    StudentStack myStack;

    initStack(&myStack);

    Student s1 = {101, "Sidd"};
    Student s2 = {102, "Adi"};
    Student s3 = {103, "Sam"};

    push(&myStack,s1);
    push(&myStack,s2);
    push(&myStack,s3);

    displayStack(&myStack);

    Student popped = pop(&myStack);
    printf("Popped Student ->ID: %d , Name:%s \n");
    displayStack(&myStack);
    return 0;
}