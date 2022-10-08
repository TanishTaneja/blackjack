from art import logo
import random

print(logo)


def blackjack():
    wish = input("Do you want to play blackjack.Type Y or N:\n").lower()
    
    if wish == 'y':

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 11, 10]

        def computer_card():

            computer_draw.append(random.choice(cards))

        def second_choice():
            sec_choice = input(
                "Type 'y' to get another card, type 'n' to pass:\n").lower()

            if sec_choice == 'y':
                player_addition()

            else:

                print(
                    f"Your cards:{ player_draw},final score: {sum(player_draw)}\n"
                )

                print(
                    f"Computer cards:{computer_draw }, final score of computer is {sum(computer_draw)}"
                )
                
                blackjack()

        def player_addition():

            player_draw.append(random.choice(cards))

            computer_card()

            if sum(player_draw) < 21:
                print(
                    f"Your cards:{ player_draw},current score: {sum(player_draw)}\n"
                )

                print(f"Computer first card:{computer_draw[0]}")

            elif sum(player_draw) > 21:
                if 11 in player_draw:
                    player_draw.remove(11)
                    player_draw.append(1)
                    print(
                    f"Your cards:{ player_draw},current score: {sum(player_draw)}\n"
                )

                    print(f"Computer first card:{computer_draw[0]}")
                    second_choice()

                else:
                    print(
                        f"Your final hand: {player_draw}, final score: {sum(player_draw)}\nComputer's final hand: {computer_draw}, final score: {sum(computer_draw)}\nYou went over. You lose"
                    )
                    blackjack()

            elif sum(player_draw) == 21:
                print("Blackjack!!!!!!!!!!!!!!!\n You Won.")
                blackjack()
            second_choice()
        player_draw = random.sample(cards, k=2)
        
        
            
            
        
        computer_draw = random.sample(cards, k=2)
        print(f"Your cards:{ player_draw},current score: {sum(player_draw)}\n")
        print(f"Computer first card:{computer_draw[0]}")
        
        second_choice()

    else:
        print("Hope you enjoyed.")

    
blackjack()
