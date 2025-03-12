import random
import os


def clear_screen():
    """Clear the terminal screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def roll():
    """Simulate rolling a six-sided die."""
    return random.randint(1, 6)


def get_player_count():
    """Get the number of players (2-4) from the user."""
    while True:
        players = input("Enter the number of players (2-4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print("Invalid input! The number of players must be between 2 and 4.")
        else:
            print("Invalid input! Please enter a valid number.")


def get_max_score():
    """Get the maximum score needed to win from the user."""
    while True:
        max_score = input("Enter the maximum score needed to win: ")
        if max_score.isdigit() and int(max_score) > 0:
            return int(max_score)
        else:
            print("Invalid input! Please enter a positive number for the maximum score.")


def get_max_rolls():
    """Get the maximum number of rolls allowed per turn from the user."""
    while True:
        max_rolls = input("Enter the maximum number of rolls allowed per turn: ")
        if max_rolls.isdigit() and int(max_rolls) > 0:
            return int(max_rolls)
        else:
            print("Invalid input! Please enter a positive number for the maximum rolls per turn.")


def take_turn(player_idx, max_rolls, player_scores):
    """Handle a player's turn (deciding whether to roll and keeping track of their score)."""
    print(f"\nPlayer {player_idx + 1}'s turn has just started!")
    print(f"Your total score is: {player_scores[player_idx]}\n")
    current_score = 0
    rolls_left = max_rolls
    while rolls_left > 0:
        while True:
            should_roll = input("Would you like to roll? (Yes/No): ").strip().lower()
            if should_roll == "yes":
                break
            elif should_roll == "no":
                print("You decided not to roll. Ending your turn.")
                return player_scores 
            else:
                print("Invalid input! Please type 'Yes' or 'No'.")
        value = roll()
        rolls_left -= 1
        if value == 1:
            print("You rolled a 1! Your turn is over, and you lose all points for this turn.")
            current_score = 0  
            break
        else:
            current_score += value
            print(f"You rolled a: {value}")
            print(f"Your score this turn is: {current_score}")
        if rolls_left == 0:
            print("You have reached the maximum number of rolls for this turn.")
            break
    player_scores[player_idx] += current_score
    print(f"Your total score is now: {player_scores[player_idx]}")
    return player_scores


def check_winner(player_scores, max_score):
    """Check if a player has won by reaching the maximum score."""
    for player_idx, score in enumerate(player_scores):
        if score >= max_score:
            print(f"\nPlayer {player_idx + 1} wins with a score of {score}!")
            return True
    return False


def ask_restart():
    """Ask the player if they want to restart the game after a winner is found."""
    while True:
        restart = input("\nWould you like to play again? (Yes/No): ").strip().lower()
        if restart == "yes":
            return True
        elif restart == "no":
            print("Thanks for playing! Goodbye!")
            return False
        else:
            print("Invalid input! Please type 'Yes' or 'No'.")


def main():
    """Main game loop: get inputs, run the game, and check for winner."""
    while True:
        clear_screen() 
        players = get_player_count()
        max_score = get_max_score()
        max_rolls = get_max_rolls()
        player_scores = [0] * players
        while True:
            for player_idx in range(players):
                clear_screen() 
                player_scores = take_turn(player_idx, max_rolls, player_scores)
                if check_winner(player_scores, max_score):
                    if not ask_restart():
                        return
                    break

main()
