#include "MyLib.h"

char nom[42];
char num[7];


//numero de pagina donde se encuentra el registro
int EsProfesor(char *lin){  //ok
   char Pag[] = "PROFESOR";
   int ans = 0;
   if(strncmp(lin,Pag,8) == 0)
      ans = 1;
   return(ans);
}

//obtengo el numero de empleado
char* getNEmpl(char *lin){
  //char num[] = "      ";
  int i = 0,ind = 10;
  strcpy(num,"      ");
  while(isdigit(lin[ind]) == 0){
    ind++;
  }
  while(isdigit(lin[ind+i])){
    num[i] = lin[ind+i];
    i++;
  }
  return(num);
}


//obtengo el nombre de empleado
char * getNomEmpl(char *lin){
  //char nom[] = "                                        ";
  int i = 0,ind = 23;
  strcpy(nom,"                                        ");
  while(lin[ind+i]!= '\n'){
    nom[i] = lin[ind+i];
    i++;
  }
  nom[i-1] = ' ';
  return(nom);
}













