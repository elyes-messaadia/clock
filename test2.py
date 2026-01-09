def count_word(phrase):
    count=1
    for lettre in phrase:
        if lettre == " ":
            count+= 1
    print(count)
    print(phrase)

count_word("Salut les gars")