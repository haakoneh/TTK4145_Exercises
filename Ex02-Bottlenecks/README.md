Exercise 2 : Bottlenecks
========================

Mutex and Channel basics
------------------------

First some theory. What is:
 - An atomic operation?
 - A semaphore?
 - A mutex?
 - A critical section?


___


Solve [the concurrent access problem from Exercise 1](https://github.com/TTK4145/Exercises/tree/master/Ex01-Intro#4-finally-some-code), such that the final result is always zero.

Make sure that the two threads intermingle. Running them one after the other would somewhat defeat the purpose.

(It may be useful to change the number of iterations in one of the threads, such that the expected final result is not zero (say, -1). This way it is easier to see that your solution actually works, and isn't just printing the initial value)


####C:

 - POSIX has both mutexes ([`pthread_mutex_t`](http://pubs.opengroup.org/onlinepubs/7990989775/xsh/pthread.h.html)) and semaphores ([`sem_t`](http://pubs.opengroup.org/onlinepubs/7990989775/xsh/semaphore.h.html)). Which one should you use?
 - Acquire the lock, do your work in the critical section, and release the lock


####Go:

We are doing Go a great disservice in this exercise, since it has a message-passing no-sharing approach to concurrency. With that said, we will still go further down the wrong path and use shared variables, with blatant disregard for the proper way of doing things. We have two major alternatives:
 - Put the shared resource `i` in a buffered channel, and read from (when there is a value there) & write to (when we are done modifying our local copy) that channel.
   - You will have to assign the value of the local copy to the global value on each iteration, otherwise the global value will never be changed.
 - Something more "semaphore-like", where the shared resource `i` is not in a channel, but we instead put some other value representing "ownership" on a buffered channel.
   - You would "take ownership" when there is a value on the channel (by receiving from it), and "give back" ownership by putting something on the channel (by sending over it).

We also have a more idiomatic way:
 - Create a server that [`select{}`](http://golang.org/ref/spec#Select_statements)s transformations to its own data. Have two other goroutines tell the server to increment & decrement its local variable.
   - Note that this variable will no longer be global, so it cannot be read by other goroutines. The proper way to handle this is to create another `select{}`-case where others can request a copy of the value.


Remember from Exercise 1 where we had no good way of waiting for a goroutine to finish? Try sending a "finished"/"worker done" message on a separate channel. If you use different channels for the two threads, you will have to use [`select { case... }`](http://golang.org/ref/spec#Select_statements) so that it doesn't matter what order they arrive in.


It seems that Go's approach to concurrency does not lend itself well to solving this (admittedly contrived) problem. Can you think of a problem/example where the opposite is true (where message passing is easy, and shared variables is hard)?

####Python:

Python provides both [Locks](http://docs.python.org/2.7/library/threading.html#lock-objects) (which are like mutexes) and [Queues](http://docs.python.org/2/library/queue.html) (which are kind of like channels). 



Choosing a language
-------------------

In Exercise 3, 4 (Network exercises) and the project, you will be using a language of your own choice. You are of course free to change your mind at any time, but to help avoid this situation (and all its associated costs) it is worth doing some research already now.

For some places to start reading, maybe look at [this list](https://github.com/TTK4145/Project/tree/master#language-resources). Send in your suggestions if you find more and/or better resources.

Here are a few things you should consider:
 - Think about how want to move data around (reading buttons, network, setting motor & lights, state machines, etc). Do you think in a shared-variable way or a message-passing way? Will you be using concurrency at all?
 - How will you split into modules? Functions, objects, threads? Think about what modules you need, and how they need to interact. This is an iterative design process that will take you many tries to get "right" (if such a thing even exists!).
 - The networking part is often difficult. Can you find anything useful in the standard libraries, or other libraries?
 - The elevator driver is written in C. How do you interface with C code?
 - You may want to work from home, where you won't have an elevator. Does the language have a framework for making and running tests, or can you create one? Testing multithreaded code is especially difficult.
 - Code analysis/debugging/IDE support?

Extra reading material
----------------------

[Different forms of message passing](http://cs.lmu.edu/~ray/notes/messagepassing/), with nice diagrams

[Origins and pitfalls of the recursive mutex](http://zaval.org/resources/library/butenhof1.html). (TL;DR: Recursive mutexes are usually bad, because if you need one you're holding a lock for too long)





