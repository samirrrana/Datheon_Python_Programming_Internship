import random
import os

# ANSI Colors for a vibrant terminal experience
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

# ASCII Gallows Art for 6 stages of mistakes
GALLOWS_STAGES = [
    f"""
       {YELLOW}+---+{RESET}
       {YELLOW}|   |{RESET}
           {YELLOW}|{RESET}
           {YELLOW}|{RESET}
           {YELLOW}|{RESET}
           {YELLOW}|{RESET}
     {YELLOW}========={RESET}
    """,
    f"""
       {YELLOW}+---+{RESET}
       {YELLOW}|   |{RESET}
       {RED}O{RESET}   {YELLOW}|{RESET}
           {YELLOW}|{RESET}
           {YELLOW}|{RESET}
           {YELLOW}|{RESET}
     {YELLOW}========={RESET}
    """,
    f"""
       {YELLOW}+---+{RESET}
       {YELLOW}|   |{RESET}
       {RED}O{RESET}   {YELLOW}|{RESET}
       {RED}|{RESET}   {YELLOW}|{RESET}
           {YELLOW}|{RESET}
           {YELLOW}|{RESET}
     {YELLOW}========={RESET}
    """,
    f"""
       {YELLOW}+---+{RESET}
       {YELLOW}|   |{RESET}
       {RED}O{RESET}   {YELLOW}|{RESET}
      {RED}/|{RESET}   {YELLOW}|{RESET}
           {YELLOW}|{RESET}
           {YELLOW}|{RESET}
     {YELLOW}========={RESET}
    """,
    f"""
       {YELLOW}+---+{RESET}
       {YELLOW}|   |{RESET}
       {RED}O{RESET}   {YELLOW}|{RESET}
      {RED}/|\\{RESET}  {YELLOW}|{RESET}
           {YELLOW}|{RESET}
           {YELLOW}|{RESET}
     {YELLOW}========={RESET}
    """,
    f"""
       {YELLOW}+---+{RESET}
       {YELLOW}|   |{RESET}
       {RED}O{RESET}   {YELLOW}|{RESET}
      {RED}/|\\{RESET}  {YELLOW}|{RESET}
      {RED}/{RESET}     {YELLOW}|{RESET}
           {YELLOW}|{RESET}
     {YELLOW}========={RESET}
    """,
    f"""
       {YELLOW}+---+{RESET}
       {YELLOW}|   |{RESET}
       {RED}O{RESET}   {YELLOW}|{RESET}
      {RED}/|\\{RESET}  {YELLOW}|{RESET}
      {RED}/ \\{RESET}  {YELLOW}|{RESET}
           {YELLOW}|{RESET}
     {YELLOW}========={RESET}
    """
]

def load_words_from_file(filename="words.txt"):
    try:
        with open(filename, "r") as file:
            words = [line.strip().upper() for line in file.readlines() if line.strip()]
            
        if not words:
            raise ValueError("File is empty!")
        return words
    except FileNotFoundError:
        print(f"{RED}⚠️  Error: '{filename}' not found!{RESET}")
        print(f"{YELLOW}Using default word list...{RESET}")
        return ["PYTHON", "DATHEON", "DEVELOPER", "INTERFACE", "TERMINAL"]
    except Exception as e:
        print(f"{RED}⚠️  Error reading file: {e}{RESET}")
        return ["PYTHON", "DATHEON", "DEVELOPER", "INTERFACE", "TERMINAL"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    
    # Load words from text file (Change "words.txt" if your filename is different)
    word_list = load_words_from_file("words.txt")
    
    print(f"{CYAN}==================================={RESET}")
    print(f"{CYAN}    WELCOME TO COLORFUL HANGMAN     {RESET}")
    print(f"{CYAN}==================================={RESET}")
    
    secret_word = random.choice(word_list).upper()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = 6

    while mistakes < max_mistakes:
        print(GALLOWS_STAGES[mistakes])
        
        displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print(f"Word to guess: {GREEN}{displayed_word}{RESET}\n")
        
        if guessed_letters:
            print(f"Guessed letters: {MAGENTA}{', '.join(sorted(guessed_letters))}{RESET}")
        else:
            print(f"Guessed letters: {MAGENTA}None{RESET}")
            
        print(f"Remaining attempts: {BLUE}{max_mistakes - mistakes}{RESET}\n")

        if all(letter in guessed_letters for letter in secret_word):
            clear_screen()
            print(f"{GREEN}==================================={RESET}")
            print(f"{GREEN}       🎉 VICTORY! YOU WIN! 🎉       {RESET}")
            print(f"{GREEN}==================================={RESET}")
            print(f"\nThe word was: {CYAN}{secret_word}{RESET}\n")
            return

        guess = input("Enter a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            clear_screen()
            print(f"{YELLOW}⚠️  Please enter a single valid letter!{RESET}")
            continue

        if guess in guessed_letters:
            clear_screen()
            print(f"{YELLOW}⚠️  You already guessed '{guess}'. No penalty deduction!{RESET}")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            clear_screen()
            print(f"{GREEN}✅ Good job! '{guess}' is in the word.{RESET}")
        else:
            clear_screen()
            mistakes += 1
            print(f"{RED}❌ Wrong guess! '{guess}' is not in the word.{RESET}")

    print(GALLOWS_STAGES[mistakes])
    print(f"{RED}==================================={RESET}")
    print(f"{RED}        💀 GAME OVER! 💀           {RESET}")
    print(f"{RED}==================================={RESET}")
    print(f"\nYou ran out of attempts. The secret word was: {CYAN}{secret_word}{RESET}\n")

if __name__ == "__main__":
    main()
