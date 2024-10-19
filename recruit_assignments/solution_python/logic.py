# it cannot be a set. it has to match the count of a letter in the message
# can decide with if key: count exists case insensitive. if it is, we can prepare our ransom message.
# how to do it fast?? lots of string operations here. 
# i can assume the bound as an average letter in a magazine. quick google research told me around 5000 words. 


'''
        This function constructs a frequency dictionary from the magazine and checks if the message can be constructed.
        Only alphabetic characters and digits are considered, ignoring punctuation and spaces.
 '''

def core_logic_func(message, magazine):
    
    '''
        turn magazine into dictionary aka frequency_dict
        if a letter in the magazine can be used meaning that it is not a punctuation or a space:
            if isalphanumeric(): // but message can include digits as well
                char.tolower()  (encapsulate it. used twice)
        if dict_mag[char_at_message] is equls to kmag -> valmag we can assume the ransom message can be constructed.
        This could be done with importing Counter from collections. Thus, I decided to give it another refactored solution after this.
        Another approach to avoid hash collisions (performance critical)
        arr = []
        idx 0  = a
        idx -> alphabet_position
        val -> char

    '''

    frequency_dict = {}
    def dict_lookup_load(c):
        frequency_dict[c] = frequency_dict.get(c, 0) + 1
   
    for char in magazine:
        # This might seem unprofessional or unnecessary however for a ransom message prepared by a noir fan, 0 can be used as o easily. i.e. Give me the m0ney
        # Just reflecting the scenario.
        if char == '0':   
            dict_lookup_load('o')
        #ransom messages can use digits. such as: lend me $100000 until december 28th. yes i thought about money symbols as well but for small change the message could fail.
        elif char.isalpha() or char.isdigit():  
            dict_lookup_load(char.lower()) 

    
    for char in message:
        char = char.lower() 
        if not char.isalpha() and not char.isdigit():
            continue  # Skip this iteration for symbols
        # Handle the case where '0' can be treated as 'o'
        if char == '0':
            if frequency_dict.get('o', 0) == 0:
                return False
            frequency_dict['o'] -= 1
        else:
            if frequency_dict.get(char, 0) == 0:
                return False
            frequency_dict[char] -= 1

    # if code does not return any bool value until here meaning that the iteration for message is completed and message can be constructed
    return True






