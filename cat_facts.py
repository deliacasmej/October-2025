import requests

# cat facts

def get_kitty():
    cat_url = "https://catfact.ninja/fact"
    try:
        response = requests.get(cat_url)
        response.raise_for_status()
        data =  response.json()
        fact = data.get("fact")
        return print(f"Did you know: {fact}")
    except requests.exceptions.RequestException as e:
        print(f"Sorry! Error: {e}")
        return None
    
get_kitty()