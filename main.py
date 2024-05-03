import random
ACCESTABLE_CHARS = ["a", "b", "c", "d", "e","f","g","h","i","j","k"]
POSSIBLE_GUESS = 3
ROW_LENGTH = 5


def generate_secret_word():
    sec_word = ""
    num_of_chars = len(ACCESTABLE_CHARS) - 1
    for i in range(ROW_LENGTH):
        random_index = random.randint(0, num_of_chars)
        sec_word += ACCESTABLE_CHARS[random_index]
    return sec_word


def initiate():
    global hided_row
    global player_answers
    global game_finished
    global score, loss
    player_answers = []
    game_finished = False
    score = 0
    loss = 0
    
    hided_row = generate_secret_word()
    print("secret word is", hided_row)

def run():
    global game_finished, player_guess
    while not game_finished:
        player_guess = input("enter your guess: ")
        player_answers.append(player_guess)
        if is_player_guess_true(player_guess):
            game_finished = True
            
            check_player_input(player_guess)
            print("You Won!", calculate_player_score(), " SCORE")
            return True
        evaluation_result = check_player_input(player_guess)
        
        print(evaluation_result)
        if len(player_answers) >= POSSIBLE_GUESS:
            game_finished = True
            
            print("You Loss :  ",calculate_player_score(), " SCORE")
        

def is_player_guess_true(player_guess):
    return player_guess == hided_row
    

def check_player_input(player_guess):
    res = ""
    for i in range(len(player_guess)):
        if player_guess[i] == hided_row[i]:
                res += "t"
        elif player_guess[i] in hided_row:
                res += "b"
    if not res:
            res += "f"
            
    return res
                
        
    
    # global score, loss
    # is_scored = False
    
    # for i in range(len(player_guess)):
    #         if player_guess[i] == hided_row[i]:
    #             score += 20
    #             is_scored = True
    #         elif player_guess[i] in hided_row:
    #             score += 10
    #             is_scored = True
                
    # if not is_scored:
    #     print("****************************")
    #     loss += 3 
               
    # return f"{player_guess} is incorrect"
        
        
def calculate_player_score()       :
    # global score, loss
    # score -= loss
    # if score < 0:
    #     score = 0        
    # return score
    res = ""
    score = 0
    counter = 0
    for anwser in player_answers:
        res += check_player_input(anwser)
    for i in res:
        if i == "t":
            score += 20
        elif i == "b":
            score += 10
        elif i == "f":
            counter += 1
        
    score =score - counter * 3   
    if score < 0:
        score = 0     
    return score
            
        
    
    
    
initiate()
run()