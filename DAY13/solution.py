def upper_case(sentence):
    for i in sentence:
        if i in sentence.upper():
            print(i, end='')

upper_case("ASSU is not an NGO")
