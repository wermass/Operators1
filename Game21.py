import random


def get_card():
    cards = [2, 3, 4, 6, 7, 8, 9, 10, 11]
    card = random.choice(cards)
    return card

def calculate_score(hand):
    return sum(hand)



player_hand = [get_card(), get_card()]
print(player_hand)
dealer_hand = [get_card(), get_card()]
print(dealer_hand)
print(calculate_score(player_hand), calculate_score(dealer_hand))
print("Добро пожаловать в игру 21!")
while True:
    player_score = calculate_score(player_hand)
    print(f"У вас {player_score} очков")
    if player_score == 21:
        print("Вы выиграли! У вас 21.")
        break
    elif player_score > 21:
        print("Перебор! Диллер проиграл.")
        break
    action = input("Хотите взять карту?(да/нет)")
    if action.lower() == "да":
        player_hand.append(get_card())
    elif action.lower() == "нет":
        break
    else:
        print("Введите корректный ответ.")
while True:
    dealer_score = calculate_score(dealer_hand)
    if dealer_score >= 16:
        break
    else:
        dealer_hand.append(get_card())
if player_score == 21 and dealer_score == 21:
        print("Диллер выиграл.")
elif dealer_score > 21:
        print("Вы выиграли!")
else:
        print("Диллер выиграл.")
print(f"Карты диллера: {dealer_score} карты игрока: {player_score}")