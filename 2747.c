#include <stdio.h>
int main(){
    int x=1, y=1, n=0;
    scanf("%d", &n);
    if (n==0) printf("0");
    else {
        int i;
        int temp;
        for (i=0; i<n-2; i++){
            temp=x+y;
            x=y;
            y=temp;
        }
        printf("%d",y);
    }
}