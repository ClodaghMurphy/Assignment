## Project title  

Problem Set 2019 Programming and Scripting 
Ten Problems. 
Due: last commit on or before March 31st




## Motivation

This project represents 50% of the marks due for Programming and Scripting Module 10 Credits.
Each problem therefore is worth 5% of the overall mark!

## Code style

The coding is written in Python, which according to DM's i-Tech Special | Coding for Beginners Volume 29 is "the greatest computer programming language ever created".  
Created by Guido van Rossum and first released in 1991, Python is considered to be an accessible language for new programmers (like me) to learn because the syntax (the form of language the program must receive to compute) is simple and consistent.

## Project Number 1 Methodology
Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
I began working on this Problem Set before I was familiar with version control software git.  
It is the first program I have written and relied on somewhat analogue methods while I learned more about coding 
and the online resources that can assist.  
Using a pen and paper, I tried to figure out a maths equation that would give me the sum of all numbers. 
This was to no avail so I started to google then came upon a formula by Gauss, a mathematician in the 18th Century.
n = n * (n + 1) / 2 
I wrote the code which would apply this formula to whatever positive integer was input.
I inserted a while statement intended to reject a number that wasn't a positive integer.
During testing, it became apparent that a request for a positive whole number would print on the screen, however the formula would 
still run on the number that was originally input.
I debugged the code by using the exit() command that simply closes the program if the condition of a positive integer is not met.
A line of text instructs the user to run the program again which ensures the results will be based on a positive integer.

## Project Number 2 Methodology

Write a program that outputs whether or not today is a day that begins with the letter T. 
I began by revisiting and modifying a programming exercise from one of the first classes entitled "Is it Tuesday?"
This uses the import statement in order to gain access to datetime Python code in another module. 
The datetime module allows for manipulation of dates and times.
It is important to bear in mind that counting starts with 0 for Monday.
The two days of the weeking beginning with T are Tuesday which python assigns the value 1 and Thursday equals 3.

I used an if else statement.
"if" the datetime.dateime.today().weekday() result was == either day 1 or 3, the text "Yes - today begins with a T" will appear.
"else" is an optional statement that executes if the conditional expression in the if statement above it supplies a FALSE value.
This sentence prints to the screen "No - today does not begin with a T."

Initially, I put in two lines of if/else statements.
This gave the correct result but in two lines of output.
I needed to figure out how to make the code more concise to produce just one line of output.
I assigned the weekday() value to x in order to make the code more readable.
On W3 Schools page I found a tidy one line if else statement, with 3 conditions.
I modified the statement, ran the program and got the expected answer.


 



##Credits
https://betterexplained.com/articles/techniques-for-adding-the-numbers-1-to-100/
https://www.hashbangcode.com/article/stopping-code-execution-python 

https://docs.python.org/3/reference/
https://docs.python.org/3/library/
https://www.tutorialspoint.com/python/python_if_else.htm
https://www.w3schools.com/python/python_conditions.asp

