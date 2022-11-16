// Programa que implementa os métodos de ordenação e os de buscas
// Estrutura de Dados II
#include <stdio.h>
#include <stdlib.h>

int quantidadeDeValores();
void entradaValores(int *v, int tV);
void apresentaVetor(int *v, int tV);
int menuEscolhaOrdenacao();
void ordenacoes(int opcaoEscolhida, int *v, int tV);
int menuEscolhaBusca();
void bubbleSort(int *v, int tV);
void shellSort(int *v, int tV);
void insertionSort(int *v, int tV);
void selectionSort(int *v, int tV);
void mergeSort(int *v, int posicaoInicio, int posicaoFim);
void quickSort(int *v, int esquerda, int direita);
void trocaBS(int *v, int pA);
void trocaSS(int c, int *v, int tV);
void trocaIS(int i, int c, int *v);  
void trocaSelSort(int *v, int minimo, int i);
void trocaMS(int *v, int *vetorTemp, int i, int j, int metadeTamanho, int posicaoFim);
int trocaQS(int *v, int x, int pivo);
int verificaMinimo(int min, int *v, int i, int tV);
void buscas(int opcaoBusca, int *v, int tV);
void buscaSequencial(int *v, int tV);  
void buscaBinaria(int pMin, int pMax, int *v);     

int main(){
    int tamanho = quantidadeDeValores(); // chamando função de quantidade a serem colocadas no vetor
    int vetor[tamanho];

    entradaValores(vetor, tamanho); // chamando função que preenche o vetor

    int opcaoEscolhida = menuEscolhaOrdenacao(); // chamando função de escolha do método de ordenação

    if(opcaoEscolhida != 0){
        ordenacoes(opcaoEscolhida, vetor, tamanho); // chamando função de controle das ordenações
        int opcaoBusca = menuEscolhaBusca(); // chamando função de escolha do tipo busca

        if(opcaoBusca != 0){
            buscas(opcaoBusca, vetor, tamanho); // chamando função de controle de busca
        }
    }

    return 0;
}

// função responsável por determinar o tamanho do vetor
int quantidadeDeValores(){
    int q = 0;

    printf("Digite quantos valores voce deseja armazenar: ");
    scanf("%d", &q);

    while(q <= 0){ // caso o valor digitado pelo usuário seja 0 ou negativo
        system("cls");
        printf("Opcao invalida! Digite valores positivos acima de 0\n");
        printf("Digite quantos valores voce deseja: ");
        scanf("%d", &q);
    }

    system("cls");    
    
    return q;
}

// função que pega os valores do teclado e preenche o vetor criado
void entradaValores(int *v, int tV){ // v =  vetor; tV = tamanho do vetor

    printf("Digite os %d valores do vetor:\n", tV);
    for(int i = 0; i < tV; i++){
        printf("valor %d: ", i + 1);
        scanf("%d", &v[i]);
    }
    system("cls");

    apresentaVetor(v,tV); // chamando função que imprime o vetor na tela
}

// funçaõ que imprime o vetor na tela
void apresentaVetor(int *v, int tV){
    int quebraLinha = 0;

    for(int i = 0; i < tV; i++){
        if(quebraLinha == 10){
            quebraLinha = 0;
            printf("\n");
            printf("%d ", v[i]);
            quebraLinha++;
        }
        else{
            printf("%d ", v[i]);
            quebraLinha++;
        }
    }
    printf("\n");
    system("pause");
    system("cls");
}

// função que escolhe o método de ordenação
int menuEscolhaOrdenacao(){
    int escolha = 9;

    while(escolha < 0 || escolha > 6){
        printf("ESCOLHA O METODO DE ORDENACAO DESEJADO!\n");
        printf("1 - Bubble Sort\n");
        printf("2 - Shell Sort\n");
        printf("3 - Insertion Sort\n");
        printf("4 - Selection Sort\n");
        printf("5 - Merge Sort\n");
        printf("6 - Quick Sort\n");
        printf("0 - Encerrar\n");
        scanf("%d", &escolha);

        if(escolha < 0 || escolha > 6){
            system("cls");
            printf("Opcao invalida! Tente novamente!\n");
        }
    }
    system("cls");

    return escolha;   
    //menuEscolhaBusca(escolha); // chamando método de escolha da busca entre binária e sequencial
}

