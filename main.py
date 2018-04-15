
import os
import platform

#Used to clear the console screen properly


def truthTableGenerator():
    #Prompt user for the number of claims to use; repeat prompt until valid input
    while True:
        try:
            numberOfClaims = int(input("Number of claims in truth table:")) #Input number of claims as an integer
            break
        except ValueError:
            print("Please input a number in integer format.")

    #In truth tables, r=2^n where r is number of rows and n is number of claims
    rowsInTable = 2 ** numberOfClaims
    #Initialize the truth table with 0 for all values
    truthTable = [[False for x in range(numberOfClaims)] for y in range(rowsInTable)] #the fuck is this syntax, python

    for row in range(rowsInTable):
        for col in range(numberOfClaims):
            # the entire continent of africa's collective AIDS concentrated into one line
            truthTable[row][col] = (row-((rowsInTable/(2**col))*(int(row/(rowsInTable/(2**col)))))) < (2**(numberOfClaims-(col+1)))

    printTruthTable(truthTable)

def printTruthTable(truthTable):
    for row in range(len(truthTable)):
        for col in range(len(truthTable[0])):
            print(truthTable[row][col],end='')
        print('\n')


'''

#How Classes Work 101

#Defining Object of a Class
Object = Class()

# Called vs Interpreted by Python
Object.Method(arg1, arg2) --> Class.Method(Object, arg1, arg2)

How Logic Claims Work 101

Where X is the Subject; Y is the predicate
Where X and Y are plural grouped nouns

A Claim: All X are Y
E Claim: No X are Y
I Claim: Some X are Y
O Claim: Some X are not Y

'''

def clearScreen():
    environment = platform.system()
    if environment == "Darwin" or environment == "Linux":
        os.system("clear")
    elif environment == "Windows":
        os.system("cls")
    elif environment == "Java":
        print("This was supposed to be the part of the program that cleared your console screen but... like... what the hell are you doing? Apparently you're running this shit in Java? Anyway, I don't know how that's possible so in lieu of clearing your screen, here--have some newline characters!\n\n\n\n\n")
    else:
        print("Okay what the hell are you even running this on, a damn NES? Here, have some newlines instead of clearing your screen, if the thing you're using even has a screen... \n\n\n\n\n")



def interface():
    while 1:
        clearScreen()
        print("Please enter a logically valid phrase.\n")
        phrase = input("\n> ")
        phraseObject = Claim(phrase)
        #clearScreen()

        while 1:

            print("What would you like to do?\n")
            print("1.) Complement a new term.")
            print("2.) Contrapose the phrase.")
            print("3.) Invert the subject/predicate")
            print("4.) Obvert the phrase.")
            print("5.) Identify the type of phrase.")
            print("6.) Print the phrase.")
            print("\n7.)Exit.")

            response = input("\n> ")


            if response == "1":
                clearScreen()
                print("Enter the term to be negated.")
                term = input("\n> ")

                print("Negating phrase...")
                new_term = phraseObject.complement(term)
                print("The negated term is now: " + new_term)
                print("\nWould you like to do another conversion with your current phrase? yes/no")
                continue_conversion = input("\n> ")
                if continue_conversion == 'no':
                    break

            if response == "2":
                clearScreen()
                print("Contraposing phrase...")
                phraseObject.contrapose()
                new_phrase = phraseObject.printPhrase()

                print("The modified phrase is now: " + new_phrase)
                print("\nWould you like to do another conversion with your current phrase? yes/no")
                continue_conversion = input("\n> ")
                if continue_conversion == 'no':
                    break

            if response == "3":

                clearScreen()
                print("Swapping subject/predicate of phrase...")
                phraseObject.convert()
                new_phrase = phraseObject.printPhrase()

                print("The modified phrase is now: " + new_phrase)
                print("\nWould you like to do another conversion with your current phrase? yes/no")
                continue_conversion = input("\n> ")
                if continue_conversion == 'no':
                    break

            if response == "4":
                clearScreen()
                print("Obverting the phrase...")
                phraseObject.obvert()
                new_phrase = phraseObject.printPhrase()

                print("The modified phrase is now: " + new_phrase)
                print("\nWould you like to do another conversion with your current phrase? yes/no")
                continue_conversion = input("\n> ")
                if continue_conversion == 'no':
                    break
            '''
            # this one needs to return the self.type of the phrase somehow
            if response == "5":

                clearScreen()
                print("Identifying the phrase...")
                phraseObject.identify()
                type = phraseObject.printPhrase()

                print("The modified phrase is now: " + new_phrase)
                print("\nWould you like to do another conversion with your current phrase? yes/no")
                continue_conversion = input("\n> ")
                if continue_conversion == 'no'
                    break
            '''
            if response == "5":
                error(50)

            if response == "6":
                clearScreen()
                phrase_current = phraseObject.printPhrase()

                print("The current phrase is: " + phrase_current)
                print("\nWould you like to do another conversion with your current phrase? yes/no")
                continue_conversion = input("\n> ")
                if continue_conversion == 'no':
                    break

            if response == "7":
                break

            #clearScreen()

