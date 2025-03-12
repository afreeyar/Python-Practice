import random
import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


def card_value(card):
    rank, _ = card
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)


def hand_value(hand):
    total = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card[0] == 'A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


def get_player_count():
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


def deal_initial_cards(deck, players):
    hands = {f'Player {i+1}': [deck.pop(), deck.pop()] for i in range(players)}
    dealer_hand = [deck.pop(), deck.pop()]
    return hands, dealer_hand


def print_hands(hands, dealer_hand, show_dealer_card=False):
    for player, hand in hands.items():
        print(f"{player}'s hand: {', '.join(f'{rank} of {suit}' for rank, suit in hand)} - Total: {hand_value(hand)}")
    dealer_hand_display = f"{dealer_hand[0][0]} of {dealer_hand[0][1]} and [Hidden]"
    if show_dealer_card:
        dealer_hand_display = f"{dealer_hand[0][0]} of {dealer_hand[0][1]} and {dealer_hand[1][0]} of {dealer_hand[1][1]}"
    print(f"\nDealer's hand: {dealer_hand_display}")
    print()


def player_turn(player, hand, deck):
    while hand_value(hand) < 21:
        print(f"Your current hand: {', '.join(f'{rank} of {suit}' for rank, suit in hand)} - Total: {hand_value(hand)}")
        action = input(f"{player}, do you want to 'Hit' or 'Stand'? ").strip().lower()
        if action == 'hit':
            hand.append(deck.pop())
            print(f"You drew a {hand[-1][0]} of {hand[-1][1]}.")
        elif action == 'stand':
            print(f"You stand with a total of {hand_value(hand)}.")
            break
        else:
            print("Invalid input! Please type 'Hit' or 'Stand'.")
    return hand


def dealer_turn(dealer_hand, deck):
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print(f"Dealer drew a {dealer_hand[-1][0]} of {dealer_hand[-1][1]}.")
    print(f"Dealer stands with a total of {hand_value(dealer_hand)}.")
    return dealer_hand


def check_winner(hands, dealer_hand):
    dealer_total = hand_value(dealer_hand)
    print(f"\nDealer's hand: {', '.join(f'{rank} of {suit}' for rank, suit in dealer_hand)} - Total: {dealer_total}")
    winners = []
    for player, hand in hands.items():
        player_total = hand_value(hand)
        if player_total > 21:
            print(f"{player} busts with {player_total}.")
        elif dealer_total > 21 or player_total > dealer_total:
            print(f"{player} wins with {player_total}!")
            winners.append(player)
        elif player_total < dealer_total:
            print(f"{player} loses with {player_total}.")
        else:
            print(f"{player} ties with the dealer.")
    return winners


def ask_restart():
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
    while True:
        clear_screen()
        players = get_player_count()
        deck = create_deck()
        hands, dealer_hand = deal_initial_cards(deck, players)
        print_hands(hands, dealer_hand)
        for player, hand in hands.items():
            hands[player] = player_turn(player, hand, deck)
        dealer_hand = dealer_turn(dealer_hand, deck)
        winners = check_winner(hands, dealer_hand)
        if winners:
            print(f"Congratulations to: {', '.join(winners)}!")
        if not ask_restart():
            break
main()
