# Strings and Text

While you have been writing strings, you will do not know what they do.In this exercise we create a bunch of variables with complex strings so you can see what they are for. First an explanation of strings.

A string is usually a bit of text you want to display to someone or “export” out of the program you are writing . Python knows you want something to be a string when you put either “ (double-quotes) or ‘ (single-quotes) around the text. You saw this many times with your use of print when you put the text you want to go inside the string inside `“` or `‘` after the print to print the string.

Strings can contain any number of variables that are  in your Python script. Remember that a variable is any line of code where you set a name = (equal) to a value. In the code for this exercise,`type_of_people = 10` creates a variable named types_of_people and sets it = (equal) to 10. You can put that in any string with {types_of_people}. You also see that I have to use a special type of string to “format”; it’s called an “f-string” and looks like this:

````python
f"some stuff here {avariable}"
f"some other stuff {anothervar}"
````

Python *also* has another kind of formatting using the . format() syntax, which you see on line 17. You’ll see me use that sometimes when I want to apply a format to an already-created string, such as in a loop. We’ll cover that more later.

We will now type in a whole bunch of strings, variables, and formats, and print them. We will also practice using short, abbreviated variable names. Programmers love saving time at your expense by using annoyingly short and cryptic names, so let’s get you started reading and writing them early on.

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex6_demo.png)

## What You Should See

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex6_demo_output.png)

## Study Drills

1. Go through this program and write a comment above each line explaining it.
2. Find all the places where a string is put inside a string. There are four places.
3. Are you sure there are only four places? How do you know? Maybe I like lying.
4. Explain why adding the two string `w` and `e` with `+` makes a longer string.

## Break it 

You are now at a point where you can try to break your code to see what happens. Think of this as a game to devise the most clever way to break the code. You can also find the simplest way to break it. Once you break the code, you then need to fix it. If you have a friend, then two of you can try to break each other’s code and fix it. Give your friend your ex6.py file so they can break something. Then you try to find their error and fix it. Have fun with this, and remember that if you wrote this code once you can do it again. If you take your damage too far, you can always type it in again for extra practice.