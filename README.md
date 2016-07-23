# rax-python-test
rackspace cloud engineer python assessment

1. You can use any module you want. Write a service that runs two asynchronous loops, 
one produces a random message and puts it into a queue and another reads from the 
queue and threads a worker process to write that message into a log file. The worker 
process should only thread a max of 20 threads.
   
2. Write a function to print a 2-D array (n x m) in spiral order (clockwise).
 
For example, consider the following input:
***
1 2 3
4 5 6        
7 8 9
***

Then the output of your program should be:
***
1 2 3 6 9 8 7 4 5
***

3. Suppose you are programming for a really old-school internet newspaper, one that 
is so old-school that they only have monospace fonts. However, the editor really wants 
to see the monospace text justified to fit into the column space he has at a particular time. 
Your job is to write a program that will take as input the width of the column in characters 
and the entire text to be formatted, and return the same text except justified to fit into the column. 
The last line does not have to be justified.
 
For example, consider the following input:
***
20
The quick brown fox jumps over the lazy dog.
***
 
Then the output of your program should be:
***
The quick brown fox 
jumps over the lazy 
dog.
***

