#include<iostream>
int main(){
	int a[6] = {3,5,7,3,2,5};
	int i,i2=0,n=3,temp;
	int smallest;
	while(i2<n){
		smallest = a[i2];
		i = i2+1;
		while(i<6){
			if(a[i]<smallest){
				temp = a[i];
				a[i] = a[0];
				a[0] = temp;
				
			}
			
			i++;			
		}
		
		i2++;
	}
	std::cout << a[i2-1];
	return 0;
}