import random

def get_random_quote(rquotes = 'russianlitquotes.txt'):

    try: 
        with open(rquotes, 'r') as file:
            quotes = file.readlines()
            if not quotes:
                return "Nyet quotes found in file."
            random_quote =  random.choice(quotes).strip()
            return random_quote
    except FileNotFoundError:
        return f" Error: The file '{rquotes}' was not found."
    
quote = get_random_quote()
print(quote)