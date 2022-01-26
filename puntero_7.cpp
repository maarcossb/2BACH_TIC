#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
	char provisional[10];
	char *aux; 
	int longitud;  
	char *mispalabras[5];
	int cont;
	int repetir;
	for(cont=0;cont<5;cont++){
		//1. Pido la palabra
		printf("\nDime la palabra %d: ",cont);
		//2. Lo guardo en una variable auxiliar
		scanf("%s",provisional);
		//3. Cuento el numero de letras
		longitud=strlen(provisional);
		//4. Busco un hueco en la memoria de ese tamaño y me apunto su direccion
		mispalabras[cont]=(char*)malloc(longitud*sizeof(char));
		//5.Copio el nombre desde auxiliar hasta el hueco encontrado
		strcpy(mispalabras[cont],provisional);
	}
	printf("\n LAS CINCO PALABRAS SON: "); //Contiene spoilers
	for(cont=0;cont<5;cont++){
		printf("\n %s",*(mispalabras+cont));
		//SUSTITUYO mispalabras[cont] por *(mispalabras+cont)
	}
	//las ordeno por tamaño
	//la ordeno de menor a mayor
	for(repetir=1;repetir<5;repetir++){
		for(cont=0;cont<=3;cont++){
			if(strlen(mispalabras[cont])>strlen(mispalabras[cont+1])){
				aux=mispalabras[cont];
				mispalabras[cont]=mispalabras[cont+1];
				mispalabras[cont+1]=aux;
			}
		}
	}
	//VUELVO A MOSTRAR LAS PALABRAS PERO ORDENADAS
	printf("\n LAS CINCO PALABRAS ORDENADAS SON: "); //Contiene spoilers
	for(cont=0;cont<5;cont++){
		printf("\n %s",*(mispalabras+cont));
	}

	return(0);
	

}