# defines and modifies phrase attributes
class Claim:
    text = ''       #the claim in string form
    type = ''       #stores a char value A,E,I,O
    is_true = True  #boolean is claim true/false
    subject = ''    #subject term in claim
    predicate = ''  #predicate term in claim



    def printPhrase(self):
        lordeJesus = {'A': ['All', 'are'], 'N': ['No', 'are'], 'I': ['Some', 'are'], 'O': ['Some', 'are not']} #It is 3:45AM, this is what you get when naming variables
        new_phrase = str(lordeJesus[self.type][0]) + " " + " ".join(str(x) for x in self.subject) + " " + str(lordeJesus[self.type][1]) + " " + " ".join(str(y) for y in self.predicate) + "."
        return(new_phrase)

    def complement(self,term):
        new_term = "non-" + str(term)
        return new_term

    def contrapose(self):
        #Swap subjects and predicates with the compliments of each other
        self.subject, self.predicate = self.complement(self.predicate), self.complement(self.subject)

    def convert(self):
        #swap subject and predicate
        self.subject, self.predicate = self.predicate, self.subject

    def obvert(self):

        #replace predicate term with its complimentary term
        self.predicate = self.complement(self.predicate)

        #Convert claim type: move horizontally across the Square of Oppositions
        if self.type == 'A':
            self.type == 'E'

        elif self.type == 'E':
            self.type == 'A'

        elif self.type == 'I':
            self.type == 'O'

        elif self.type == 'O':
            self.type == 'I'

        else:
            error(100)

    def identify(self):
        '''
        Analyzes the text in a claim to determine the claim type

        '''
        phrase_words = self.text
        # sets type
        if phrase_words[0] == "All":
            self.type = 'A'
        elif phrase_words[0] == "No":
            self.type = 'E'
        elif phrase_words[0] == "Some":
            for word in phrase_words:
                if word == "are":
                    if phrase_words[word+1] == "not":
                        self.type = 'O'
                    else:
                        self.type = 'I'

    def __init__(self, phrase):

        self.text = phrase

        # splits into list of words
        phrase_words = phrase.split(" ")

        # sets subject and predicate
        for word in phrase_words:
            if word == "are":
                # ommits the first word, using some jenk-ass python syntaxing to find the wörd-th word
                self.subject = phrase_words[1:phrase_words.index(word)]
                self.predicate = phrase_words[phrase_words.index(word):]

        # sets type
        if phrase_words[0] == "All":
            self.type = 'A'
        elif phrase_words[0] == "No":
            self.type = 'E'
        elif phrase_words[0] == "Some":
            for word in phrase_words:
                if word == "are":
                    if phrase_words[(phrase_words.index(word)+1)] == "not":
                        self.type = 'O'
                    else:
                        self.type = 'I'
        else:
            error(101)
            return
        print(" _____   _  ___ ___ ___ ___ ___ ")
        print("|_  / | | |/ __/ __| __/ __/ __|")
        print(" / /| |_| | (_| (__| _|\__ \__ \\")
        print("/___|\___/ \___\___|___|___/___/")

def error(errorNumber):
    #errorDict = {911: 'Bush did it, fuck if I know', 666: 'yes', 420: '#blazeit'} -- @roostaa
    errorDict = {50: "Feature is not yet implemented.", 100: "Invalid claim type detected during obversion", 101: "Invalid claim type detected during initialization"}
    print(errorDict[int(errorNumber)])

def main():
    #truthTableGenerator()
    interface()

#Call main function to run when file is run from CLI
if __name__ == "__main__":
    main()
