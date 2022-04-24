def reverse_word(word):
    index = -1
    for i in range(len(word)-1, int(len(word)/2), -1):
        if word[i].isalpha():
            sen_t = word[i]
            while True:
                index += 1
                if word[index].isalpha():
                    word[i] = word[index]
                    word[index] = sen_t
                    break
    print("".join(word))


reverse_word(list("lade, what is your name?"))
