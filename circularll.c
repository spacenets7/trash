#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node * next;
};

void linkedListTraversal(struct Node *head){
    struct Node *ptr = head;
    printf("Elements is %d\n",ptr->data);
    ptr = ptr->next;

    while(ptr!=head){
        printf("Elements is %d\n",ptr->data);
         ptr = ptr->next;
    }
}

struct Node * insertAtFirst(struct Node *head, int data){
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr ->data = data;

    struct Node * p =head->next;
    while(p->next!=head){
        p=p->next;
    }
    // at this point p points to the last node of this circular linked list

    p->next=ptr;
    ptr->next = head;
    head = ptr;
    return head;
}


int main(){
    struct Node *head;
    struct Node *second;
    struct Node *third;
    struct Node *fourth;

    head = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));
    fourth = (struct Node *)malloc(sizeof(struct Node));

    //link first and second nodes
    head ->data=7;
    head->next=second;

    //link second and third nodes
    second->data=11;
    second->next = third;

    // the list at the third node
    third->data=10;
    third->next = fourth;

    //link the fourth to first node
    fourth -> data = 9;
    fourth->next=head;

    linkedListTraversal(head);
    head = insertAtFirst(head, 60);
    printf("After traversal: \n");
    linkedListTraversal(head);

    return 0;
}