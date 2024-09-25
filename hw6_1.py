# .1 כתוב תוכנית בפייטון הקולטת שמות של 4 שחקנים המשתתפים בהגרלה str,
# עליך להגריל מתוך 4 השחקנים שחקן זוכה אחד באופן אקראי
# הגרל מי השחקן שניצח והדפס את שמו. רמז: choice.random

import random
player1_name: str = input("player1, your name:")
player2_name: str = input("player2, your name:")
player3_name: str = input("player3, your name:")
player4_name: str = input("player4, your name:")

winner: str = random.choice([player1_name, player2_name, player3_name, player4_name])
print(f"the winner is: {winner}")
