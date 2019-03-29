## Project title  

Problem Set 2019 Programming and Scripting<br>
Due: last commit on or before March 31st.




## Motivation
This respository contains my answers to Problem Set 2019 Programming and Scripting Assignment, full details are set out in this document:  
https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf <br>
The project represents 50% of the marks due for Programming and Scripting Module in GMIT Higher Diploma in Data Analysis.


## Code style

The coding is written in Python, which according to DM's i-Tech Special | Coding for Beginners Volume 29 is
>"the greatest computer programming language ever created".  
>
<br>
Created by Guido van Rossum and first released in 1991, Python is considered to be an accessible language for new programmers (like me) to learn because the syntax (the form of language the program must receive to compute) is simple and consistent.

## Instructions for downloading this repository
Log on to [GitHub](http://github.com) and search for user ClodaghMurphy, the repository is entitled Assignment.


## Project Number 1 Methodology
_Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number._<br>
I began working on this Problem Set before I was familiar with version control software git.  
It is the first program I have written and relied on analogue methods while I learned more about coding and the online resources that can assist.  
Using a pen and paper, I tried to figure out a maths equation that would give me the sum of all numbers. 
This was to no avail so I started to google then came upon a formula n = n * (n + 1) / 2 by Gauss (an 18th Century mathematician) on the website
[Betterexplained.com](https://betterexplained.com/articles/techniques-for-adding-the-numbers-1-to-100/)
<br>
I wrote the code which would apply this formula to whatever positive integer was input.<br>
I inserted a while statement intended to reject a number that wasn't a positive integer.<br>
During testing, it became apparent that a request for a positive whole number would print on the screen, however the formula would
still run on the number that was originally input.<br>I debugged the code by using the exit() command that simply closes the program if the condition of a positive integer is not met.<br>A line of text instructs the user to run the program again which ensures the results will be based on a positive integer.<br>
When I tested the program the result was always displayed with as a floating number (that is one with a decimal point)<br>
In order to give a result of an integer without a radix point I have used .format () command which will return a new formatted version of the string for which it is called.  To interpret an integer as a ﬂoat, place an "f" to the right side of the colon.<br>
Indicate zero decimals using .0, which will display ﬂoats as integers<br>
print ("The sum of all numbers between one and your number is {:.0f}".format(x))<br>
Use of .format method adapted from examples in Chapter 5 Simple Functions<br>
"The Coder’s Apprentice" by Peter Spronck<br>



## Project Number 2 Methodology

_Write a program that outputs whether or not today is a day that begins with the letter T._ <br>
I began by revisiting and modifying a programming exercise from one of the first classes entitled "Is it Tuesday?"<br>
This uses the import statement in order to gain access to datetime Python code in another module. <br>
The datetime module allows for manipulation of dates and times.<br>
It is important to bear in mind that counting starts with 0 for Monday.<br>
The two days of the weeking beginning with T are Tuesday which python assigns the value 1 and Thursday equals 3.<br>

I used an if else statement.<br>
"if" the datetime.datetime.today().weekday() result was == either day 1 or 3, the text "Yes - today begins with a T" will appear.
"else" is an optional statement that executes if the conditional expression in the if statement above it supplies a FALSE value.<br>
This sentence prints to the screen "No - today does not begin with a T."<br>

Initially, I put in two lines of if/else statements.<br>
This gave the correct result but in two lines of output.<br>
I needed to figure out how to make the code more concise to produce just one line of output.<br>
I assigned the weekday() value to x in order to make the code more readable.<br>
On [W3 Schools page](https://www.w3schools.com/python/python_conditions.asp) I found an elegant if else statement with 3 conditions.<br>
I modified the statement, ran the program and got the expected answer.<br>


## Question 3 Methodology
_Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12._ <br>
I used the built-in range() function that generates arithmetic progressions. I used an if/and statement for i in the above mentioned range, print all results where i can be divided by 6 with no remainder and when being divided by 12 leaves a remainder.<br>
!= is a handy standard comparison operator that means not equal to<br>
f  (i % 6 == 0) and (i % 12 != 0): print (i)<br>
In order to test my result I started with a range (1000, 1100) and manually checked every output.  <br>
Once this proved correct I expanded the parameters.<br>


## Question 4 Methodology
_Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and,if it is even,divide it by two,but if it is odd,multiply it by three and add one. Have the program end if the current value is one._<br>
The instructions provided above refer to the collatz conjecture, this is
an unsolved mathematical problem at time of writing.<br>
No matter what number selected, the final result will always be one.<br>
This code can be used to test the theory and if you get a result other than one I'd be happy to take a cut of the $500 reward :stuck_out_tongue: <br>

Firstly ask the user to input a positive integer i.e. a whole number.<br>
Tell the user it must be a positive integer if it is not one<br>
Use the exit() method to stop the program running. <br>
It is the most reliable, cross-platform way of stopping code execution<br>

I have used the collatz function verbatim from user R2DPoop on [stackoverflow](https://stackoverflow.com/questions/33324432/collatz-sequence-python-3#)<br>
!= means not equal to, therefore when i is equal to 1 the loop won't happen<br>
There is no need to write code for both conditions i%2==0 and i%2==1 <br>
If one is true, the other is automatically false<br>
Finally, call the function collatz (x)<br>


## Question 5 Methodology

_Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime._<br> 

A prime number is greater than 1 and cannot be divided evenly by any other number except 1 and itself.<br>
Firstly ask the user to input a positive integer i.e. a whole number.<br>
Then exclude numbers less than or equal to 1 from being input at the outset because 1 is not prime and negative numbers cannot be.<br>   Use the exit() method to stop the program running. <br>
Code adapted from [Programiz website](https://www.programiz.com/python-programming/examples/prime-number)<br>
Use if/else loop to check for factors of x by iteration.  <br>
The equation x % 1== 0 determines whether the number can be divided by any other number in the range between 2 and itself.<br>
Use break statement to terminate the loop once all the numbers in the range have been exhausted to tell the user that the number is a prime i.e., it could only be divided by itself.<br>
 
## Question 6 Methodology

_Write a program that takes a user input string and outputs every second word._<br>

Solution adapted from contribution by user Merig on [stackoverflow](https://stackoverflow.com/questions/54857129/write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word/54857192#54857192)<br>
words = input("Enter a phrase: ")<br>
All data from the input command is stored as a string variable.<br>
Use the split method to break a string into words<br>
words = words.split()<br>
the [::2] slice syntax will return items from the array going up by two<br>
print (words[::2]) #this command outputs words 0,2,4 etc starting fom 0 not 1<br>
not every second word as the human eye counts<br>
but that is how the example provided for the problem appears so it must be grand<br>
I cannot figure out how to format the text to print without square brackets, commas and parenthesis!<br>
Enter a phrase: python problem set is a wonderful challenge<br>
['python', 'set', 'a', 'challenge']<br>


## Question 7 Methodology

_Write a program that that takes a positive ﬂoating point number as input and outputs an approximation of its square root._ <br>
I used the import statement to import a specific function from the math module. <br> 
According to "The Coder’s Apprentice" by Peter Spronck, it is possible to rename a function that you import from a module, using the
keyword as. This is helpful if using several modules that contain functions with similar names.<br>
I have included this renaming function to make my code easier to read for a beginner: squareroot not sqrt!<br>
As all data stored from the input command is stored as a string variable use the conversion process known as TypeCasting<br>
float() type casting will return the value between the parentheses as a floating-point number<br>
even though it was not input as one.<br>
I used the format() function to round down the decimals to one, it took a lot of experimentation with syntax in order to get the correct result.<br>
print ("The square root of", i, "is approximately {:.1f}.".format( squareroot(i)))<br>



## Question 8 Methodology
_Write a program that outputs today’s date and time in the format ”Monday,January 10th 2019 at 1:15pm”._<br>
Using imported time module, the following directives to indicate the particular format the date and time should take<br>
%A Weekday as locale’s full name<br>
%B Month as locale’s full name.<br>
%d Day of the month as a zero-padded decimal number.	<br>
%Y Year with century as a decimal number.<br>
%I:%M  Hour:Minute (12-hour clock) as a zero-padded decimal number.<br>
%p Locale’s equivalent of either AM or PM.<br>
print(datetime.datetime.now().strftime("%A, %B %d %Y at %I:%M %p"))<br>
Above code produces result in following format: "Sunday, March 10 2019 at 09:29 AM"<br>

The solution requires English ordinal suffix for the day of the month i.e. 10th and this is not a functionality of python. <br>
I adapted a piece of brilliant code to create a function called custom_strftime that provides a suffix by user gsteff from [stackoverflow website](https://stackoverflow.com/questions/5891555/display-the-date-like-may-5th-using-pythons-strftime/5891658#5891658)<br>
Day endings are usually "th", this code provides alternative endings on specified days.<br>
It uses the time module which provides various time-related functions.<br>
there is no requirement to import datetime module<br>
The localtime() function used instead of now() used in original code above returns current local time<br>
whereas datetime.now() function uses GMT time by default.


## Question 9 Methodology
_Write a program that reads in a text ﬁle and outputs every second line. The program should take the ﬁlename from an argument on the command line._<br>

Using the [python tutorial](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files),I adapted the example with open('honeybees.txt','r+') as f:.  It is good practice to use the with keyword when dealing with file objects.<br>
The first argument is a string containing the filename<br>
The second argument is another string containing a few characters describing the way in which the file will be used i.e., r+ opens the file for both reading and writing<br>
mylist = list(f)<br>
As advised by user Martijn Pieters on [stackoverflow](https://stackoverflow.com/questions/17569679/python-attributeerror-io-textiowrapper-object-has-no-attribute-split), the file can be read as a list of lines by calling list() on the file object<br>
I used the [::2] slice syntax to return items from the array going up in increments of two.<br>
The output is printed with new line characters \r\n, that is not how i want the text to appear.<br>
I tried using thecsv module, even though it is a text file, csv reader can remove delimiters and return file contents as a list of strings.<br>
The output is neat but I am unable to code correctly so that it returns every second line as per the instruction.<br>
import csv<br>
with open('honeybees.txt', newline='') as csvfile:<br>
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')<br>
    for row in spamreader:<br>
            print(' '.join(row))<br>
I am submitting the code that returns untidy output because it more accurately answers the problem.

## Question 10 Methodology
_Write a program that displays a plot of the functions x, x2 and 2x in the range [0,4]._<br>
I was not sure if I had matplotlib (Python 2D plotting library) on my machine, I input pip install matplotlib into cmder and got the output that the requirement was already satisfied.<br>
from matplotlib import pyplot as plt, plt is the standard abbreviation for pyplot<br>
Code adapted from one by Tacratis at [stackoverflow](https://stackoverflow.com/questions/54662759/how-to-plot-the-function-y-x2-using-python-program-in-matlpotlib/54915958#54915958)<br>
Create a variable to represent the values in the designated range.<br>
Use the list function for each of the functions you need to express (x, x2, 2x)<br>
List function consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses<br>
a = [x for x in X]<br>
b = [x**2 for x in X]<br>
c = [x*2 for x in X]<br>
Next, give the axes and the graph as a whole meaningful/relevant titles. <br>
plt.xlabel ('this is the X axis. Range [0,4]')<br>
plt.ylabel ('This is the Y axis')<br>
plt.title ('GRAPH SHOWING PLOT OF FUNCTIONS x, x2 AND 2x IN THE RANGE [0,4]')<br>
Insert keyword argument "label" into the plt.plot command which will plot the functions, this ensures a legend explaining the plots will be displayed.
The plt.show() command is important in order to render the plot.



## References
The references used also appear in the comments of the individual solutions.<br>

"The Coder’s Apprentice" by Peter Spronck<br>
"How to Think Like a Computer Scientist" by Allen Downey<br>
https://betterexplained.com/articles/techniques-for-adding-the-numbers-1-to-100/<br>
https://www.hashbangcode.com/article/stopping-code-execution-python <br>
https://docs.python.org/3/reference/<br>
https://docs.python.org/3/library/<br>
https://www.tutorialspoint.com/python/python_if_else.htm<br>
https://www.w3schools.com/python/python_conditions.asp<br>
https://www.thoughtco.com/how-to-determine-number-is-prime-2312518<br>
https://www.programiz.com/python-programming/examples/prime-number<br>
https://en.wikipedia.org/wiki/Collatz_conjecture<br>
https://stackoverflow.com/questions/33324432/collatz-sequence-python-3<br>
https://stackoverflow.com/questions/17569679/python-attributeerror-io-textiowrapper-object-has-no-attribute-split<br>
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files<br>
https://stackoverflow.com/questions/54857129/write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word/54857192#54857192<br>
https://www.pythonforbeginners.com/basics/list-comprehensions-in-python<br>
https://stackoverflow.com/questions/54662759/how-to-plot-the-function-y-x2-using-python-program-in-matlpotlib/54915958#54915958<br>
https://www.youtube.com/watch?v=aCULcv_IQYw<br>
