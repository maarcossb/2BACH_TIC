#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
	//RESERVA DINAMICA DE MEMORIA
	char aux[10]; //Reservo una variable auxiliar para guardar el momento de la palabra
	int longitud; //Defino el tamaño 
	char *lista[3];
	int cont;
	for(cont=0;cont<3;cont++){
		//1. Leo el nombre en un
		printf("\nDime el nombre del rey %d: ",cont);
		//2. Lo guardo en una variable auxiliar
		scanf("%s",aux);
		//3. Cuento el numero de letras
		longitud=strlen(aux);
		//4. Busco un hueco em la memoria de ese tamaño y me apunto su direccion
		lista[cont]=(char*)malloc(longitud*sizeof(char));
		//5.Copio el nombre desde auxiliar hasta el hueco encontrado
		strcpy(lista[cont],aux);
	}
	printf("\n LOS TRES REYES MAGOS SON: "); //Contiene spoilers
	for(cont=0;cont<3;cont++){
		printf("\n %s",lista[cont]);
	}
	return(0);
	

}
