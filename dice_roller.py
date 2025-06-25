import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    print("🎲 Dice Roller Simulator")
    try:
        sides = int(input("Enter the number of sides on the die (default is 6): ") or 6)
        if sides < 2:
            print("A die must have at least 2 sides.")
            return

        while True:
            input("Press Enter to roll the die...")
            result = roll_dice(sides)
            print(f"🎯 You rolled a {result}!\n")
            again = input("Roll again? (y/n): ").strip().lower()
            if again != 'y':
                print("Goodbye!")
                break
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
