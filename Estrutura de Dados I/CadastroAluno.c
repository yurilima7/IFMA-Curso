// Programa que realiza o cadastro de alunos
// Utilizando, Lista, Pilha, Fila e Árvore
// Estrutura de Dados I
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Item{
    char nome[50];
    int serie;
    char CPF[12];
    int idade;
    char genero[50];
    int matricula;
    struct Item *proximo;
}Item;

typedef struct lista{
    char nome[50];
    int serie;
    char CPF[12];
    int idade;
    char genero[50];
    int matricula;
    struct lista *proximo;
}alunoLista;

typedef struct Dados{
    char nome[50];
    int serie;
    char CPF[12];
    int idade;
    char genero[50];
    int matricula;
}Dados;

typedef struct alunoPilha{
    Item *topo;
    int tamanho;
}alunoPilha;

typedef struct alunoFila{
    Item *inicio;
    Item *fim;
    int tamanho;
}alunoFila;

typedef struct Aluno{
    Dados dados;
    struct Aluno *esquerda;
    struct Aluno *direita;
}Aluno;

int menuEscolha();

int menuLista();
alunoLista *inicializaLista();
int vaziaLista (alunoLista *aluno);
alunoLista *cadastraAlunoLista(alunoLista *aluno, int matricula);
alunoLista *descadastraAlunoLista(alunoLista *aluno, int matricula);
void buscaDadosAlunoLista(alunoLista *aluno, int matricula);
void exibirCadastradosLista(alunoLista *aluno);
void liberaLista(alunoLista *aluno);

alunoPilha *inicializaPilha();
int vaziaPilha(alunoPilha *aluno);
int menuPilha();
Item *inicializaDadosPilha(int matricula);
void cadastraAlunoPilha(alunoPilha *aluno, Item *item);
Item *retiraUltimoCadastradoPilha(alunoPilha *aluno);
void exibeAlunosPilha(alunoPilha *aluno);
void eliminaCadastroPilha(alunoPilha *aluno);

alunoFila *inicializaFila();
int vaziaFila(alunoFila *aluno);
int menuFila();
Item *inicializaDadosFila(int matricula);
void cadastraAlunoFila(alunoFila *aluno, Item *item);
int tamanhoFila(alunoFila *aluno);
Item *retiraPrimeiroCadastradoFila(alunoFila *aluno);
void exibeCadastradosFila(alunoFila *aluno);
void eliminaCadastradosFila(alunoFila *aluno);

Aluno *inicializa();
int menu();
Dados *inicializaDados(int matricula);
int verifica(Aluno* aluno, int nC);
Aluno *cadastraDados(Aluno *aluno, Dados *item);
int busca();
Aluno *buscando(Aluno *aluno, int matriculaBuscada);
void apresentaDados(Aluno *aluno);
void exibindoCadastrados(Aluno *aluno);
Aluno *maiorEsquerda(Aluno *aluno);
Aluno *removeAluno(Aluno *aluno, int quemSai);
Aluno *derrubaArvore(Aluno *aluno);

