from BlackJack_classes import *
from BlackJack_funcs import *


def restart():
    print('\n'*100)
    game_deck.shuffle()
    for i in range(2):
        player.add_card(game_deck.deal())
        dealer.add_card(game_deck.deal())
    take_bet(player_chips)
    show_some(player, dealer)

while True:
    # Print an opening statement
    print('Hello and welcome to BlackJack!')
    player = Hand()
    dealer = Hand()

    # Create & shuffle the deck, deal two cards to each player
    game_deck = Deck()
    game_deck.shuffle()

    for i in range(2):
        player.add_card(game_deck.deal())
        dealer.add_card(game_deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)

    while True:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(game_deck, player)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player_chips)

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer.value < 17:
            hit(game_deck, dealer)

        # Show all cards
        show_all(player, dealer)
        # Run different winning scenarios
        if (player.value > dealer.value) or (player.value == 21):
            player_wins(player_chips)
        elif dealer.value > 21:
            dealer_busts(player_chips)
        elif dealer.value > player.value:
            dealer_wins(player_chips)
        else:
            push()

        # Inform Player of their chips total 
        print(f'You have {player_chips.total} chips left!')

        # Ask to play again
        replay = input("Wanna play again??? (Y/N): ")
        if replay == 'Y'.lower():
            player.new()
            dealer.new()
            game_deck.new()
            restart()
        else:
            print('Thanks for Playing !')
            break
    break
