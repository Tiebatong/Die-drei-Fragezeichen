def main():
    versuche = 5
    for x in range(versuche):
        word = "davor"
        guess = input("input: ").lower()
        if len(guess) == len(word):
            if word == guess:
                print("Gewonnen")
                break
            for i in range(len(word)):
                if guess[i] == word[i]:
                    print(str(guess[i]) + " ist richtig")
                elif guess[i] in word and guess[i] != word[i]:
                    print(str(guess[i]) + " kommt an einer anderen Stelle vor")
                else:
                    print(str(guess[i]) + " kommt nicht vor")
        print("verbleibende Versuche: " + str(4 - x))
main()