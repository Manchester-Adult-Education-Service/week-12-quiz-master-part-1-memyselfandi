# -------------------------------------------
# Exercise 1: The Ultimate Quiz Master
# -------------------------------------------
# In this exercise, we are going to build an interactive quiz program step-by-step.
# We will start by hardcoding simple questions, then move to Lists/Dictionaries,
# and finally upgrade the program to load quiz data from an external **JSON file**.
#
# Key Concepts:
# - Variable Initialisation
# - Arithmetic & Comparison Operators
# - User Input (input(), int())
# - String Methods (.upper(), .lower())
# - Conditionals (if, elif, else)
# - Loops (for, while)
# - Lists and Dictionaries
# - File Handling (open, load)
#
# IMPORTANT:
# You will need to create a 'quiz.json' file for Task 6!
# -------------------------------------------
# GROUP INSTRUCTIONS
# -------------------------------------------
# Work in groups of 2–3. Share the same GitHub repository.
# Roles:
# - One learner acts as the **DRIVER** (types the code and runs commands).
# - The other learners are **NAVIGATORS** (observe, guide, and provide suggestions).
#
# After each task:
# - Current learner: git add, commit, and push
# - Next learner: git pull origin main
# -------------------------------------------

# Leave this alone!!
import json # This will be used in Task 6 and Extension 3

# -------------------------------------------
# Task 1: Setting up the Game and Score
# -------------------------------------------
# We need to set up the basic variables for the game.
#
# TODO:
# 1. Initialise a variable called 'player_score' and set it to 0.
# 2. Initialise a variable called 'max_score' and set it to 10 (as in 10 potential questions).
# 3. Print a welcome message: "Welcome to The Ultimate Python Quiz!"
# 4. Print the current 'player_score' using an f-string: "Your current score is 0."
#
# Write your code below:




# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your code. You should see the welcome message and the score print correctly.
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit with an appropriate message.
# 3. Push to the repository.
# The next learner must pull the latest version before continuing.
# -------------------------------------------


# -------------------------------------------
# Task 2: The First Simple Question (Arithmetic)
# -------------------------------------------
# Let's ask the first question and handle the input using basic math and conditionals.
#
# TODO:
# 1. Print the heading "--- Testing Basic Functions ---"
# 2. Ask the user the question: "Q1: What is 7 * 5?" and save their answer as 'answer1' (make sure it's an integer).
# 3. Use an **IF/ELSE** statement to check if 'answer1' is equal to 35.
# 4. If correct, print "Correct!" and increase 'player_score' by 1.
# 5. If incorrect, print "Incorrect. The answer was 35."
#
# HINT: You will need to use the **'int()'** function to convert the input from text to a number.
#
# Write your code below:




# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your code. Test with a correct answer (35) and an incorrect one.
# Check if 'player_score' updates correctly.
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit with an appropriate message.
# 3. Push to the repository.
# The next learner must pull the latest version before continuing.
# -------------------------------------------


# -------------------------------------------
# Task 3: A String-Based Question (String Methods)
# -------------------------------------------
# Now let's ask a text-based question and use string methods for flexible checking.
#
# TODO:
# 1. Ask the user the question: "Q2: Which conditional keyword means 'otherwise, if'?" and save their answer as 'answer2'.
# 2. Convert 'answer2' to **lowercase** using the **.lower()** method.
# 3. Use an **IF/ELSE** statement to check if the **lowercase** answer is equal to "elif".
# 4. If correct, print "You got it!" and increase 'player_score' by 1.
# 5. If incorrect, print "Not quite. It was ELIF."
# 6. Print the closing "--- End of Basic Test ---\n"
#
# Write your code below:




# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your code. Test with 'elif' and 'else'. Ensure only the correct answers (regardless of case) score a point.
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage.
# 2. Commit.
# 3. Push.
# The next learner must pull before continuing.
# -------------------------------------------


# -------------------------------------------
# Task 4: Storing Questions in a List of Dictionaries (Data Structure Practice)
# -------------------------------------------
# Typing out an IF/ELSE block for every question is repetitive. We need a better structure.
#
# ACTION REQUIRED:
# Comment out the old code from Task 2 and Task 3. We are replacing it with a better data structure!
#
# TODO:
# 1. Create a variable called **'quiz_questions'**.
# 2. Assign it a **list** containing at least **three** **dictionaries**.
# 3. Each dictionary must represent a question and have the following keys:
#    - **'question'**: The question text (string)
#    - **'answer'**: The correct answer (string or number)
#    - **'type'**: 'int' or 'str' (to indicate if the answer is a number or text)
#
# Example of a list containing quiz question dictionary:
# quiz_questions = [
#   {
#   'question': 'What is the capital of France?',
#   'answer': 'PARIS',
#   'type': 'str'
#   },
#   {
#     Second quiz question dictionary here
#   }
# ]
#
# Write your code below:




# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your code. Nothing should break. Print 'quiz_questions' to verify it looks correct.
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage.
# 2. Commit.
# 3. Push.
# The next learner must pull before continuing.
# -------------------------------------------


