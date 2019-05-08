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

```python
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
```

That’s a large file, probably the largest you have typed in.So go slow, do your checks, and make it run.One trick is to get bits of it running at a time.Get lines 1–8 running, then five more, then a few more, until it’s all done and running.

## What You Should See

There are actually two things you will see. First, the output of your new script:

![](D:/MyNoteBook/Learn-Python3-The-Hard-Way/images/ex16_demo_output.png)

Now, open up the file you made (in my case, test.txt) in your editor and check it out. Neat, right?

## Study Drills

1. If you do not understand this,go back through and use the comment trick to get it squared away in your mind.One simple English comment above each line will help you understand or at least let you know what you need to research more.
2. Write a script similar to the last exercise that uses read and argv to read the file you just created.
3. There’s too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.
4. Find out why we had to pass a 'w' as an extra parameter to open.Hint: open tries to be safe by making you explicitly say you want to write a file.
5. If you open the file with 'w' mode, then do you really need the target.truncate()?Read the documentation for Python’s open function and see if that’s true.

## Common Student Questions

**Is the** truncate() **necessary with the** 'w' **parameter?**  See Study Drills number 5.

**What does** 'w' **mean? ** It’s really just a string with a character in it for the kind of mode for the file.If you use 'w' then you’re saying “open this file in ‘write’ mode,” thus the 'w' character. There’s also 'r' for “read,” 'a' for “append,” and modifiers on these.

**What modifiers to the file modes can I use? **The most important one to know for now is the `+` modifier, so you can do 'w+', 'r+', and 'a+'.This will open the file in both read and write mode and, depending on the character use, position the file in different ways.

**Does just doing** open(filename) **open it in** 'r' **(read) mode**? Yes, that’s the default for the open() function.