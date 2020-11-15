import getpass

print("Please enter the secret word or phrase. Nothing will appear, which will keep it secret.")
secret_phrase = getpass.getpass()
secret_phrase = secret_phrase.lower()
secret_list = list(secret_phrase)

chances = 5

for i in range(len(secret_list)):
    if secret_list[i] != ' ':
        secret_list[i] = '_'

while '_' in secret_list and chances > 0:
    print(''.join(secret_list))
    print("You have", chances, "left")
    guess = input("Guess a letter: ").lower()

    if guess in secret_phrase:
        for i in range(len(secret_phrase)):
            if secret_phrase[i] == guess:
                secret_list[i] = guess
    else:
        chances -= 1

if chances > 0:
    print("Congratulations! You won!")
else:
    print("Game over.\nYou've run out of tries. The secret phrase was", secret_phrase)
