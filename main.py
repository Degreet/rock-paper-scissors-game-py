import random

def start():
  print("Что выбрать?\n1) Камень\n2) Ножницы\n3) Бумага")
  user_choice = input(">> ")

  if user_choice == "1" or user_choice == "2" or user_choice == "3":
    bot_choice = str(random.randint(1, 3))

    if user_choice == "1" and bot_choice == "2" or user_choice == "2" and bot_choice == "3" or user_choice == "3" and bot_choice == "1":
      show(bot_choice)
      win()
    elif user_choice == bot_choice:
      show(bot_choice)
      draw()
    else:
      show(bot_choice)
      defeat()
  else:
    print("Ошибка.\n")
    start()

def show(bot_choice):
  print("\nБот выбрал: " + bot_choice.replace("1", "Камень").replace("2", "Ножницы").replace("3", "Бумага"))

def win():
  print("Вы выиграли!\n")
  start()

def defeat():
  print("Вы проиграли!\n")
  start()

def draw():
  print("Ничья!\n")
  start()

start()