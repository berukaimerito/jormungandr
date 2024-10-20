#include <iostream> 
#include <fstream>
#include <sstream>
#include <string>
#include <array>
#include <cctype> // for isalnum()


int find_index(char ch) {
    if(std::isalpha(ch)) {
        return std::tolower(ch) - 'a'; // converts to lowercase and find the index -> 'a' has an ascii value of 97.
    } else if (std::isdigit(ch)) {
        return (ch - '0') + 26; // substract the ascii value of zero and and the index of starting point
    }
    return -1;
}

bool core_logic_func(const std::string& msg, const std::string& mag) 
{
    /*
        Create a constant array with a size 26. 
        For each alphanum char inside mag, increase the value at the index ord(char) - ord(97) ascii value
        Iterate the message, if you find any 0 at alphabet-based index return 0. If not decrement the value at index.
        return true if iteration does not fail.
        
    */

   // create fixed size array 
   std::array<int, 36> frequency_arr = {0};

    //build the frequncy using magazine
    for(char ch : mag) {
        if (std::isalnum(ch)) {
            int index = find_index(ch);
            if(index != -1) {
                frequency_arr[index]++;
            }
        }
    }


    //check  if message can be constructed
    // i used almann braces here to show logic explicitly 
    for(char ch : msg) {
        if(std::isalnum(ch)) {
            int index = find_index(ch);
            if (index != -1) {
                if (frequency_arr[index] == 0) 
                {
                    return false;
                }
                frequency_arr[index]--;
            }
        }
    }

    return true;

}


int main(int argc, char* argv[]) {
    /*
        1. Program should check cli arguments
         2. Put file content into logic function
        3. Receive the boolean value.
    */

    if(argc != 3) {
        std::cerr << " Usage:  message.txt magazine.txt " << std::endl;
        return 1;
    }

    std::string message_file = argv[1];
    std::string magazine_fle = argv[2];

    std::ifstream message_stream(message_file);
    if(!message_stream) {
        std::cerr << "Could not load the file." << std::endl;
        return 1;
    }

    std::stringstream message_buffer;
    message_buffer <<  message_stream.rdbuf();
    std::string message = message_buffer.str();

    std::ifstream magazine_stream(magazine_fle);
    if(!magazine_stream) {
        std::cerr << "Could not load the magazine file." << std::endl;
        return 1;
    }
    
    std::stringstream magazine_buffer;
    magazine_buffer << magazine_stream.rdbuf();
    std::string magazine = magazine_buffer.str();

    /*
    std::cout << "Message file content: " << message << std::endl;
    std::cout << "Magazine fle content: " << magazine << std::endl;
    */
    bool result = core_logic_func(message, magazine);

    std::cout << "Can the ransom message be constructed? --> " << std::boolalpha << result  << std::endl;
    
    return 0;
}

