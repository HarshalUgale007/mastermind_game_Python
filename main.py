import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

def guess_code():
    while True:
        guess = input("Guess : ").upper().split(" ")
        
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
            
        valid_guess = True
        for color in guess:
            if color not in COLORS:
                print(f"{color} is not a valid color.")
                valid_guess = False
                break
        
        if valid_guess:
            break
            
    return guess

def check_code(guess, real_code):
    correct_pos = sum(g == r for g, r in zip(guess, real_code))
    
    guess_color_count = {color: guess.count(color) for color in COLORS}
    real_color_count = {color: real_code.count(color) for color in COLORS}
    
    incorrect_pos = sum(min(guess_color_count[color], real_color_count[color]) for color in COLORS) - correct_pos
    
    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to the Mastermind game! You have {TRIES} tries to guess the code.")
    print(f"The valid colors are", *COLORS)
    
    code = generate_code()
    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            print(f"You guess the code in {attempt} tries!")
            break
        
        print(f"Correct position: {correct_pos} | Incorrect position: {incorrect_pos}")
        
    else:
        print("You ran out of tries. The code was", *code)

if __name__ == "__main__":
    game()
