# Prompting People

When you typed `input()` you were typing the ( and ) characters, which are *parenthesis* characters. This is similar to when you used them to do a format with extra variables, as in `f"{x} {y}"`. For input you also put in a prompt [^1] to show to a  person so he knows what to type. Put a string that you want for the prompt inside the `() ` so that it looks like this:

```python
y = input("Name? ")
```

This prompts the user with “Name?” and puts the result into the variable `y`. This is how you ask someone a question and get the answer.  

This means we can completely rewrite our previous exercise using just input to do all the prompting.

````python
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
````

## What You Should See

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex12_demo_output.png)

## Study Drills

1. In Terminal, where you normally run python 3.7 to run your scripts, type  `python -m pydoc input`. Read what it says.
2. Get out of pydoc by typing `q` quit.
3. Look online for what the pydoc command does.
4. Use pydoc to also read about open, file, os, and sys. It’s alright if you do not understand those; just read through and take notes about interesting things.

## Common Student Questions

**How come I get** SyntaxError :  invalid syntax **whenever I run** pydoc? You aren’t running pydoc from the command line; you’re probably running it from inside python 3.7. Exit out of python 3.7.

**Why does my** pydoc **not pause like yours does?**  Sometimes if the help document is short enough to fit on one screen then pydoc will just print it. 

**When I run** pydoc **I get** more is not recognized as an internal. Some versions of Windows do not have that command, which means pydoc is broken for you. You can skip this Study Drill and just search online for Python documentation when you need it. 

**Why can’t I do** `print("How old are you?", input()?)` You can, but then the result of calling `input()` is never saved to a variable, and it’ll work in a strange way. Try this, and then try to print out what you type. See if you can debug why this isn’t working.

[^1]: 提示

