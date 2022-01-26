#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int cuenta_vocales(char *letrita){
	int n_vocales=0;
	int cont;
	int longitud;
	longitud=strlen(letrita);
//	printf("\nSoy la funcion y me has enviado la palabra %s",letrita);
//	printf("\nSu longitud es de %d",longitud);
	for(cont=0;cont<longitud;cont++){
		printf("\nLa letra %d es %c",cont,*(letrita+cont));
		if(*(letrita+cont)=='A' || *(letrita+cont)=='a'){
			n_vocales++;
//			printf("\nTiene una a. De momento %d vocales",n_vocales);
		}
		if(*(letrita+cont)=='E' || *(letrita+cont)=='e')
			n_vocales++;
		if(*(letrita+cont)=='I' || *(letrita+cont)=='i')
			n_vocales++;
		if(*(letrita+cont)=='O' || *(letrita+cont)=='o')
			n_vocales++;
		if(*(letrita+cont)=='U' || *(letrita+cont)=='u')
			n_vocales++;		
	}
	return(n_vocales);
}


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
		printf("\nLa palabra %s tiene %d vocales\n",provisional,cuenta_vocales(provisional));
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
	//las ordeno por num de vocales
	//la ordeno de menor a mayor
	for(repetir=1;repetir<5;repetir++){
		for(cont=0;cont<=3;cont++){
			if(cuenta_vocales(mispalabras[cont])>cuenta_vocales(mispalabras[cont+1])){
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
