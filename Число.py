# Написать игру "Угадай число". Компьютер загадывает случайное число от 1 до 20,
# а пользователь должен его угадать. Компьютер должен давать подсказки в виде "слишком много" или "слишком мало".
import random
ai_choice = random.randint(1, 500)
print(ai_choice)
player_choice = 0
while player_choice != ai_choice:
    player_choice = int(input("ИИ загадал число от 1 до 20, попробуй его угадать!"))
    if player_choice > ai_choice:
        print("Слишком много!")
    elif player_choice < ai_choice:
        print("Слишком мало!")
print("Молодец, ты выиграл!")
