## Project title  

Problem Set 2019 Programming and Scripting 
Due: last commit on or before March 31st




## Motivation
This respository contains my answers to Problem Set 2019 Programming and Scripting Assignment, full details are set out in this document:  
https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf 
The project represents 50% of the marks due for Programming and Scripting Module in GMIT Higher Diploma in Data Analysis.


## Code style

The coding is written in Python, which according to DM's i-Tech Special | Coding for Beginners Volume 29 is "the greatest computer programming language ever created".  
Created by Guido van Rossum and first released in 1991, Python is considered to be an accessible language for new programmers (like me) to learn because the syntax (the form of language the program must receive to compute) is simple and consistent.

## Instructions for downloading this repository
Log on to github and search for user ClodaghMurphy, the repository is entitled Assignment PANDS 2019

## Instructions for running the code displayed in each solution



## Project Number 1 Methodology
Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.
I began working on this Problem Set before I was familiar with version control software git.  
It is the first program I have written and relied on analogue methods while I learned more about coding and the online resources that can assist.  
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


## Question 3 Methodology
Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.  
I used the built-in range() function that generates arithmetic progressions. I used an if/and statement for i in the above mentioned range, print all results where i can be divided by 6 with no remainder
and when being divided by 12 leaves a remainder.
In order to test my result I started with a range (1000, 1100) and manually checked every output.  
Once this proved correct I expanded the parameters 




## Question 4 Methodology
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and,if it is even,divide it by two,but if it is odd,multiply it by three and add one. Have the program end if the current value is one.

## Question 5 Methodology

Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime. 

## Question 6 Methodology

Write a program that takes a user input string and outputs every second word

## Question 7 Methodology

Write a program thatthat takes a positive ﬂoating point number as input and outputs an approximation of its square root. 
I used the import statement to import a specific function from the math module.  
According to "The Coder’s Apprentice" by Peter Spronck, it is possible to rename a function that you import from a module, using the
keyword as. This is helpful if using several modules that contain functions with similar names.
I have included this renaming function to make my code easier to read for a beginner.
I used float() type casting to return the value between the parentheses as a floating-point number even if it was not input as one.
I used the format() function to round down the decimals to one, it took a lot of experimenting with syntax in order to get the correct result.
## Question 8 Methodology
Write a program that outputs today’s date and time in the format ”Monday,January 10th 2019 at 1:15pm”. 

## Question 9 Methodology
Write a program that reads in a text ﬁle and outputs every second line. The program should take the ﬁlename from an argument on the command line.

## Question 10 Methodology
Write a program that displays a plot of the functions x, x2 and 2x in the range [0,4].




##References
The references used also appear in the comments of the individual solutions.
"The Coder’s Apprentice" by Peter Spronck
https://betterexplained.com/articles/techniques-for-adding-the-numbers-1-to-100/
https://www.hashbangcode.com/article/stopping-code-execution-python 

https://docs.python.org/3/reference/
https://docs.python.org/3/library/
https://www.tutorialspoint.com/python/python_if_else.htm
https://www.w3schools.com/python/python_conditions.asp