// função que escolha o método de busca
int menuEscolhaBusca(){
    int escolha = 3;

    printf("ESCOLHA UMA OPCAO DE BUSCA!\n");
    while(escolha < 0 || escolha > 2){
        printf("1 - Busca Sequencial\n");
        printf("2 - Busca Binaria\n");
        printf("0 - Encerrar\n");
        scanf("%d", &escolha);

        if(escolha < 0 || escolha > 2){
            system("cls");
            printf("Opcao invalida! Tente novamente!\n");
        }
    }
    system("cls");
    return escolha;
}

// função que controla as ordenações
void ordenacoes(int opcaoEscolhida, int *v, int tV){
    switch (opcaoEscolhida)
    {
        case 1:{
            bubbleSort(v, tV); // chamando método de ordenação Bubble Sort
            apresentaVetor(v, tV);
            break;
        }
        case 2:{
            shellSort(v, tV); // chamando método de ordenação Shell Sort
            apresentaVetor(v, tV);
            break;
        }

        case 3:{
            insertionSort(v, tV); // chamando método de ordenação Insertion Sort
            apresentaVetor(v, tV);
            break;
        }

        case 4:{
            selectionSort(v, tV); // chamando método de ordenação Selection Sort
            apresentaVetor(v, tV);
            break;
        }

        case 5:{
            mergeSort(v, 0, tV - 1); // chamando método de ordenação Merge Sort
            apresentaVetor(v, tV);
            break;
        }

        case 6:{
            quickSort(v, 0, tV - 1); // chamando método de ordenação Quick Sort
            apresentaVetor(v, tV);
            break;
        }
            
        default:{
            break;
        }
    }
}

// Metodo de ordenacao bubble sort
void bubbleSort(int *v, int tV){
    int pVT, pA; 
    // pVT - controla o vetor total; pA - controla o percurso até final atual

    for(pVT = 1; pVT < tV; pVT++){
        for(pA = 0; pA < tV - 1; pA++){
            if(v[pA] > v[pA + 1]){
                trocaBS(v, pA);  // chamando troca por Bubble Sort              
            }
        }
    }
}

// trocando valores do Bubble Sort
void trocaBS(int *v, int pA){
    int aux;
    aux = v[pA];
    v[pA] = v[pA + 1];
    v[pA + 1] = aux;
}

// Metodo de ordenação shell Sort
void shellSort(int *v, int tV){
    int cont = 1;

    while(cont < tV) {
        cont = 3 * cont + 1;
    }

    trocaSS(cont, v, tV); // chamando troca por Shell Sort
}

// trocando valores do Shell Sort caso necessário
void trocaSS(int c, int *v, int tV){
    int i , j , valorComp;

    while (c > 1) {
        c /= 3;

        for(i = c; i < tV; i++) {
            valorComp = v[i];
            j = i - c;

            while (j >= 0 && valorComp < v[j]) {
                v[j + c] = v[j];
                j -= c;
            }

            v[j + c] = valorComp;
        }
    }
}

// Metodo de ordenção Insertion Sort
void insertionSort(int *v, int tV){
    int i = 1;

    for(i; i < tV; i++){
        int c = i;

        trocaIS(i, c, v); // chamando função de troca por Insertion Sort 
    }
}

// trocando valores do Insertion Sort
void trocaIS(int i, int c, int *v){
    while(v[c] < v[c-1]){
        int aux = v[c-1];
        v[c-1] = v[c];
        v[c] = aux;
        c--;

        if(c == 0){
            break;
        }
    }
}

// Metodo de ordenação Selection Sort
void selectionSort(int *v, int tV){
    int minimo;

    for(int i = 0; i < tV; i++){
        minimo = i;

        minimo = verificaMinimo(minimo, v, i, tV); // chamando função que verifica o menor valor 
        trocaSelSort(v, minimo, i); // chamando função de troca por Selection Sort
    }
}

// Verificando valor minimo do Selection Sort
int verificaMinimo(int min, int *v, int i, int vT){

    for(int j = i + 1; j < vT; j++){
        if(v[min] > v[j]){
            min = j;
        }
    }
    
    return min;
}

// Trocando valores do Selection Sort
void trocaSelSort(int *v, int minimo, int i){
    int auxiliar = v[i];
    v[i] = v[minimo];
    v[minimo] = auxiliar;
}

