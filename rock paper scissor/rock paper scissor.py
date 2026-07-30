import random

computer = random.choice(['rock', 'paper', 'scissor'])
player = input("Pick rock, paper or scissor : ").strip().lower()

print(f"Computer use {computer}")