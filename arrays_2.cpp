#include<stdio.h>

int main(){
	float x[10];
	int cont;
	float media;
	float suma=0;
//	cont++ equivale a cont=cont+1
/*	while(cont<=10){
		...
		cont++;
	}
*/
	for(cont=0;cont<10;cont++){
//		num=input("dame un numero: ")
		printf("Dame un numero: ");
		scanf("%f",&x[cont]);
		
	}
	
	for(cont=0;cont<10;cont++){
		printf("\nx[%f.2]=%f.2",cont,x[cont]);
		suma+=x[cont];
//		suma=suma+x[cont];
	}
	media=suma/cont;
	printf("\nLA MEDIA VALE: %.2f",media);
	
	
	return(0);

}
