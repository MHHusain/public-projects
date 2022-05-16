#include<stdio.h>
#define n 5
void smallest_number_sort(int *x)
{
	int s;
	int temp;
	for(int i = 0; i < n-1;++i){
		s = i;
		for(int j = i+1;j < n;++j){
			if(x[j] < x[s]){
				s = j;
			}
		}
		temp = x[i];
		x[i] = x[s];
		x[s] = temp;
	}
}
void smallest_largest_pair(int *array)
{
	int cach;
	int i = 0;
	while(i < n){
		cach = array[n-1];
		int j = n-2;
		while(j > i){
			array[j+1] = array[j]; 
			j--;

		}
		array[i + 1] = cach;
		i = i + 2;
	}

}
int main()
{
	int arr[n] = {8,3,6,2,7};
	

	smallest_number_sort(arr);
	smallest_largest_pair(arr);

	for(int o = 0;o < n;o++){
		printf("%d\n",arr[o]);
	}
	return 0;
}
