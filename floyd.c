#include <stdio.h>
#include <stdlib.h>

#define INF 1000;

int adj[1000][1000];


void printa_matriz(int n){
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      printf("%d ", adj[i][j]);
    }
    printf("\n");
  }
}

void init_matriz(int n){//aqui era pra colocar a matriz
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      if(i == j){
        adj[i][j] = 0;
      }
      else{
        adj[i][j] = INF;
      }
    }
  }
}

int min(int x, int y){
    if(x <= y)
      return x;

    return y;
}


void encontra_min(int n){
  int soma = 0, anterior;

  for(int k = 0; k < n; k++){
    for(int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        anterior = adj[i][j];
        if(adj[i][k] == 1000 || adj[k][j] == 1000){
          soma =  INF;
        }else{
          soma = adj[i][k] + adj[k][j];
        }
        adj[i][j] = min(anterior, soma);
      }
    }
  }
}

int main(){
  int V,E,v1,v2,peso;
  printf("Digite vertice e arestas\n");
  scanf("%d %d",&V,&E);
  init_matriz(V);

  for(int i = 0; i < E; i++){
    scanf("%d %d %d",&v1,&v2,&peso);
    adj[v1][v2] = peso;
  }
  encontra_min(V);
  printa_matriz(V);
  return 0;
}
