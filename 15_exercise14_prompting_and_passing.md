# Prompting and Passing

Let’s do more one exercise that uses `argv` and `input` together to ask the user something specific. You will need this for the next exercise where you learn to read and write files. In this exercise we’ll use input slightly differently by having it print a single `>` prompt. This is similar to games like *Zork* or *Adventure*.

````python
from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me. 
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
````

We make a variable, prompt, that is set to the prompt we want, and we give that to input instead of  typing it over and over. Now if we want to make the prompt something else, we just change it in this one spot and rerun the script. Very handy.

## What You Should See

When you run this, remember that you have to give the script your name for the argv arguments.

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex14_demo_output.png)

## Study Drills

1. Find out what the games *Zork* and *Adventure* were. Try to find copies and play them.
2. Change the prompt variable to something else entirely.
3. Add another argument and use it in your script, the same way you did in the previous exercise with first, second = ARGV.
4. Make sure you understand how I combine a `“"”` style multiline string with the `{}` format activator as the las print.

## Common Student Questions

**I get** SyntaxError: invalid syntax **when I run this script.**  Again, you have to run it right on the command line, not inside Python. If you type `python` and then try to type `python ex14.py Zed` , it will fail because you are running Python *inside* Python

**I don’t understand what you mean by changing the prompt?** See the variable prompt `=`  `‘>` `‘.`. Change that to have a different value. You know this: it’s just a string and you’ve done 13 exercises making them , so take the time to figure it out.

**I get the error** ValueError: need more than 1 value to unpack. Remember when I said you need to look at the *What You Should See* section and replicate what I did?  You need to do the same thing here, and focus on how I type the command in and why I have a command line argument.

**How can I run this from IDLE?** Don’t use IDLE.

**Can I use double-quotes for the** prompt **variable?**  You totally can. Go ahead and try that.

**I get** NameError: name ‘prompt’ is not defined **when I run it.** You either spelled the name of the prompt variable wrong or forgot that line. Go back and compare each line of code to mine, starting at the bottom of the script and working up to the top. Any time you see this error, it means you spelled something wrong or forgot to create the variable.