// Metodo de ordenação Merge Sort
void mergeSort(int *v, int posicaoInicio, int posicaoFim) {
    int i, j, metadeTamanho, *vetorTemp;

    if(posicaoInicio == posicaoFim){ 
        return;
    }
    metadeTamanho = (posicaoInicio + posicaoFim ) / 2;

    mergeSort(v, posicaoInicio, metadeTamanho); // chamando merge sort
    mergeSort(v, metadeTamanho + 1, posicaoFim);

    i = posicaoInicio;
    j = metadeTamanho + 1;

    int tamTemp = posicaoFim - posicaoInicio + 1;
    vetorTemp = (int *) malloc(sizeof(int) * (tamTemp)); // criando vetor temporário

    trocaMS(v, vetorTemp, i, j, metadeTamanho, posicaoFim);

    for(i = posicaoInicio; i <= posicaoFim; i++) {
        v[i] = vetorTemp[i - posicaoInicio];
    }
    free(vetorTemp); // desalocando vetor temporário
}

// trocando valores usando Merge Sort
void trocaMS(int *v, int *vetorTemp, int i, int j, int metadeTamanho, int posicaoFim){
    int k = 0;
    while(i < metadeTamanho + 1 || j  < posicaoFim + 1) {
        if (i == metadeTamanho + 1 ) { 
            vetorTemp[k] = v[j];
            j++;
            k++;
        }
        else {
            if (j == posicaoFim + 1) {
                vetorTemp[k] = v[i];
                i++;
                k++;
            }
            else {
                if (v[i] < v[j]) { //*
                    vetorTemp[k] = v[i];
                    i++;
                    k++;
                }
                else {
                    vetorTemp[k] = v[j];
                    j++;
                    k++;
                }
            }
        }
    }
}

// Metodo de ordenação do Quick Sort
void quickSort(int *v, int esquerda, int direita){
    int pivo = esquerda;

    for(int x = esquerda + 1; x <= direita; x++){
        pivo = trocaQS(v, x, pivo); // chamando função de troca de valores do Quick Sort
    }

    if(pivo - 1 >= esquerda){              
        quickSort(v, esquerda, pivo - 1); // chamando função de ordenação quick Sort 
    }
    if(pivo + 1 <= direita){              
        quickSort(v, pivo + 1 ,direita);  // chamando função de ordenação quick Sort
    }
}

// trocando valores do Quick Sort
int trocaQS(int *v, int x, int pivo){
    int y = x;

    if(v[y] < v[pivo]){
        int aux = v[y];

        while(y > pivo){
            v[y] = v[y - 1];
            y--;
        }

        v[y] = aux;
        pivo++;

        return pivo;
    }
    return pivo;
}

// função que controla as buscas
void buscas(int opcaoBusca, int *v, int tV){
    switch (opcaoBusca)
    {
        case 1:{
            buscaSequencial(v, tV); // chamando função de Busca Sequêncial
            break;
        }

        case 2:{
            buscaBinaria(0, tV - 1, v); // chamando função de Busca Binária
            break;
        }
        
        default:{
            break;
        }
    }
}

// função de busca sequêncial
void buscaSequencial(int *v, int tV){
    int search, achou = 0;
    printf("Digite o numero buscado: ");
    scanf("%d", &search);

    system("cls");

    for(int i = 0; i < tV; i++){
        if(search == v[i]){
            achou = 1;
        }
    }

    if(achou == 1){
        printf("%d foi encontrado!\n", search);
    }
    else{
        printf("%d nao foi encontrado!\n", search);
    }
}

// função de busca binária
void buscaBinaria(int pMin, int pMax, int *v){
    int search, achou = 0;

    printf("Digite o numero buscado: ");
    scanf("%d", &search);

    system("cls");

    while(pMin <= pMax){
        int meio = (pMin + pMax) / 2;

        if(search == v[meio]){
            printf("%d foi encontrado!\n", search);
            system("pause");
            break;
        }
        else if(search < v[meio]){
            pMax = meio - 1;
        }
        else{
            pMin = meio + 1;
        }        
    }

    if(pMin > pMax){
        printf("%d nao foi encontrado!\n", search);
        system("cls");
    }
}
