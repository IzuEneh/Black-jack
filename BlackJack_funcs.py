playing = True


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("Hey place a bet!: "))
        except ValueError:
            print("Hey that's not a number")
        else:
            if chips.bet > chips.total:
                print("Hey you don't have enough for that! You have {} left".format(chips.total))
            else:
                break


def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):

    while True:
        choice = input('Hit or Stand? ')

        if choice.lower() == 'hit':
            hit(deck, hand)
            print(hand.cards, hand.value, '\n')
        elif choice.lower() == 'stand':
            print('dealers turn')
            break
        else:
            print("That's not a valid input, try again!")


def show_some(player, dealer):
    print('This is the player: ')
    print('\t', player.cards)
    print('\n')
    print('This is the dealer: ')
    print('\t', dealer.cards[1])
    print('\n')


def show_all(player, dealer):

    print('This is all the players cards: ')
    print('\t', player.cards, player.value)
    print('\n')
    print('This is the dealers cards: ')
    print('\t', dealer.cards, dealer.value)
    print('\n')


def player_busts(chips):
    chips.lose_bet()
    print('\n')
    print('You lost!'.upper())
    print('\n')


def player_wins(chips):
    chips.win_bet()
    print('\n')
    print('You won!'.upper())
    print('\n')


def dealer_busts(chips):
    chips.win_bet()
    print('\n')
    print('Dealer busted You Win!')
    print('\n')


def dealer_wins(chips):
    chips.lose_bet()
    print('\n')
    print('Dealer Won You Lost!')
    print('\n')


def push():
    print('\n')
    print('It was a tie !')
    print('\n')
