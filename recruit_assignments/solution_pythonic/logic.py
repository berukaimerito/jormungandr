from collections import Counter

'''
 This function encapsulates some steps and it uses list-comprehensions. It is still performant. Counter is an optimized.
'''

def core_logic_func(message, magazine):
    letters_magazine = [char.lower() if char.isalpha() else 'o' if char == '0' else None for char in magazine]
    cleaned_letters_mag = filter(None, letters_magazine)
    frequency_dict = Counter(cleaned_letters_mag)
    
    for char in message:
        char = char.lower()
        if char.isalnum():  # Check if the character is alphanumeric (letters or digits) # replace the need for checking isdigit and isalpha separately.
            if char == '0':
                char = 'o'  # Treat '0' as 'o' when checking the message
            if frequency_dict.get(char, 0) == 0:
                return False
            frequency_dict[char] -= 1
    
    return True