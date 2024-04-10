#include <stdio.h>
int main(){
    int t=0;
    scanf("%d", &t);
    int i;
    for (i=0; i<t; i++){
        int n;
        scanf("%d", &n);
        int j, sum=0, buf=0;
        for (j=0; j<n; j++){
            scanf("%d", &buf);
            sum+=buf;
        }
        printf("%d\n", sum);
    }
}