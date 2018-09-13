
import pickle

def add_word(language_translate,words): #Asks the user to add new words not in the dictionary to the dictionary
    print("add a word to the dictionary: ")
    add_translation = input("translation of " + words + " into spanish is:")
    language_translate[words]=add_translation
    #translatedtext = repr(language_file.language_translate)
    #utf = translatedtext.encode('utf-8')
    with open('language_file.pkl','wb') as pickle_out: #rewrites the current dictionary with the updated dictionary

       pickle.dump(language_translate,pickle_out)
       print(language_translate)
    return add_translation   

def translate(): #uses the current dictionary to translate words
    with open('language_file.pkl','rb') as pickle_in:
       language_translate = pickle.load(pickle_in)
       
    print("Translate text into Spanish: ")
    english_input=input("Enter text here: ")

    sentence_output = ""


    for words in english_input.split():
        if words in language_translate:
                sentence_output += language_translate[words] + " "
        else:
            print("cannot find", words)
            define=input("Do you know the defintion? (y/n) ").lower()
            if (define == 'y'):
                sentence_output += add_word(language_translate,words) + " "
            elif (define == 'n'):
                break
                   
    print(sentence_output)


if __name__ == "__main__":  #Starts the program, asks if user wants to continue or closes
   while True:
    translate()
    restart = input('Translate something else?(y/n): \n').lower()
    if restart == ('n'):
        exit()
    elif restart == ('y'):
        continue

