#include<iostream>
using namespace std;
int main()
{
    int x[]= {5,3,2,6};
    int i;
    int largest=x[0];
    int largest_index;
    int temp;
    int smallest=x[0];
    int smallest_index;

    while(i<4){

            if (x[i]>largest){

                largest = x[i];

                largest_index = i;
            }
            if(x[i]<smallest){
                smallest=x[i];
                smallest_index = i;

            }

        i++;
    }


    temp = x[largest_index];
    x[largest_index] = x[smallest_index];
    x[smallest_index] = temp;
    cout<<x[2];
}