int main(){
    int esc = 1;
    while(esc != 0){
        esc = menuEscolha();

        switch(esc){
            case 1:{
                int opcao = 1, nC = 0;
                alunoLista *novoAluno = inicializaLista();

                while(opcao != 0){
                    opcao = menuLista();

                    switch(opcao){
                        case 1:{
                            nC++;
                            novoAluno = cadastraAlunoLista(novoAluno, nC);
                            break;
                        }

                        case 2:{
                            int des;
                            printf("Digite o numero da matricula para descadastrar: ");
                            scanf("%d", &des);
                            novoAluno = descadastraAlunoLista(novoAluno, des);
                            break;
                        }

                        case 3:{
                            int bus;
                            printf("Digite o numero da matricula buscada: ");
                            scanf("%d", &bus);
                            buscaDadosAlunoLista(novoAluno, bus);
                            break;
                        }

                        case 4:{
                            exibirCadastradosLista(novoAluno);
                            break;
                        }

                        case 0:{
                            liberaLista(novoAluno);
                            break;
                        }

                        default:{
                            printf("Opcao invalida!!\n");
                            system("pause");
                            system("cls");
                            break;
                        }
                    }

                }
                break;
            }

            case 2:{
                alunoPilha *aluno = inicializaPilha();
                Item *cadAluno;
                int opcao = 1, nC = 0; 
                
                while(opcao != 0){
                    opcao = menuPilha();

                    switch(opcao){
                        case 1:{
                            nC++;
                            cadAluno = inicializaDadosPilha(nC);
                            cadastraAlunoPilha(aluno, cadAluno);
                            break;
                        }

                        case 2:{
                            cadAluno = retiraUltimoCadastradoPilha(aluno);
                            break;
                        }

                        case 3:{
                            exibeAlunosPilha(aluno);
                            break;
                        }

                        case 0:{
                            eliminaCadastroPilha(aluno);
                            break;
                        }

                        default:{
                            printf("Opcao invalida!!\n");
                            system("pause");
                            system("cls");
                            break;
                        }
                    }
                }
                break;
            }

            case 3:{
                alunoFila *aluno = inicializaFila();
                Item *cadAluno;
                int opcao = 1, nC = 0;

                while(opcao != 0){
                    opcao = menuFila();

                    switch(opcao){
                        case 1:{
                            nC++;
                            cadAluno = inicializaDadosFila(nC);
                            cadastraAlunoFila(aluno, cadAluno);
                            break;
                        }

                        case 2:{
                            cadAluno = retiraPrimeiroCadastradoFila(aluno);
                            break;
                        }

                        case 3:{
                            exibeCadastradosFila(aluno);
                            break;
                        }

                        case 0:{
                            eliminaCadastradosFila(aluno);
                            break;
                        }

                        default:{
                            printf("Opcao invalida!!\n");
                            system("pause");
                            system("cls");
                            break;
                        }
                    }
                }
                break;
            }

            case 4:{
                Aluno *aluno = inicializa();
                Dados *cadAluno;
                int opcao = 1;
                while(opcao != 0){
                    opcao = menu();

                    switch(opcao){
                        case 1:{
                            int cont = 0;
                            
                            while(cont == 0){
                                int nC, volta = 0;
                                while(volta == 0){
                                    printf("Digite a numero da matricula: ");
                                    scanf("%d", &nC);
                                    system("pause");
                                    system("cls");

                                    if(nC <= 0){
                                        printf("Numero invalido para matricula, tente novamente\n");
                                        system("pause");
                                        system("cls");
                                    }
                                    else{
                                        volta = 1;
                                    }
                                }
                                int veri;
                                veri = verifica(aluno, nC);
                                if(veri==1){
                                    printf("Ja existe, tente novamente!\n");
                                    system("pause");
                                    system("cls");
                                }
                                else{
                                    cadAluno = inicializaDados(nC);
                                    aluno = cadastraDados(aluno, cadAluno);
                                    cont = 1;
                                }
                            }
                            break;
                        }

                        case 2:{
                            int des;
                            des = busca();
                            aluno = removeAluno(aluno, des);
                            break;
                        }

                        case 3:{
                            int bus;
                            bus = busca();
                            Aluno *buscador = buscando(aluno, bus);
                            if(buscador != NULL){
                                apresentaDados(buscador);
                            }
                            break;
                        }

                        case 4:{
                            exibindoCadastrados(aluno);
                            break;
                        }

                        case 0:{
                            derrubaArvore(aluno);
                            break;
                        }

                        default:{
                            printf("Opcao invalida!!\n");
                            system("pause");
                            system("cls");
                            break;
                        }
                    }

                }
                break;
            }
            
            case 0:{
                continue;
            }

            default:{
                printf("Opcao invalida!!\n");
                system("pause");
                system("cls");
                break;
            }
        }
    }
    return 0;
}

