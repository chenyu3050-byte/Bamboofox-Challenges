#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>//hint :call system call

char message[48];//it appears in the section of .bbs  =global variable 

int main()
{
  char name[16];
  printf("Give me your message: ");
  fflush(stdout);
  read(0, message, 0x30);
  printf("Give me your name: ");
  fflush(stdout);
  read(0, name, 0x30);//we can transmit more bits to control the flow
  return 0;
}
