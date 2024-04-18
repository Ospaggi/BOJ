#include <stdio.h>
int main() {
	char s[50];
	int sum=0;
	scanf("%s", s);
	for (int i = 0; s[i] != 0; i++) sum+=(s[i + 1] == s[i]) ? 10 : 15; 
	printf("%d", sum);
	return 0;
}