int menuEscolha(){
    int o;
    printf ("\t\t****************************************\n");
    printf ("\t\t***************** Menu *****************\n");
    printf ("\t\t****************************************\n");
    printf ("\t\t*        1 - Criar com Lista           *\n");
    printf ("\t\t*        2 - Criar com Pilha           *\n");
    printf ("\t\t*        3 - Criar com Fila            *\n");
    printf ("\t\t*        4 - Criar com Arvore          *\n");
    printf ("\t\t*        0 - Encerrar                  *\n");
    printf ("\t\t****************************************\n\n");
    printf("\t\tDigite uma opcao: ");
    scanf("%d", &o);
    system("pause");
    system("cls");
    return o;
}

int menuLista(){
    int o;
    printf ("\t\t****************************************\n");
    printf ("\t\t***************** Menu *****************\n");
    printf ("\t\t****************************************\n");
    printf ("\t\t*        1 - Cadastrar Aluno           *\n");
    printf ("\t\t*        2 - Descadastrar Aluno        *\n");
    printf ("\t\t*        3 - Buscar dados de Aluno     *\n");
    printf ("\t\t*        4 - Exibir Cadastrados        *\n");
    printf ("\t\t*        0 - Voltar                    *\n");
    printf ("\t\t****************************************\n\n");
    printf("\t\tDigite uma opcao: ");
    scanf("%d", &o);
    system("pause");
    system("cls");
    return o;
}

alunoLista *inicializaLista(){
    return NULL;
}

int vaziaLista (alunoLista *aluno){
    if (aluno == NULL){
        return 1;
    }
    else{
        return 0;
    }
}

alunoLista *cadastraAlunoLista(alunoLista *aluno, int matricula){
    alunoLista *novoCadastro = (alunoLista*) malloc(sizeof(alunoLista));
    fflush(stdin);
    printf("Digite o nome do(a) aluno(a): ");
    gets(novoCadastro->nome);
    printf("Digite a serie do(a) aluno(a): ");
    scanf("%d", &novoCadastro->serie);
    fflush(stdin);
    printf("Digite o CPF do(a) aluno(a): ");
    gets(novoCadastro->CPF);
    printf("Digite a idade do(a) aluno(a): ");
    scanf("%d", &novoCadastro->idade);
    fflush(stdin);
    printf("Digite o genero do(a) aluno(a): ");
    gets(novoCadastro->genero);

    printf("Cadastrado com sucesso!\nMatricula: %d\n", matricula);
    system("pause");
    system("cls");
    novoCadastro->matricula = matricula;
    novoCadastro->proximo = aluno;

    return novoCadastro;
}

alunoLista *descadastraAlunoLista(alunoLista *aluno, int matricula){
    alunoLista *anterior = NULL;
    alunoLista *a = aluno;
    // Verifica se quem sai é o primeiro elemento
    while (a != NULL && a -> matricula != matricula){
        anterior = a;
        a = a -> proximo;
    }
    // Verifica se a lista está vazia
    if(a == NULL){
        printf("Lista vazia, impossivel retirada!\n");
        system("pause");
        system("cls");
        return a;
    }

    if(anterior == NULL){ // Caso saia o primeiro elemento da lista
        aluno = a -> proximo;
        printf("Descadastrado com sucesso!\n");
        system("pause");
        system("cls");
    }
    else{ // Caso saia os demais elementos da lista
        anterior -> proximo = a -> proximo;
        printf("Descadastrado com sucesso!\n");
        system("pause");
        system("cls");
    }
    free(a);
    return aluno;
}

