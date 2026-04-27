import kotlin.random.Random
import kotlin.random.nextInt

fun main() {
    // Create players
    val player1 = createPlayer()
    val player2 = createPlayer()

    // Game condition - While no player has won
    while(player1.score < 10 && player2.score < 10) {

        // Player 1 turn
        println("It's ${player1.name}'s turn!")
        player1.roll()
        println("${player1.name}'s current score: ${player1.score}\n")

        // Check if player 1 has won after their turn
        // This stops player 2 from taking a turn when player 1 has already won
        if(player1.score > 10){
            break
        }

        // Player 2 turn
        println("It's ${player2.name}'s turn!")
        player2.roll()
        println("${player2.name}'s current score: ${player2.score}\n")
    }

    // Compare scores to determine winner
    val winner = if(player1.score > player2.score) player1.name else player2.name
    println("${winner} is the winner!")
    println("${player1.name} : ${player1.score} Points")
    println("${player2.name} : ${player2.score} Points")


}

fun createPlayer(): Player{
    println("Choose a player name: ") // Query the user
    val playerName = readln().trim() // Get rid of surrouning whitespace
    if(playerName.isEmpty() || playerName.isBlank()) { // Check if user has inputted any amount of characters
        println("Please enter a valid player name.")
        return createPlayer() // If invalid, query the user again
    } else {
        return Player(playerName)
    }

}


class Player(val name: String){
    var score = 0

    fun roll(): Boolean{
        // Recursive function so user can keep rolling if they decide

        // Roll the die
        val rollVal = Random.nextInt(1,7) // (1 - 6) - last val in range is exclusive
        println("${this.name} rolled a ${rollVal}!")

        // Base case: Player rolls a 1 - return false, no values get added to score
        if(rollVal == 1){
            println("SKIP TURN!")
            return false
        }

        // If queryPlayer returns true (Player chooses hold)
        // Add the rollVal to player score and return true
        if(queryPlayer()) {
            this.score += rollVal
            return true
        }

        // If roll() returns true (player chooses to hold at top of stack)
        // add rollVal to score and return true for the function we came from
        if(roll()) {
            this.score += rollVal
            return true
        } else {
            // If roll() returns false, user rolled a 1
            return false
        }
    }

    fun queryPlayer(): Boolean{
        // Ask user if they want to roll or hold
        println("${this.name}, hold or roll again? ('H' / 'R')\n")
        // Normalise the input
        val input = readln().uppercase().trim()

        // Check if input is either of options
        if (input == "H") {
            return true // TRUE = Hold
        } else if(input == "R") {
            return false
        } else {

            // If input is invalid, query the player again and return the answer
            println("Please choose a valid option ('H' / 'R')")
            return queryPlayer()
        }
    }
}


