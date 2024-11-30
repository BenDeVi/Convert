def convert(sentence):
    sentence=sentence.replace(":)","🙂")
    sentence=sentence.replace(":(","🙁")
    return sentence

def main():
    user_input=input()
    converted_input=convert(user_input)
    print(converted_input)
main()
