#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
	//RESERVA DINAMICA DE MEMORIA
	char aux[100]; //Reservo una variable auxiliar para guardar el momento de la palabra
	int longitud; //Defino el tamaño 
	printf("Dime una palabra: ");
	scanf("%s",aux);
	longitud=strlen(aux);
	char *palabra; //palabra es un puntero (una variable que contiene 
	//una dirección de memoria de algo que es una letra)
	palabra=(char*)malloc(longitud*sizeof(char)); //memory allocation
	strcpy(palabra,aux);
	printf("\nRESULTADO: ");
	printf("%s",palabra);
	return(0);
	

}
