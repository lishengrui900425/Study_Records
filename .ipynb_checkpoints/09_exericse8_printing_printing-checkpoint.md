# Printing, Printing

We will now see how to do a more complicated formatting of a string. This code looks complex, but if you do your comments above each line and break each thing down to its parts, you’ll understand it.

```python
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))
```

## What You Should See

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex8_demo_output.png)

In this exercise I’m using something called a *function* to turn the formatter variable into other strings. When you see me write `formatter.format( . . . )` I’m telling python to do the following:

1. Take the formatter string defined on line 1.
2. Call its format function, which is similar to telling it to do a command line command named format.
3. Pass format four arguments, which match up with the four `{}`s in the formatter variable. This is like passing arguments to the command line command format.
4. The result of calling format on formatter is a new string that has the `{}` replaced with the four variables. This is what print is now printing out.

That’s a lot for the eighth exercise, so what I want you do is consider this a brain teaser [^1] . It’s alright if you don’t *really* understand what’s going on because the rest of the book will slowly make this clear. At this point, try to study this and see what’s going on, then move on to the next exercise.

## Study Drills

Do your checks, write down your mistakes, and try not to make the same mistakes on the next exercise. In other words, repeat the *Study Drills* from Exercise 7.

## Common Student Questions

**Why do I have to put quotes around “one” but not around *True* and *False* ? ** Python recognizes *True* and *False* as keywords representing the concept of true and false. If you put quotes around them then they are turned into strings and won’t work. You’ll learn more about how these work in Exercise 27.

**Can I use IDLE to run this?** No, you should learn to use the command line. It is essential to learning programming and is a good place to start if you want to learn about programming.  IDLE will fail for you when you get further in the book.





[^1]: 脑筋急转弯