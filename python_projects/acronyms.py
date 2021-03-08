#accept a string
input = str(input('Enter a Phrase: '))

#split the string
input_str = input.split()

#create a variable to store the acronyms
acronyms = ''

#for loop to get the acronyms
for i in input_str:
    acronyms += str(i[0]).upper()
print(acronyms)    
