#include<stdio.h>
#define n 5
int main(){
	int arr[n][n] = {
				{1, 2, 3, 4, 5},
				{6, 7, 8, 9, 10},
				{11,12,13,14,15},
				{16,17,18,19,20},
				{21,22,23,24,25}
			};
	
	
	for(int start = 0; start <= n / 2;start++){
		for(int i = start; i < n - start ;i++){
			
			printf("%d\n",arr[i][n-start-1]);
			
			
		
		}
		
	}
	
	return 0;
}
