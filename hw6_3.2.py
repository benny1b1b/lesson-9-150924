
max_stars: int = int(input("base of the pyramid:"))
stars: int = 1
# stars += 2
spaces: int = max_stars // 2

for stars in range(1, max_stars + 2, 2):
    for _ in range(1, spaces + 1):
        print(" ", end="")
    for _ in range(1, stars + 1):
        print("*", end="")
    print()
    spaces -= 1


