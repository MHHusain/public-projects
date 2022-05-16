#include<iostream>
int smallest(int *index,int n=1) {
	int i, temp, i2 = 0;
	while (i2 < n) {

		i = i2 + 1;
		while (i < 6) {
			if (index[i] < index[i2]) {
				temp = index[i];
				index[i] = index[i2];
				index[i2] = temp;

			}

			i++;
		}

		i2++;
	}

	return index[n - 1];

}
int main() {
	int a[6] = {2,3,-90,5,7,55};
	std::cout << smallest(a);
	/*int x = 0;
	while (x < 6) {
		std::cout << a[x]<< " ";
		x++;
	}*/
	return 0;
}