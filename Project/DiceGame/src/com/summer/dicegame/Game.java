package com.summer.dicegame;

import java.util.Random;
import java.util.Scanner;

public class Game {

	public static void main(String[] args) {
		
		Scanner reader = new Scanner(System.in);
		
		int scoreP1 = 0;
		int scoreP2 = 0;
		
		//Array to reference by index
		int[] scores = {scoreP1, scoreP2};
		
		int unheld1 = 0;
		int unheld2 = 0;
		
		//Array
		int[] unhelds = {unheld1, unheld2};
		
		int playerTurn = 1;
		
		//Get Player Names
		System.out.println("Enter Player 1 Name: ");
		String p1Name  = reader.nextLine();
		System.out.println("Player 1: " + p1Name);
		
		lineBreak();
		
		System.out.println("Enter Player 2 Name: ");
		String p2Name  = reader.nextLine();
		System.out.println("Player 2: " + p2Name);
		
		lineBreak();
		
		String[] names = {p1Name, p2Name};
		
		//Main Game Loop:
		while(scoreP1 < 100 && scoreP2 < 100) {
			
			lineBreak();
			
			System.out.println("p" + playerTurn + ": " + names[playerTurn-1] + ", 1 for Roll, or 2 for Hold?");
			
			int input = reader.nextInt();
			
			//Roll
			if(input == 1) {
				
				int rollValue = rollDice();
				
				if (rollValue == 1) {
					unhelds[playerTurn-1] = 0;  
					playerTurn = switchTurn(playerTurn);
					System.out.println("You rolled a 1! switching to p" + playerTurn + ": " + names[playerTurn - 1]);
					System.out.println("p1: " + names[0] + " score = " + scores[0]);
					System.out.println("p2: " + names[1] + " score = " + scores[1]);
					//Reset unheld values
					for(int i = 0; i < unhelds.length; i++) {
						unhelds[i] = 0;
					}
					
				}else {
					unhelds[playerTurn-1] += rollValue;

					System.out.println("You rolled a " + rollValue);
					System.out.println("Total unheld score: " + unhelds[playerTurn-1]);
				}
				
	
			//Hold
			}else if(input == 2) {
				scores[playerTurn-1] += unhelds[playerTurn-1];
				System.out.println("p1: " + names[0] + " score = " + scores[0]);
				System.out.println("p2: " + names[1] + " score = " + scores[1]);
				playerTurn = switchTurn(playerTurn);
				
				
			//Invalid Input
			}else if(input == 3){
				scores[playerTurn-1] += 150;
				
			}else {
				System.out.println("invalid");
			}
			
		}
		
		for (int i = 0; i < scores.length; i++) {
			if(scores[i] > 100) {
				System.out.println("Player " + i+1 + ": " + names[i+1] + " wins! score: " + scores[i]);
			}
		}
		
	}
	
	//Generate number 1-6
	public static int rollDice() {
		
		Random rand = new Random();
		
		//Add 1
		return rand.nextInt(6) + 1;
		
	}
	
	//Return the number of the other player to switch the turn
	public static int switchTurn(int current) {
		
		if(current == 1) {
			return 2;
		}else if(current == 2) {
			return 1;
		}
		return 0;
		
	}
	
	//Line break for easier reading
	public static void lineBreak() {
		
		System.out.println();
		System.out.println("------------------------------");
		System.out.println();
		
	}
	
}
