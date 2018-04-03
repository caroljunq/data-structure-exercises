#include <stdio.h>
#include <stdlib.h>

//Min Binary Heap with Percolate Up and Down operations
//Class number 5 --> April  2, 2018
//Array Implementation

typedef struct{
  int key;
  void *value;
} elem;

typedef struct{
  elem *elems;
  int n;
  int max;
} bin_heap;

//heap init --> index = 1
void create_heap(bin_heap *h, int capacity){
  h->elems = (elem *) malloc((capacity + 1) * sizeof(elem));
  h->max = capacity;
  (h->elems[0]).key = 0;
  (h->elems[0]).value = NULL;
  h->n = 0;
}

//Percolate up
void perc_up(bin_heap *h, int i, elem *e){
  if(i == 1){
    h->elems[1] = *e;
  }
  else if(h->elems[i/2].key < e->key){
    h->elems[i]= *e;
  }
  else{
    h->elems[i] = h->elems[i/2];
    perc_up(h, i/2, e);
  }
}

//Insertion operation
void insert(bin_heap *h, elem *e){
  if(h->n == 0){
    h->elems[1] = *e;
  }
  else{
    perc_up(h, h->n+1, e);// i = n+1, n+1 = last position is empty
  }
  h->n++;
}

//Percolate Down
void perc_down(bin_heap *h, int i, elem *e){
  int j;
  int n = h->n;
  if((2*i) > n ){
    h->elems[i] = *e;
  }

  else if((2*i) == n){
    if((h->elems[2*i]).key < e->key){
      h->elems[i] = h->elems[2*i];
      h->elems[2*i] = *e;
    }
    else{
      h->elems[i] = *e;
    }
  }

  else{
    if((h->elems[2*i]).key < (h->elems[(2*i) + 1]).key){
      j = 2 * i;
    }
    else{
      j =  (2 * i) + 1;
    }

    if((h->elems[j]).key < e->key){
      h->elems[i] = h->elems[j];
      perc_down(h, j, e);
    }
    else{
      h->elems[i] = *e;
    }
  }
}

//delete min --> heap min root
void delete_min(bin_heap *h){
  if(h->n == 1){
    (h->elems[1]).key = 0;
    (h->elems[1]).value = "vazio";
  }
  else{
    perc_down(h, 1, &(h->elems[h->n]));//i = n, last filled position
  }
  h->n--;
}

int main(){
  bin_heap heap;
  create_heap(&heap, 6); // example with max 6 elements on min binary heap

  //tests
  elem test[] = {{8,"hello"},{5,"hello"},{10,"hello"},{12,"hello"},{4,"hello"},{1,"hello"}};
  insert(&heap,&test[0]);
  insert(&heap,&test[1]);
  insert(&heap,&test[2]);
  insert(&heap,&test[3]);
  insert(&heap,&test[4]);
  insert(&heap,&test[5]);

  delete_min(&heap);
  delete_min(&heap);

  for(int i = 1; i <= heap.n; i++){
    printf("%d ", heap.elems[i].key);
  }

  return 0;
}
