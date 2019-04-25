# More Printing

[TOC]

Now we are going to do a bunch of exercises where you just type code in and make it run. I won’t be explaining this exercise because it is more of the same. The purpose is to build  up your chops.[^1] See you in a few exercises, and do not skip! Do not paste!

````python
print('Mary had a little lamb.')
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # What'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#wath end = ' ' at the end. try removing it to see what happens
print(end1 + end2 +end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
````

## What You Should See

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex7_demo_output.png)

## Study Drills

For these next few exercises, you will have the exact same Study Drills.

1. Go back through and write a comment on what each line does.
2. Read each one backward or out loud to find your errors.
3. From now on, when you make mistakes, write down on a piece of paper what kind of mistake you made.
4. When you go to the next exercise, look at the mistakes you have made and try not to make them in this new one.
5. Remember that everyone makes mistakes. Programmers are like magicians who fool everyone into thinking they are perfect and never wrong, but it’s all an act. They make mistakes all the time.

## Break It

Did you have fun breaking the code in Exercise 6? From now on you’re going to break all the code you write or a friend’s code. I won’t have a *Break It* section explicitly [^2] in every exercise, but I will do this in almost every video. Your goal is to find as many different ways to break your code until you get tired or exhaust all possibilities. In some exercises I might point out a specific common way people break that exercise’s code, but otherwise consider this is a standing order to always break it.

## Common Student Questions

**Why are you using the variable named `snow`?** That’s actually not a variable: It is just a string with the word snow in it. A variable wouldn’t have the single-quotes around it.

**Is it normal to write an English comment for every line of code like you say to do in Study Drill 1? ** No, you write comments only to explain difficult-to-understand code or why you did something. Why is usually much more important , and then you try to write the code so that it explains how something is being done on its own. However, sometimes you have to write such nasty code to solve a problem that it does need a comment on every line. In this case it’s strictly for you to practice translating code to English.

**Can I use single-quotes or double-quotes to make a string or do they do different things?** In Python either way to make a string is acceptable, although typically you’ll use single-quotes for any short strings like ‘a’ or ‘snow’.

[^1]: 建立你的能力
[^2]: 明确地；明白地