import random

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

class ChoHanGame:
    def __init__(self):
        self.__choice = None
        self.__bet = None
        self.__money = 5000

    def place_bet(self, bet):
        if bet <= self.__money:
            self.__bet = bet
        else:
            raise ValueError(f"Ставка перевищує доступний баланс {self.__money}")

    @staticmethod
    def __roll_dice():
        return random.randint(1, 6), random.randint(1, 6)

    def choose_cho_han(self, choice):
        if choice not in ["cho", "han"]:
            raise ValueError("Введіть Cho або Han")
        self.__choice = choice


    def play_round(self):
        dice1, dice2 = self.__roll_dice()
        sum_dice = dice1 + dice2
        if sum_dice % 2 == 0:
            result = "cho"
        else:
            result = "han"
        print("The dealer lifts the cup to reveal: ")
        print(f"{JAPANESE_NUMBERS[dice1]} - {JAPANESE_NUMBERS[dice2]}")
        print(f"{dice1} - {dice2}")
        if self.__choice == result:
            print(f"You won! You take {self.__bet} mon. The house collects a 40 mon fee")
            self.__money += self.__bet - 40
        else:
            print(f"You lost! You lose {self.__bet} mon")
            self.__money -= self.__bet

    def get_money(self):
        return self.__money

def play_game():
    cho_han_game = ChoHanGame()
    while cho_han_game.get_money() > 0:
        print(f"You have {cho_han_game.get_money()} mon. How much do you bet? (or QUIT)")
        bet = input('>')
        if bet.lower() == 'quit' or 'q':
            break
        try:
            cho_han_game.place_bet(int(bet))
        except ValueError as e:
            print(e)
            continue
        print("The dealer swirls the cup and you hear the rattle of dice.")
        print("The dealer slams the cup on the floor, still covering the dice and asks for your bet")
        print("CHO (even) or HAN (odd)?")
        choice = input('>')
        try:
            cho_han_game.choose_cho_han(choice.lower())
        except ValueError as e:
            print(e)
            continue
        cho_han_game.play_round()


if __name__ == '__main__':
    play_game()