void buscaDadosAlunoLista(alunoLista *aluno, int matricula){
    alunoLista *aux = aluno;
    int verifica;
    verifica = vaziaLista(aux);

    if(verifica == 0){
        for(aux; aux != NULL; aux = aux->proximo){
            if(matricula == aux->matricula){
                printf("Dados do(a) Aluno(a)\n");
                printf("Matricula: %d\n", aux->matricula);
                printf("Nome: %s\n", aux->nome);
                printf("Serie: %d\n", aux->serie);
                printf("CPF: %s\n", aux->CPF);
                printf("Idade: %d\n", aux->idade);
                printf("Genero: %s\n", aux->genero);
                system("pause");
                system("cls");
            }
        }    
    }
    else{
        printf("Nao foi possivel buscar, pois lista esta vazia!!\n");
        system("pause");
    }
}

void exibirCadastradosLista(alunoLista *aluno){
    alunoLista *a = aluno;
    int verifica = vaziaLista(a);

    if(verifica == 0){
        for(a; a != NULL; a = a->proximo){
            printf("Matricula: %d\n", a->matricula);
            printf("Nome: %s\n", a->nome);
            printf("Serie: %d\n", a->serie);
            printf("CPF: %s\n", a->CPF);
            printf("Idade: %d\n", a->idade);
            printf("Genero: %s\n", a->genero);
            system("pause");
            system("cls");
        }
    }
    else{
        printf("Nao foi possivel exibir a lista, pois esta vazia!!\n");
        system("pause");
        system("cls");
    }
}

void liberaLista(alunoLista *aluno){
    alunoLista *aux = aluno;
    
    while(aux != NULL){    
        alunoLista *aux2 = aux->proximo;
        free(aux);
        aux = aux2;
    }
}

alunoPilha *inicializaPilha(){
    alunoPilha *aluno = (alunoPilha *) malloc(sizeof(alunoPilha));
    aluno->tamanho = 0;
    aluno->topo = NULL;
    return aluno;
}

int vaziaPilha(alunoPilha *aluno){
    if(aluno->topo == NULL){
        return 1;
    }
    else{
        return 0;
    }
}

int menuPilha(){
    int o;
    printf ("\t\t*****************************************\n");
    printf ("\t\t*********** Escolha uma Opcao ***********\n");
    printf ("\t\t*****************************************\n");
    printf ("\t\t*      1 - Cadastrar Aluno              *\n");
    printf ("\t\t*      2 - Descadastrar ultimo Aluno    *\n");
    printf ("\t\t*      3 - Exibir Cadastrados           *\n");
    printf ("\t\t*      0 - Voltar                       *\n");
    printf ("\t\t*****************************************\n\n");
    printf("\t\tDigite uma opcao: ");
    scanf("%d", &o);
    system("pause");
    system("cls");
    return o;
}

Item *inicializaDadosPilha(int matricula){ // Inicializando os dados do aluno
    Item *item = (Item *) malloc(sizeof(Item));
    fflush(stdin);
    printf("Digite o nome do(a) aluno(a): ");
    gets(item->nome);
    printf("Digite a serie do(a) aluno(a): ");
    scanf("%d", &item->serie);
    fflush(stdin);
    printf("Digite o CPF do(a) aluno(a): ");
    gets(item->CPF);
    printf("Digite a idade do(a) aluno(a): ");
    scanf("%d", &item->idade);
    fflush(stdin);
    printf("Digite o genero do(a) aluno(a): ");
    gets(item->genero);
    
    printf("Cadastrado com sucesso!\nMatricula: %d\n", matricula);
    system("pause");
    system("cls");

    item->matricula = matricula;
    return item; 
}

void cadastraAlunoPilha(alunoPilha *aluno, Item *item){ // Inserindo os dados no cadastro do aluno
    item->proximo = aluno->topo;
    aluno->topo = item;
    aluno->tamanho++;
}

