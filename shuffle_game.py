from random import shuffle
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def player_guess():
    user_guess=''
    while user_guess not in ['0','1','2']:
        user_guess=input("Please enter any one number 0,1,2")
    return user_guess

def guess_check(user_guess,shuffled_list):
    if shuffled_list[int(user_guess)]=='o':
        return "You have guessed it correctly"
    else:
        return "Wrong guess"
shuffled_list=shuffle_list(['','o',''])
user_guess=player_guess()
print(guess_check(user_guess, shuffled_list))

