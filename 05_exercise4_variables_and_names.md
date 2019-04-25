# Variables and Names

Now you can print things with `print` and you can do math. The next step is to learn about variables. In programming, a variable is nothing more than a name for something, similar to how my name, “lishengrui”, is a name for “the human who wrote this book”. Programmers use these variable names to make their code read more like English and because they have lousy memories. If they didn’t use good names for things in their software, they’d get lost when they tried to read their code again.

In you get stuck with this exercise, remember the tricks you have been taught so far of finding differences and focusing on details:

1. Write a comment above each line explaining to yourself in English what it does.
2. Read your .py file backward.
3. Read your .py file out loud, saying even the characters.

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex4_demo.png)

## What You Should See

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex4_demo_output.png)

## Study Drills

When I wrote this program the first time I had a mistake, and Python told me about it like like:

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\exercise4_study_drills_output.png)

Explain this error in your own words. Make sure you use line numbers and explain why.

Here are more study drills:

1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4?
2. Remember that 4.0 is a *floating point* number. It’s just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating number. 
3. Write comments above each of the variable assignments.
4. Make sure you know what `=` is called (equals) and that its purpose is to give data (numbers, strings, etc.) names (cars_driven, passengers).
5. Remember that `_` is an underscore character.
6. Try running python from the terminal as a calculator like you did before, and use variable names to do your calculations, Popular variable names include i, x, and j.

## Common Student Questions

**What is the difference between `=` (single-equal) and `==` (double-equal)?**  The `=` (single-equal) assigns the value on the right to a variable on the left. The `==` (double-equal) tests whether two things have the same value. You’ll learn about this in Exercise 27.

**Can we write `x=100` instead of `x = 100` ?**  You can, but it’s bad form. You should add space around operators like this so that it’s easier to read.

**What do you mean by “read the file backward” ?** Very simple. Imagine you have a file with 16 lines of code in it. Start at line 16, and compare it to my file at line 16. Then do it again for 15, and so on until you’ve read the whole file backward.

**Why did you use 4.0 for `space_in_a_car`?**  It’s mostly so you can then find out what a floating point number is and ask this question. See the Study Drills.