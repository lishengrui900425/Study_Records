# More Files

Now let's do a few more things with files. We'll write a Python script to copy one file to another. It'll be very short but will give you ideas about other things you can do with files.

````python
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file,'rb')
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist?{exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file,'w')
out_file.write(str(indata))

print("Alright,all done.")

out_file.close()
in_file.close()
````

You should immediately notice that we import another handy command named exists. This returns True if a file exists, based on its name in a string as an argument. It returns False if not.We'll be using this function in the second half of this book to do lots of things, but right now you should see how you can import it.

Using import is a way to get tons of free code other better(well,usually) programmers have written so you do not have to write it.

## What You Should See

Just like your other scripts, run this one with two arguments: the file to copy from and the file to copy it to. I'm going to use a simple test file named test.txt:
