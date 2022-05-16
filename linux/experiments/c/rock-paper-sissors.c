#include<stdio.h>
enum rpc{
	ROCK,
	PAPER,
	SISSORS
}
struct Player{
	char name[50];
	enum rpc choice;

}
typedef struct Player Player
int main(){
	Player player1, player2;
	
	
	player1.name="muntathar";
	player2.name="mahdy";
	
	player1.choice=ROCK;
	
	player2.choice=ROCK;
	
	
	if(player1.choice == player2.choice){
		printf("a tie");
	}
	else{
		 if(player1.choice == ROCK && player2.choice == SISSORS){
		 	printf("%s wins",player2.choice);
		 
		 }
		 if(player1.choice > player2.choice){
			printf("%s wins",player1.name);
			}
		else{
			printf("%s wins",player2.name);
			}
		
	}
}

