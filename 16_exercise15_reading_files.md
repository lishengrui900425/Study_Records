# Reading Files

You know how to get input from a user with input or argv. Now you will learn about reading from a file.You may have to play with this exercise the most to understand what’s going on,so do the exercise carefully and remember your checks.  Working with files is an easy way to *erase* your work if you are not careful.

This exercise involves writing two files. One is the usual ex15.py file that you will run, but the other is named ex15_sample.txt.  This second file isn’t a script but a plain text file we’ll be reading in our script.Here are the contents of that file:

```markdown
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
```

What we want to do is *open* that file in our script and print it out.  However, we do not want to just *hard code* the name ex15_sample.txt into our script. “Hard coding” means putting some bit of information that should come from the user as a string directly in our source code.That’s bad because we want it to load other files later.  **The solution is to use argv or input to ask the user what file to open instead of hard coding the file’s name.**

````python
from sys import argv

script, filename = argv  

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
````

A few fancy things are going on in this file, so let’s break it down real quickly:

+ Lines 1–3 use argv to get a filename. Next we have line 5, where we use a new command,open. Right now, run pydoc open and read the instructions. Notice how, like your own scripts and input, it takes a parameter and returns a value you can set to your own variable.
+ Line 7 prints a little message, but on line 8 we have something very new and exciting.We call a function on txt named read. What you get back from open is a file, and it also has commands you can give it. You give a file a command by using the . (dot or period), the name of the command, and parameters, just like with open and input. The difference is that
  txt.read() says, “Hey txt! Do your read command with no parameters!”

The remainder of the file is more of the same, but we’ll leave the analysis to you in the Study Drills.

## What You Should See

I made a file called ex15_sample.txt and ran my script.

![](https://raw.githubusercontent.com/learn_python_the_hard_way/master/images/ex15_demo_output.png?raw=true)

## Study Drills

This is a big jump, so be sure you do this Study Drill as best you can before moving on.

1. Above each line, comment out in English what that line does.
2. If you are not sure, ask someone for help or search online.Many times searching for “python3.7 THING” will find answers to what that THING does in Python.Try searching for “python3.7 open.”
3. I used the word “commands” here, but commands are also called “functions” and “methods.”You will learn about functions and methods later in the book.
4. Get rid of lines 10–15 where you use input and run the script again.
5. Use only input and try the script that way.Why is one way of getting the filename better than another?
6. Start python3.7 to start the python3.7 shell, and use open from the prompt just like in this program.
7. Have your script also call close() on the txt and txt_again variables. It’s important to close files when you are done with them.

## Common Student Questions

**Does** `txt = open(filename)` **return the contents of the file?** No, it doesn’t. It actually makes something called a **file object**. You can think of a file like an old tape drive that you saw on mainframe computers in the 1950s or even like a DVD player from today. You can move around inside them and then “read” them, but the DVD player is not the DVD the same way the file object is not the file’s contents.

**I can’t type code into Terminal/PowerShell like you say in Study Drill 7. **First, from the command line just type python and press Enter.Now you are in python3.6 as we’ve done a few other times.Then you can type in code and Python will run it in little pieces. Play with that.To get out of it type quit() and hit Enter.

**Why is there no error when we open the file twice?**Python will not restrict you from opening a file more than once, and sometimes this is necessary.

**What does** `from sys import argv` **mean?** For now just understand that sys is a package, and this phrase just says to get the argv feature from that package. You’ll learn more about these later.

**I put the name of the file in as** `script, ex15_sample.txt = argv`, **but it doesn’t work. **No, that’s not how you do it.Make the code exactly like mine, then run it from the command line the exact same way I do.  You don’t put the names of files in, you let Python put the name in.

# Reading and Writing Files

If you did the Study Drills from the last exercise, you should have seen all sorts of commands (methods/functions) you can give to files. Here’s the list of commands I want you to remember:

+ close: Closes the file. Like File->Save... in your editor.
+ read: Reads the contents of the file. You can assign the result to a variable.
+ readline: Reads just one line of a text file.
+ truncate: Empties the file. Watch out if you care about the file.
+ write('stuff'): Writes “stuff” to the file.
+ seek(0): Moves the read/write location to the beginning of the file.

One way to remember what each of these does is to think of a vinyl record, cassette tape, VHS tape, DVD, or CD player. In the early days of computers, data was stored on each of these kinds of media,so many of the file operations still resemble a storage system that is linear.Tape and DVD drives need to “seek” a specific spot, and then you can read or write at that spot.Today we have operating systems and storage media that blur the lines between random access memory and disk drives, but we still use the older idea of a linear tape with a read/write head that must be moved.

For now, these are the important commands you need to know.. Some of them take parameters, but we do not really care about that. You only need to remember that write takes a parameter of a string you want to write to the file.

Let’s use some of this to make a simple little text editor:

`````python
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
`````

That’s a large file, probably the largest you have typed in.So go slow, do your checks, and make it run.One trick is to get bits of it running at a time.Get lines 1–8 running, then five more, then a few more, until it’s all done and running.

## What You Should See

There are actually two things you will see. First, the output of your new script:

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex16_demo_output.png)

Now, open up the file you made (in my case, test.txt) in your editor and check it out. Neat, right?

## Study Drills

1. If you do not understand this,go back through and use the comment trick to get it squared away in your mind.One simple English comment above each line will help you understand or at least let you know what you need to research more.
2. Write a script similar to the last exercise that uses read and argv to read the file you just created.
3. 
