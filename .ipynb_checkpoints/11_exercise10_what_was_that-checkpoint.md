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
```



[^1]: 保持警惕
[^2]: 转义

