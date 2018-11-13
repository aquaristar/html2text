#include <stdio.h>
#include <string.h>

#define IN 0
#define OUT 1

int main(void) {
 int c = 0;
 int state = OUT;
 int tstate = OUT;
 char tagbuff[2048];
 char *ptr1 = NULL;

 ptr1 = tagbuff;

 while((c = getchar()) != EOF) {
  /* copy tag into tagbuff */
  if(c == '<' || c == '&') state = IN;
  if(state == IN) *ptr1++ = c;
  if(c == '>' || c == ';') { 
   state = OUT; *ptr1++ = '\0'; 

   /* search tagbuff, javascript, style tags */
   if(strstr(tagbuff, "<s") != 0 || strstr(tagbuff, "<S") != 0)
    tstate = IN;
   if(strstr(tagbuff, "</") != 0)
    tstate = OUT;

   /*   ? */
   if(strstr(tagbuff, "nbsp") != 0 || strstr(tagbuff, "NBSP") != 0)
    printf(" ");

   ptr1 = tagbuff;
  } /* end if */

  /* not in a tag, print character */
  if(state == OUT && tstate == OUT && c != '>' && c != ';')
   printf("%c", c);
 }

 return 0;
}
