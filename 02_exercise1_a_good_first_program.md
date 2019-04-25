# Exercise 1 A Good First Program

You should have spent a good amount of time in Exercise 0 learning how to install a text editor, run the text editor, run the Terminal, and work with both of them. If you haven’t done that, then do not go on. You will not have a good time. 

Type the following text into a single file named ex1.py. Python works best with files ending in . py.

```python
print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print("Yay! Printing.")
print("I'd much rather you 'not'.")
print('I "said" do not touch this')
```

Your Visual Studio Code text editor should look something like this on all platforms:

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex1.png)

Don’t worry if your editor doesn’t look exactly the same; it should be close though. You may have a slightly different window header, maybe slightly different colors.All of those differences are fine.

When you create this file, keep in mind these points:

1. I did not type the line numbers on the left. Those are printed in the book so I can talk about specific lines by saying, “See line 5 …”You do not type line numbers into Python scripts.
2. I have the print at the beginning of the line, and it looks exactly the same as what I have in ex1.py. Exactly means exactly, not kind of sort of the same. Every single character has to match for it to work. Color doesn’t matter, only the characters you type.

On Windows, remember you always type `python` instead of `python 3.7` like this:

​	`python ex1.py`

If you did it right then you should see the same output as I in the What You Should See section of this exercise. If not, you have done something wrong. No , the computer is not wrong.

## What You Should See

On Windows in PowerShell you should see this:

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\exercise1_what_you_should_see.png)

You may see different names before the python ex1.py command , but the important part is that you type the command and see the output is the same as mine.

If you have an error it will look like this:

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\exercise1_error.png)

It’s important that you can read these error messages because you will be making many of these mistakes. Even I make many of these mistakes. Let’s look at this line by line.

1. We ran our command in the Terminal to run the ex1.py script.
2. Python tells us that the file ex1.py has an error on line 3 of ex1.py.
3. It prints this line of code for us to see it.
4. Then it puts a ^(caret)   character to point at where the problem is . Notice the missing “(double-quote) character?
5. Finally, it prints out a “SyntaxError” and tells us something about what might be the error. Usually these are very cryptic, but if you copy that text into a search engine, you will find someone else who’s had that error, and you can probably figure out how to fix it.

## Study Drills

**The Study Drills contain things you should try to do. If you can’t, skip it and come back later.**

For this exercise, try these things:

1. Make your script print another line.
2. Make your script print only one of the lines
3. Put a #(octothorpe) character at the beginning of a line. What did it do? Try to find out what this character does. 

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\exercise1_study_drills.png)

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\exercise1_study_drills_output.png)

From now on, I won’t explain how each exercise works unless an exercise is different.

## Common Student Questions 

There are actual questions that real students have asked when doing this exercise.

**Can I use IDLE?** No, you should see PowerShell on Windows, just like I have here. If you don’t know how to use PowerShell, then you can go read the appendix. 

**How do you get colors in your editor?** Save your file first as a .py file, such as ex1.py. Then you’ll have color when you type.

**I get** SyntaxError: invalid syntax **when I run** ex1.py. You are probably trying to run Python, then trying to type Python again. Close your Terminal, start it again, and right away type only python 3.7 ex1.py.

**I get** can’t open file ‘ex1.py’: [Errno 2] No such file or directory. You need to be in the same directory as the file you created. Make sure you use the `cd` command to go there first. For example, if you saved your file in D:\MyNoteBook\Learn-Python3-The-Hard-Way/ex1.py, then you would do `cd` D:\MyNoteBook\Learn-Python3-The-Hard-Way/ before trying to run python 3.7 ex1.py. If you don’t know what any of that means, then go through the appendix.

**My file doesn’t run; I just get the prompt back with no output.**  You most likely took the code in my ex1.py file literally and thought that print(“Hello World!”) meant to type only “Hello World!” into the file, without the print. You files has to be exactly like mine.

