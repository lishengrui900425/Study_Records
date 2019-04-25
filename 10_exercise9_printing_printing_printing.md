# Printing, Printing, Printing

By now you should realize the  pattern for this book is to use more than one exercise to teach you something new. I start with code that you might not understand, then more exercised explain the concept. If you don’t understand something now, you will later as you complete more exercises. Write down what you don’t understand, and keep going.

```python
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Thr Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:", days)
print("Here are the months:", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
```

## What You Should See

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex9_demo_output.png)

## Study Drills 

Check your work, write down your mistakes, try not to make them on the next exercise. Are you breaking your code and then fixing it? In other words, repeat the Study Drills From Exercise 7. 

## Common Student Questions

**What do I get an error when I put spaces between the three double-quotes?** You have to type them like """ and not " " ", meaning with *no* space between each one.

**What if I want to start the months on a new line?** You simply start the string with `\n`, like this:

``