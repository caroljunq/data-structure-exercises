#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

//Binary Search
//Class number 4, March 26, 2018
//Recursive Implementation

//Check elem in an array
bool check_elem(int *v, int min_index, int max_index, int val){

  int middle = ((min_index + max_index)/2);

  if(max_index < min_index)
    return false;
  if(val == v[middle])
    return true;
  if(val < v[middle])
    check_elem(v, min_index, middle - 1, val);
  else
    check_elem(v, middle + 1 , max_index, val);
}

int main(){
  int arr[] = {11,21,33,66,77,88};
  printf("%d\n", check_elem(arr,0,(int)(sizeof(arr)/sizeof(arr[0]))-1,11));
  return 0;
}
