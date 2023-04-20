import json5
from PIL import Image


def decrypt_location(json_file_path, english_txt_file_path):
    # Read the JSON file and load its contents as a Python dictionary
    with open(json_file_path, 'r') as f:
        data = json5.load(f)
    
    # Extract the encrypted location data for your project team
    encrypted_location = data['Shabazz Napier']
    
    # Read the English.txt file and split its contents into a list of words and symbols
    with open(english_txt_file_path, 'r') as f:
        english_words = f.read().splitlines()
    
    # Create a dictionary that maps each index to its corresponding word or symbol
    word_dict = {}
    for i, word in enumerate(english_words):
        word_dict[i] = word
        
    # Decrypt the location data using the word dictionary
    decrypted_location = []
    for index in encrypted_location:
        # Convert the index to an integer and subtract 1 to account for non-zero indexing
        index = int(index) - 1
        
        # Get the word or symbol corresponding to the index
        word = word_dict.get(index, '')
        
        # Append the word or symbol to the decrypted location list
        decrypted_location.append(word)
    
    # Join the decrypted location list with spaces in between
    decrypted_location = ' '.join(decrypted_location)
    
    return decrypted_location


def display_image(filepath):
    try:
        with Image.open(filepath) as img:
            rotated_img = img.rotate(-90, expand=True)
            rotated_img.show()
    except FileNotFoundError:
        print(f"Error: file {filepath} not found.")