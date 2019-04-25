# Numbers and Math

Every programming language has some kind of way doing numbers and math. Do not worry: programmers frequently lie about being math geniuses when they really aren’t. If they were math geniuses, they would be doing math, not writing buggy web frameworks so they can drive race cars.

This exercise has lots of math symbols. Let’s name them right away so you know what they are called. As you type this on in, say the name. When saying them feels boring you can stop saying them. Here are the names:

| Symbols | Name |
| ------- | ---- |
|   `+`      |  plus    |
|`-`|minus|
|`/`|slash|
|`*`|asterisk|
|`%`|percent|
|`<`|less-than|
|`>`|greater-than|
|`<=`|less-than-equal|
|`>=`|greater-than-equal|

Notice how the operations are missing? After you type in the code for this exercise, go back and figure out what each of these does and complete the table. For example, `+` does addition.

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\Numbers_and_Math.png)

Make sure you type this exactly before you run it. Compare each line of your file to my file.

## What You Should See

![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\Exercise3_Session.png)

## Study Drills

1. Above each line, use the `#` to write a comment to yourself explaining what the line does.

2. Remember in Exercise 0 when you started python 3. 7 ? Start python 3.7 this way again and, using the math operators, Use Python as a calculator.

3. Find something you need to calculate and write a new. py file that does it.

4. Rewrite ex3 .py to use floating point numbers so it’s more accurate. 20.0 is floating point.

   ![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\exercise3_study_drills.png)

   ![](D:\MyNoteBook\Learn-Python3-The-Hard-Way\images\exercise3_study_drills_output.png)

## Common Student Questions
**Why is the `%` character a "modulus" and not  a "percent"?**  Mostly that's just how the designers chose to use that symbol. In normal writing you are correct to read it as a "percent". In programming this calculation is typically done with simple division and the `/` operator. The `%` modulus is a different operation that just happens to use the `%` symbol.

**How does `%` work?** Another way to say it is , “X divided by Y with J remaining.”  For example, “100 divide by 16 with 4 remaining. ” The result of `%` is the J part, or the remaining part.

**What is the order of operations?** In the United States we use an acronym called PEMDAS which stands for Parentheses Exponents Multiplication Division Addition Subtraction. That’s the order Python follows as well. The mistake people make the PEMDAS is to think this is a strict order, as in “Do P, then E, then M, then D, then A, then S.” The actual order is you do the multiplication and  division(M&D) in one step, from left to right, then you do the addition and subtraction in one step from left to right. So, you could rewrite PEMDAS as PE(M&D)(A&S).

