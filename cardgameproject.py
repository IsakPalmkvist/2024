import random
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks= ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values={"One":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}
class Card: 
    #suit, rank, value
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit #assumes that rank and suit are strings

two_hearts=Card("Hearts", "Two")
print(two_hearts.value)
three_clubs=Card("Clubs", "Three")

class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name=name
        self.deck=[]
    
    def remove_one(self):
        return self.deck.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) ==type([]):
            self.deck.extend(new_cards)
        else:
            self.deck.append(new_cards)
        
    
    def __str__(self):
        return f"Player {self.name} has {len(self.deck)} cards"

player1=Player("One")
player2=Player("Two")
new_deck=Deck()
new_deck.shuffle()


for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())

game_on=True

round_num=0
while game_on:

    round_num+=1
    print(f"Round {round_num}")

    if  len(player1.deck)==0:
        print("Player one out of cards! Player Two wins!")
        game_on=False
        break

    if  len(player2.deck)==0:
        print("Player Two out of cards! Player One wins!")
        game_on=False
        break
    #start a new round
    player1_cards=[]
    player1_cards.append(player1.remove_one())

    player2_cards=[]
    player2_cards.append(player2.remove_one())

    at_war=True

    while at_war:
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)

            at_war=False

        elif player2_cards[-1].value > player1_cards[-1].value:
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)

            at_war=False

        else:
            print("War!")

            if len(player1.deck)<5:
                print("Player One unable to declare war")
                print("Player Two wins!")
                game_on=False
                break

            elif len(player2.deck)<5:
                print("Player Two unable to declare war")
                print("Player One wins!")
                game_on=False
                break
            
            else:
                for num in range(3):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())

            
    

        






