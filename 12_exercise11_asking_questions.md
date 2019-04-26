# Asking Questions

 Now it is time to pick up the pace [^1]. You are doing a lot of printing to get you familiar with typing simple things, but those simple things are fairly boring. What we want to do now is get data into your programs. This is a little tricky because you have to learn to do two things that may not make sense right away, but trust me and do it anyway. It will make sense in a few exercises.

Most of what software does is the following:

1.  Takes some kind of input from a person. 
2. Changes it. 
3. Prints out something to show how it changed.

So far you have been printing strings, but you haven’t been able to get any input from a person. You may not even know what “input” means, but type this code in anyway and make it exactly the same. In the next exercise we’ll do more to explain input.

```python
print("How old are you?", end= ' ')
age = input()
print("How tall are you?", end= ' ')
height = input()
print("How much do you weigh?", end= ' ')
weight = input()

print(f"So, you're {age} old, {heigh} tall and {weight} heavy.")
# WARNING! We put an end=' ' at the end of each print line. This tells print to not end the line with a newline character and go to the next line.
```

## What You Should See

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex11_demo_output.png)

## Study Drills

1. Go online and find out what Python’s input does.
2. Can you find other ways to use it? Try some of the samples you find.
3. Write another “form” like this to ask some other questions.

