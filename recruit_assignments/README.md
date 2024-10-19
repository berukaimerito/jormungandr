# RUNNING THE PROGRAM

* For Unix-based systems, execute the code with
```bash
 ./program message.txt magazine.txt
 ```
* For Windows systems, you can run the corresponding .bat executable using Command Prompt or PowerShell:

 ```bash
 program message.txt magazine.txt
 ```

* The code expects the input files to be passed in the following format:
    * program message.txt magazine.txt
    * Both test files should be in .txt 
    * Both files should be in the same directory as main.py and executable files.

## Trade-offs.

* I choose Python as my first to-go and I went on explicit on dictionary lookup:
    * I wanted to show I am mildly aware of under-the-hood operations.
    * If I encapsulated everything and went explicit, I thought I would be giving away from my general comprehension of the given task.
    * The solution could be very encapsulated and functional as well. Although I thought the input limit would be handled fine by such solutions, I coded for one extreme scenario.
    * Python does not use built-in arrays, so it kind of lifts the real concern of performance-critical runtime.
    * Thus, I considered providing an array-based solution in another language, believing this would showcase my ability to code in different languages and paradigms, and switch between them easily.


## Handling Edge Cases, Pathological Cases, and Assumptions on Input Data

* Given the context of the problem (using a magazine as a source), I assumed the average input size would be around 5000 words. Any solution should comfortably handle such input sizes.
* However, I aimed for a more generic solution, capable of handling potential edge cases or malformed inputs. Assuming all input data is always clean and ordered could indicate a lack of consideration for extreme or pathological cases.
* By thinking through these scenarios—without overcomplicating the code—I tried to strike a balance between practicality and robustness, ensuring the code remains efficient while also handling unexpected inputs. 
* Ransom messages can include digits. It include include currency signs as well. Alhthough I thought not finding a single symbol shouldn't stop constructing the message This is especially true when the symbols themselves don't add significant meaning or are easily ignorable in the context of ransom messages.
* I have just added one replacement case 'Zero for `o`' for demonstration of scenario.


### Solutions in order:

1. solution_python : First implementation
2. solution_pythonic Second implementation in Python.
3. solution_