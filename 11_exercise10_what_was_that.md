# What Was That?

In Exercise 9 I threw you some new stuff, just to keep you on your toes [^1]. I showed you two ways to make a string that goes across multiple lines. In the first way, I put the characters `\n`  (backslash n) between the names of the months. These two characters put a *new line* character into the string at that point. 

This `\` (backslash) character encodes difficult-to-type characters into a string. There are various escape [^2] sequences available for different characters you might want to use. We’ll try a few of these sequences so you can see what I mean.

An important escape sequence is to escape a single-quote( ` ) or double-quote(“).  Imagine you have a string that use double-quotes and you want to put a double-quote inside the string.  If you write “I “understand” joe.”  then Python will get confused because it will think the double-quotes around “understand” actually ends the string. You need a way to tell Python that the double-quote inside the string isn’t a *real* double-quote.

To solve this problem you escape double-quotes and single-quotes so Python knows to include them in the string. Here’s an example:

````python
"I am 6 '2\" tall."  # escape double-quote inside string
'I am 6\'2" tall.'   # escape single-quote inside string 
````

The second way is by using triple-quotes, which is just ``"""`` and works like a string, but you also can put as many lines of text as you want until you type ``"""`` again. We’ll also play with these.

```python
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food 
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
```

##  What You Should See

Look for the tab characters that you made. In this exercise the spacing is important to get right.

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\ex10_demo_output.png)

## Escape Sequences

This is all of the escape sequences Python supports. You may not use many of these, but memorize their format and what they do anyway.  Try them out in some strings to see if you can make them work.

| Escape     | What it does                                               |
| ---------- | ---------------------------------------------------------- |
| \\         | Backslash(\)                                               |
| \'         | Single-quote (')                                           |
| \"         | Double-quote(")                                            |
| \a         | ASCII bell (BEL)                                           |
| \b         | ASCII backspace[^3] (BS)                                   |
| \f         | ASCII formfeed [^4] (FF)                                   |
| \n         | ASCII linefeed  [^5] (LF)                                  |
| \N{name}   | Character named name in the Unicode database(Unicode only) |
| \r         | Carriage return [^6] (CR)                                  |
| \t         | Horizontal tab [^7] (TAB)                                  |
| \uxxxx     | Character [^8] with 16-bit hex [^9] value xxxx             |
| \Uxxxxxxxx | Character with 32-bit hex value xxxxxxxx                   |
| \v         | ASCII vertical tab [^10] (VT)                              |
| \000       | Character with octal [^11] value 000                       |
| \xhh       | Character with hex value hh                                |

## Study Drills

1. Memorize all the escape sequences by putting them on flash cards.
2. Use ``'''`` (triple-single-quote) instead. Can you see why you might use that instead of `"""`?
3. Combine escape sequences and format strings to create a more complex format.

## Common Student Questions

**I still haven’t completely figured out the last exercise. Should I continue?**  Yes, keep going. Instead of stopping, take notes listing things you don’t understand for each exercise. Periodically [^12] go through your notes and see if you can figure these things out after you’ve completed more exercises. Sometimes, though, you may need to go back a few exercises and do them again.

**What makes \\\ special compared to the other ones?**  It’s simply the way you would write out one backslash (\\) character. 

**When I write // or /n it doesn’t work.** That’s because you are using a forward-slash(/) and not a backslash(\\). They are different characters that do very different things.

**I don’t get Study Drill 3. What do you mean by “combine” escape sequences and formats?** One concept I need you to understand is that each of these exercises can be combined to solve problems. Take what you know about format strings and write some new code that uses format strings and the escape sequences from this exercise.

**What’s better, ``'''`` or `"""`?** It’s entirely based on style. Go with the ``'''``(triple-single-quote) style for now, but be ready to use either depending on what feels best or what everyone else is doing.

[^1]: 保持警惕
[^2]: 转义
[^3]: 退格符
[^4]: 换页符
[^5]: 换行符(newline)
[^6]: 回车符
[^7]: 水平制表符
[^8]: 字符
[^9]: 十六进制的
[^10]: 垂直制表符
[^11]: 八进制的
[^12]: 定期地