Item *retiraUltimoCadastradoPilha(alunoPilha *aluno){
    int verifica;
    verifica = vaziaPilha(aluno);

    if(verifica == 0){
        Item *item = aluno->topo;
        aluno->topo = aluno->topo->proximo;
        aluno->tamanho--;
        printf("Removido com sucesso!\n");
        system("pause");
        system("cls");
        return item;
    }
    else{
        printf("Cadastro vazio!\n");
        system("pause");
        system("cls");
        return NULL;
    }
}

void exibeAlunosPilha(alunoPilha *aluno){
    Item *aux = aluno->topo;
    int verifica = vaziaPilha(aluno);

    if(verifica == 0){
        while(aux != NULL){
            printf("Dados do(a) Aluno(a)\n");
            printf("Matricula: %d\n", aux->matricula);
            printf("Nome: %s\n", aux->nome);
            printf("Serie: %d\n", aux->serie);
            printf("CPF: %s\n", aux->CPF);
            printf("Idade: %d\n", aux->idade);
            printf("Genero: %s\n", aux->genero);
            system("pause");
            system("cls");
            aux = aux->proximo;
        }
    }
    else{
        printf("Cadastro vazio!\n");
        system("pause");
        system("cls");
    }
}

void eliminaCadastroPilha(alunoPilha *aluno){
    Item *aux = aluno->topo;
    
    while(aux != NULL){
        Item *aux2 = aux;
        aux = aux->proximo;
        free(aux2);
    }
    aluno->topo = NULL;
    aluno->tamanho = 0;
}

alunoFila *inicializaFila(){
    alunoFila *aluno = (alunoFila *) malloc(sizeof(alunoFila));
    aluno->fim = NULL;
    aluno->inicio = NULL;
    aluno->tamanho = 0;
    return aluno;
}

int vaziaFila(alunoFila *aluno){
    if(aluno->inicio == NULL){
        return 1;
    }
    else{
        return 0;
    }
}

int menuFila(){
    int o;
    printf ("\t\t*****************************************\n");
    printf ("\t\t*********** Escolha uma Opcao ***********\n");
    printf ("\t\t*****************************************\n");
    printf ("\t\t*    1 - Cadastrar Aluno                *\n");
    printf ("\t\t*    2 - Descadastrar primeiro Aluno    *\n");
    printf ("\t\t*    3 - Exibir Cadastrados             *\n");
    printf ("\t\t*    0 - Voltar                         *\n");
    printf ("\t\t*****************************************\n\n");
    printf("\t\tDigite uma opcao: ");
    scanf("%d", &o);
    system("pause");
    system("cls");
    return o;
}

Item *inicializaDadosFila(int matricula){ // Inicializando dados do aluno
    Item *item = (Item*) malloc(sizeof(Item));
    item->matricula = matricula;
    fflush(stdin);
    printf("Digite o nome do(a) aluno(a): ");
    gets(item->nome);
    printf("Digite a serie do(a) aluno(a): ");
    scanf("%d", &item->serie);
    fflush(stdin);
    printf("Digite o CPF do(a) aluno(a): ");
    gets(item->CPF);
    printf("Digite a idade do(a) aluno(a): ");
    scanf("%d", &item->idade);
    fflush(stdin);
    printf("Digite o genero do(a) aluno(a): ");
    gets(item->genero);
    printf("Cadastrado com sucesso!\nMatricula: %d\n", matricula);
    system("pause");
    system("cls");
    return item;
}

void cadastraAlunoFila(alunoFila *aluno, Item *item){ // Inserindo os dados no cadastro do aluno
    item->proximo = NULL;
    int verificador = vaziaFila(aluno);
    if(verificador == 1){
        aluno->inicio = item;
    }
    else{
        aluno->fim->proximo = item;
    }
    aluno->fim = item;
    aluno->tamanho++;
}

int tamanhoFila(alunoFila *aluno){
    return (aluno->tamanho);
}

