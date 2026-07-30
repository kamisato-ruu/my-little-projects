import random

computer = random.choice(['rock', 'paper', 'scissor'])
beats = {'rock' : 'scissor', 'paper' : ' rock', 'scissor' : 'paper' }

player = input("Pick rock, paper or scissor : ").strip().lower()

print(f"You pick {player} computer use {computer}")

if player == computer:
    print('itss drawww')
elif beats[player] == computer:
    print('you win!!')
else:
    print('noo you losee!!')