# -------------------------------------------
# Task 5: Looping Through the Questions (FOR Loop)
# -------------------------------------------
# We will create a function to handle the quiz logic, making it reusable.
#
# TODO:
# 1. Define a function called **`run_quiz`** that takes one argument, `questions`.
# 2. Inside the function:
#    a. Reset **`player_score`** to 0 and set **`max_score`** to the length of the `questions` list.
#    b. Create a **FOR loop** to iterate through each question dictionary `q` in the `questions` list.
#    c. Inside the loop, get the user's input. Check **`q['type']`** and convert the input accordingly (`int()` or `.upper()`).
#    d. Update the **`player_score`** and print the result.
# 3. **After** the loop, calculate and display the final score and percentage, including the "Excellent job!" conditional check (from Task 4 in the hint section).
# 4. **Comment out** the line that calls the function for now, as we will use it in Task 7.
#
# Write your code below:




# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Test your logic by uncommenting and calling `run_quiz(quiz_questions)` once. Does it work?
# Remember to comment it out again before proceeding.
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage.
# 2. Commit.
# 3. Push.
# The next learner must pull before continuing.
# -------------------------------------------


# -------------------------------------------
# Task 6: Migrating to JSON (External File Loading)
# -------------------------------------------
# We are moving the data outside the Python file. This is how real-world programs work!
#
# ACTION REQUIRED:
# 1. Create a new file named **'quiz.json'** in the SAME folder.
# 2. **Copy the entire 'quiz_questions' list** you made in Task 4 and paste it into **'quiz.json'**.
# 3. At the very top of your Python file, ensure you have: `import json`
# 4. **DELETE** the hardcoded 'quiz_questions' list you defined in Task 4.
# 5. Replace it with the code below to load the data instead:
#
# HINT for Loading JSON:
# with open('quiz.json', 'r') as file:
#     quiz_questions = json.load(file)
#
# TODO:
# 1. Implement the HINT code above to load the external data into the **'quiz_questions'** variable.
# 2. Add basic error handling (try/except) for `FileNotFoundError`.
#
# (Modify the code below)
# Write your code below:




# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your code. Did it load the data from 'quiz.json' and run the quiz correctly?
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage.
# 2. Commit.
# 3. Push.
# The next learner must pull before continuing.
# -------------------------------------------


# -------------------------------------------
# Task 7: Handling Multiple Attempts (WHILE loop)
# -------------------------------------------
# Now that our quiz loads data correctly, let's wrap the whole thing in a loop so the user can play again easily.
#
# ACTION REQUIRED:
# Surround the entire quiz logic (Tasks 6 and 5) with a WHILE loop.
#
# TODO:
# 1. Initialise a variable 'take_quiz' to 'Y' (uppercase) before the main loop.
# 2. Create a **WHILE loop** that runs as long as 'take_quiz' is equal to 'Y'.
# 3. Implement a simple menu that asks the user to type 'play' or 'exit'.
# 4. If the user chooses 'play', call `run_quiz(quiz_questions)`.
# 5. If the user chooses 'exit', use a `break` to stop the loop.
# 6. Add a farewell message after the while loop.
#
# (Modify the code below)
# Write your code below:




# -------------------------------------------
# CHECKPOINT
# -------------------------------------------
# Run your code. Does the quiz start? When you finish, can you choose to play again?
# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage.
# 2. Commit.
# 3. Push.
# The next learner must pull before continuing.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# If you have completed the tasks above, try these extensions to
# really test your skills!
# -------------------------------------------

# Extension 1: Question Numbering
# -------------------------------------------
# The questions currently don't say "Q1", "Q2", etc.
#
# ACTION REQUIRED:
# Modify the FOR loop in Task 5.
#
# TODO:
# 1. Change your FOR loop to use the **'enumerate'** function.
# 2. This gives you both the index (starting at 0) and the item.
# 3. When printing the question, add the number (index + 1) at the start.
#
# (Modify the code in Task 5 - Do not write new code here)
# -------------------------------------------


# Extension 2: Input Validation (WHILE loop & Try/Except)
# -------------------------------------------
# Right now, if the user enters text for a question that expects an integer, the program will crash.
#
# ACTION REQUIRED:
# Modify the code inside the FOR loop in Task 5.
#
# TODO:
# 1. Inside the loop, create a new **WHILE loop** that only runs if the 'type' is 'int'.
# 2. Inside the WHILE loop, use a **try/except** block to attempt converting the input to an integer.
# 3. If the conversion succeeds, 'break' the WHILE loop.
# 4. If a 'ValueError' occurs, print an error message (e.g., "Error: Please enter a whole number.") and let the WHILE loop repeat the input prompt.
#
# (Modify the code in Task 5 - Do not write new code here)
# -------------------------------------------


# Extension 3: Saving Data (Writing JSON)
# -------------------------------------------
# This is advanced! Let's allow users to add a new question and **SAVE** it to the external file.
#
# ACTION REQUIRED:
# Create a new menu option for the user *inside* the main WHILE loop from Task 7.
#
# TODO:
# 1. Change the Task 7 menu: Add a new option, like asking for input: "Type 'play' or 'add' to choose an action: "
# 2. Create an **IF/ELIF** block to handle the user's action.
# 3. If the action is 'add' (Add New Question):
#    a. Get inputs for the new question: text, correct answer, and type ('int' or 'str').
#    b. Create a new dictionary with these values.
#    c. Append this new dictionary to the **'quiz_questions'** list.
#    d. **KEY STEP:** Write the updated list back to the JSON file:
#
#    with open('quiz.json', 'w') as file:
#        json.dump(quiz_questions, file, indent=4)
#
# (Modify the code in Task 7 - Do not write new code here)
# -------------------------------------------


# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Use Git to:
# 1. Stage your final changes.
# 2. Commit with an appropriate message (e.g. "Completed extension activity").
# 3. Push your final version and the 'quiz.json' file to the repository.
# -------------------------------------------
