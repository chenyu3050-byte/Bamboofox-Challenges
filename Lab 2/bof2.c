#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void y0u_c4n7_533_m3()
{
  int allow = 0;
  if (allow) {
    execve("/bin/sh", 0, 0);
  }
  else {
    puts("Oh no~~~!");
    exit(0);
  }
}

int main()
{
  char buf[16];
  puts("This is your second bof challenge ;)");
  fflush(stdout);
  read(0, buf, 0x30);
  if (strlen(buf) >= 16) {//check the length
    puts("Bye bye~~");                                  //modify
    exit(0);    //we can find ay least 24*'a'if we want revise the return address
  }                   //by IDA pro ,so we must make strlen() invalid
  return 0;
}
