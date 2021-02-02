# Write your code here
def create_dict():
    '''Create a function that opens the flowers.txt, reads every        
        line in it, and saves it as a dictionary
    '''
    with open('flowers.txt') as f:
        flower_dict = {}
        for line in f:
            letter = line.split(':')[0].lower()
            flower_dict[letter] = line.split(':')[1].strip()
    return flower_dict
        
        
def match_flowers():
    '''A function that takes user input (user's first name and last name) 
    and parse the user input to identify the first letter of the first name. It should then use it to print
    the flower name with the same first letter (from dictionary created in the first function)
    '''
    name= input('Enter your First [space] Last name only: ')
    
    first_letter = name.lower()[0]
    
    flower_dict = readflowers()
    flower = flower_dict[first_letter]
    
    print(("Unique flower name with the first letter: {}".format(flower))


match_flowers()



