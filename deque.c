#include <stdio.h>
#include <stdlib.h>

//Double-ended queue
//Class number 3 --> March 19, 2018
//Array Implementation

typedef struct Deque{
  int front;
  int rear;
  int *arr;
  int count;
} deque;

void initDeque(deque *dq, int size){
  dq->front = -1;
  dq->rear = size;
  dq->arr = malloc(size * sizeof(int));
  dq->count = 0;
}

int isEmpty(deque *dq){
  if(dq->count == 0)
    return 1;
  return 0;
}

int last(deque *dq){
  return dq->arr[dq->rear];
}

int first(deque *dq){
  return dq->arr[dq->front];
}

void removeLast(deque *dq, int size){
  if(dq->rear < size){
    dq->rear++;
    dq->count--;
  }
}

void removeFirst(deque *dq){
  if(dq->front >= 0){
    dq->front--;
    dq->count--;
  }
}

void insertFirst(deque *dq, int el){
  if((dq->front + 1) < dq->rear){
    dq->front++;
    dq->arr[dq->front] = el;
    dq->count++;
  }
}

void insertLast(deque *dq, int el){
  if((dq->rear - 1) > dq->front){
    dq->rear--;
    dq->arr[dq->rear] = el;
    dq->count++;
  }
}

int main(){
  deque *dq = (deque *) malloc(sizeof(deque));
  initDeque(dq, 5);

  insertFirst(dq, 1);
  insertFirst(dq, 2);
  insertLast(dq, 77);
  insertLast(dq, 88);
  insertFirst(dq, 666);
  removeLast(dq,5);
  insertFirst(dq, 999);

  for(int i = 0; i < 5; i++){
    printf("%d ",dq->arr[i]);
  }

  return 0;
}