Item *retiraPrimeiroCadastradoFila(alunoFila *aluno){
    int verifica = vaziaFila(aluno);
    if(verifica == 1){
        printf("Lista vazia!\n");
        system("pause");
        system("cls");
        return NULL;
    }
    else{
        Item *aux = aluno->inicio;
        aluno->inicio = aluno->inicio->proximo;
        if(tamanhoFila(aluno) == 1){
            aluno->fim = NULL;
        }
        aluno->tamanho--;
        printf("Removido com sucesso!\n");
        system("pause");
        system("cls");
        return aux;
    }
}

void exibeCadastradosFila(alunoFila *aluno){
    Item *aux = aluno->inicio;
    int verifica = vaziaFila(aluno);

    if(verifica == 0){
        while(aux != NULL){
            printf("Dados do(a) Aluno(a)\n");
            printf("Matricula: %d\n", aux->matricula);
            printf("Nome: %s\n", aux->nome);
            printf("Serie: %d\n", aux->serie);
            printf("CPF: %s\n", aux->CPF);
            printf("Idade: %d\n", aux->idade);
            printf("Genero: %s\n", aux->genero);
            system("pause");
            system("cls");
            aux = aux->proximo;
        }
    }
    else{
        printf("Cadastro vazio!\n");
        system("pause");
        system("cls");
    }
}

void eliminaCadastradosFila(alunoFila *aluno){
    Item *aux = aluno->inicio;

    while(aux != NULL){
        Item *aux2 = aux;
        aux = aux->proximo;
        free(aux2);
    }
    aluno->fim = NULL;
    aluno->inicio = NULL;
    aluno->tamanho = 0;
}

Aluno *inicializa(){
    return NULL;
}

int menu(){
    int o;
    printf ("\t\t****************************************\n");
    printf ("\t\t***************** Menu *****************\n");
    printf ("\t\t****************************************\n");
    printf ("\t\t*        1 - Cadastrar Aluno           *\n");
    printf ("\t\t*        2 - Descadastrar Aluno        *\n");
    printf ("\t\t*        3 - Buscar dados de Aluno     *\n");
    printf ("\t\t*        4 - Exibir Cadastrados        *\n");
    printf ("\t\t*        0 - Voltar                    *\n");
    printf ("\t\t****************************************\n\n");
    printf("\t\tDigite uma opcao: ");
    scanf("%d", &o);
    system("cls");
    return o;
}

Dados *inicializaDados(int matricula){
    Dados *item = (Dados*) malloc(sizeof(Dados));
    item->matricula = matricula;
    fflush(stdin);
    printf("Digite o nome do(a) aluno(a): ");
    gets(item->nome);
    printf("Digite a serie do(a) aluno(a): ");
    scanf("%d", &item->serie);
    fflush(stdin);
    printf("Digite o CPF do(a) aluno(a): ");
    gets(item->CPF);
    printf("Digite a idade do(a) aluno(a): ");
    scanf("%d", &item->idade);
    fflush(stdin);
    printf("Digite o genero do(a) aluno(a): ");
    gets(item->genero);
    
    system("cls");
    return item;
}

int verifica(Aluno* aluno, int nC){
    int aux = 0;
    if(aluno!=NULL){
        if(nC == aluno->dados.matricula){
            aux=1;
        }else{
            if(nC < aluno->dados.matricula){
                 aux = verifica(aluno->esquerda, nC);
            }
            else if(nC > aluno->dados.matricula){
                aux = verifica(aluno->direita, nC);
            }
        }
        return aux;
    }
    return aux;
}

Aluno *cadastraDados(Aluno *aluno, Dados *item){
    if(aluno == NULL){
        Aluno *raiz = (Aluno*) malloc(sizeof(Aluno));
        raiz->dados = *item;
        raiz->esquerda = NULL;
        raiz->direita = NULL;
        return raiz;
    }
    else{
        if(item->matricula <= aluno->dados.matricula){
            aluno->esquerda = cadastraDados(aluno->esquerda, item);
        }
        else if(item->matricula > aluno->dados.matricula){
            aluno->direita = cadastraDados(aluno->direita, item);
        }
    }
    return aluno;
}

