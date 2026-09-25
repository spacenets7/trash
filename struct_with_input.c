#include <stdio.h>
#define MAX 3

typedef struct{
    int id;
    char name[30];
}Student;

typedef struct{
    Student array[MAX];
    int top;
}Stack;

void init(Stack *s){
    s->top=-1;
}

void push(Stack *s, Student x){
    if(s->top==MAX-1){
        printf("Stack Overflow\n");
        return;
    }
    s->top++;
    s->array[s->top]=x;
}

Student pop(Stack *s){
    Student x = {-1, "Empty"};
    if(s->top ==-1){
        printf("Stack underflow\n");
        return x;

    }
    x = s-> array[s->top];
    s->top--;
    return x;

}

void display(Stack *s){
    if(s->top==-1){
        printf("Stack empty\n");
        return;
    }

    for(int i = s->top;i>=0;i--){
        printf("%d %s \n",s->array[i].id,s->array[i].name);
    }
}

int main(){
    Stack s;
    Student student;

    init(&s);

    for(int i=0;i <MAX;i++){
        printf("Enter ID: ");
        scanf("%d", &student.id);

        printf("Enter Name: ");
        scanf("%s",student.name);

        push(&s, student);
    }

    display(&s);

    Student removed = pop(&s);

    printf("\nPopped: %d %s\n",removed.id,removed.name);

    display(&s);

    return 0;

}