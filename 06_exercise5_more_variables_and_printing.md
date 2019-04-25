# More Variables and Printing 

Now we’ll do even more typing of variables and printing them out. This time we’ll use something called a **format string**. Every time you put `“` (double-quotes) around a piece of text you have been making a string.  A string is how you make something that your program might have to a human. You print strings, save strings to files, send strings to files, send strings to web servers, among many other things.

Strings are really handy, so in this exercise you will learn how to make strings that have variables embedded in them. You embed variables inside a string by using a special `{}` sequence and then put the variable you want inside the `{}` characters. You also must start the string with the letter `f` for “format”, as in **`f “Hello {somevar}”`**. This little `f` before the `“`(double-quote) and the `{}` characters tell Python 3, “Hey, this string needs to be formatted. Put these variables in there.”

As usual, just type this in even if you do not understand it , and make it exactly the same.

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex5_demo.png)

## What You Should See

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex5_demo_output.png)

## Study Drills

1. Change all the variables so there is no `my_` in front of each one. Make sure you change the name everywhere, not just where you used `=` to set them.
2. Try to write some variables that convert the centimeters and kilograms to inches and pounds. Do not just type in the measurements. Work out the math in Python.

## Common Student Questions

**Can I make a variable like this: `1 = ‘lishengrui’?`** No, `1` is not a valid variable name. They need to start with a character, so `a1` would work, but `1` will not.

**How can I round a floating point number?**  You can use the `round()` function like this: `round(1.7333)` .

**Why does this not make sense to me?**  Try making the numbers in this script your measurements. It’s weired, but talking about yourself will make it seem more real. Also, you’re just starting out so it won’t make too  much sense. Keep going and more exercise will explain it more.