int busca(){
    int buscado;
    printf("Digite o numero do cadastro buscado: ");
    scanf("%d", &buscado);
    system("pause");
    system("cls");
    return buscado;
}

Aluno *buscando(Aluno *aluno, int matriculaBuscada){
    if(aluno != NULL){
        if(aluno->dados.matricula == matriculaBuscada){
            printf("Aluno encontrado!\n");
            system("pause");
            system("cls");
            return aluno;
        }
        else{
            if(matriculaBuscada > aluno->dados.matricula){
                return buscando(aluno->direita, matriculaBuscada);
            }
            else if(matriculaBuscada < aluno->dados.matricula){
                return buscando(aluno->esquerda, matriculaBuscada);
            }
        }
        printf("Aluno nao encontrado!\n");
        system("pause");
        system("cls");
        return NULL;
    }
    else{
        printf("Erro! Cadastro vazio!\n");
        system("pause");
        system("cls");
        return NULL;
    }
}

void apresentaDados(Aluno *aluno){
    printf("Dados do(a) Aluno(a)\n");
    printf("Matricula: %d\n", aluno->dados.matricula);
    printf("Nome: %s\n", aluno->dados.nome);
    printf("Serie: %d\n", aluno->dados.serie);
    printf("CPF: %s\n", aluno->dados.CPF);
    printf("Idade: %d\n", aluno->dados.idade);
    printf("Genero: %s\n", aluno->dados.genero);
    system("pause");
    system("cls");
}

void exibindoCadastrados(Aluno *aluno){
    if(aluno != NULL){
        exibindoCadastrados(aluno->esquerda);
        apresentaDados(aluno);
        exibindoCadastrados(aluno->direita);
    }
}

Aluno *maiorEsquerda(Aluno *aluno){
    if(aluno->direita != NULL){
        return maiorEsquerda(aluno->direita);
    }
    return aluno;
}

Aluno *removeAluno(Aluno *aluno, int quemSai){
    if(aluno != NULL){
        if(quemSai == aluno->dados.matricula){
            if(aluno->esquerda == NULL && aluno->direita == NULL){
                free(aluno);
                printf("Sucesso na remocao!\n");
                system("pause");
                system("cls");
                return NULL;
            }
            else if(aluno->esquerda != NULL && aluno->direita == NULL){
                Aluno *aux = aluno->esquerda;
                free(aluno);
                printf("Sucesso na remocao!\n");
                system("pause");
                system("cls");
                return aux;
            }
            else if(aluno->esquerda == NULL && aluno->direita != NULL){
                Aluno *aux = aluno->direita;
                free(aluno);
                printf("Sucesso na remocao!\n");
                system("pause");
                system("cls");
                return aux;
            }
            else if(aluno->esquerda != NULL && aluno->direita != NULL){
                Aluno *maior = maiorEsquerda(aluno->esquerda);
                Dados aux = maior->dados;
                aluno = removeAluno(aluno, aux.matricula);
                aluno->dados = aux;
            }
        }
        else{
            if(quemSai > aluno->dados.matricula){
                aluno->direita = removeAluno(aluno->direita, quemSai);
            }
            else if(quemSai < aluno->dados.matricula){
                aluno->esquerda = removeAluno(aluno->esquerda,quemSai);
            }
        }
        return aluno;
    }
    else{
        printf("Cadastro vazio!\n");
        system("pause");
        system("cls");
        return NULL;
    }
}

Aluno *derrubaArvore(Aluno *aluno){
    if(aluno != NULL){
        aluno->esquerda = derrubaArvore(aluno->esquerda);
        aluno->direita = derrubaArvore(aluno->direita);
        free(aluno);
        return NULL;
    }
    return aluno;
}