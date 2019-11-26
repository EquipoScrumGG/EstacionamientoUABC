#include <stdio.h>
#include <stdlib.h>
#include "MyLib.h"
#define M 140

int main(){
    char linea[M];
    char *numemp;
    char *name;
    char semana[16][6];

    char path[20],yn;
    int i,n, suma;
    printf("\n\tDesea abrir hor_gen.txt [y/n]: ");
    //yn = getch();
    yn = tolower(yn);
    if (yn == 'y' || yn ==  '\r')
      pf = fopen("hor_gen.txt","r");
    else{
     system("dir *.txt");
     printf("\n\tNombre del archivo a abrir: ");
     scanf("%s",path);
     pf = fopen(path,"r");
    }

    if(pf == NULL){
      printf("\n\tNo existe archivo...");
    }
    else{
       printf("\n\tNombre del documento modificado hor_gen.xls  [y/n]");
//       yn = getch();
       yn = tolower(yn);
       if (yn == 'y' || yn == '\r')
         pf1 = fopen("hor_gen.xls","w+");
       else{
          printf("\n\tNombre del archivo a salvar: ");
          scanf("%s",path);
          strcat(path,".csv");
          printf("\tSu archivo se llama %s",path);
          pf1 = fopen(path,"w+");
       }
       if(pf == NULL){
         printf("\n\tNo existe archivo...");
       }
       else{
          fprintf(pf1,"#,N Empleado,MAESTRO,Horario,Lunes,Martes,Miercoles,Jueves,Viernes,Sabado\n");
          while(fgets(linea,M,pf)){
             if(EsProfesor(linea)){
                numemp = getNEmpl(linea);
                name = getNomEmpl(linea);
                //fprintf(pf1,"\t%s\t%s\n",numemp,name);
                for(i = 0; i < 5; i++)
                   fgets(linea,M,pf);
                suma = 0;
                for(i = 0; i < 16; i++){
                   for(n = 0; n < 6; n++){
                      if(isdigit(linea[17 + 17*n])){
                        semana[i][n] = 'X';
                        suma++;
                      }
                      else
                        semana[i][n] = ' ';
                   }
                   fgets(linea,M,pf);fgets(linea,M,pf);fgets(linea,M,pf);
                }
                for(i = 0; i < 16; i++){
                   fprintf(pf1,",%s,%s,%d:00 - %d:00",numemp,name,7+i,8+i);
                   for(n = 0; n < 6; n++){
                      fprintf(pf1,",%c",semana[i][n]);
                   }
                   fprintf(pf1,"\n");
                }
                fprintf(pf1,",%s,%s,%d,",numemp,name,suma);

             }


          }
       }
    }
    fclose(pf);
    fclose(pf1);
    return 0;
}
