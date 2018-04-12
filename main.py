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
    truthTable = [[False for x in range(numberOfClaims)] for y in range(rowsInTable)]

    for row in range(rowsInTable):
        for col in range(numberOfClaims):
            # the entire continent of africa's collective AIDS condensed into one line
            truthTable[row][col] = (row-((rowsInTable/(2**col))*(int(row/(rowsInTable/(2**col)))))) < (2**(numberOfClaims-(col+1)))

    printTruthTable(truthTable)

def printTruthTable(truthTable):
    for row in range(len(truthTable)):
        for col in range(len(truthTable[0])):
            print(truthTable[row][col],end='')
        print('\n')

def

def main():
    truthTableGenerator()

#Call main function to run when file is run from CLI
if __name__ == "__main__":
    main()
