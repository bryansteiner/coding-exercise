## Setup

- Created a new project on github
- Cloned to local repository
- Opened repository using Pycharm and created two scripts, one for each problem
- Python environment: 3.6.2

## Problem 1

**Problem:**
- Write a method *getMissingLetters*, which takes as input a string containing a sentence (of length n) and returns all the letters not present in the sentence

**Assumptions:**
- Length of given string: 0 < n < 50
- Ignore case sensitivity
- Ignore non-alphabet characters (i.e. %#$&)
- Ignore non-US-ASCII characters
- Returned answer should be all lower-case, alphabetical ordering
- Method can be called thousands of times in rapid succession
- Extra: produce a solution that handles the case of long strings (n > 100) efficiently

**Methodology:**

The problem is pretty clearly stated and so are its assumptions. I'll start be defining the function:

    def getMissingLetters(sentence=""):
        return None

I've decided to go ahead and use a default argument of an empty string; this way, function calls with no arguments will not throw an error and instead be treated like an empty string (i.e. we expact all letters to be returned "abc...xyz")
For now, we'll return *None* as a placeholder.

Let's consider the lower bound on the runtime complexity for this problem:
one line of reasoning is that this problem cannot run in less than *O(n)* time. The reason being: we must consider every character in the input before ultimately deciding whether a letter does or does not appear at all. For small sentences, this makes sense...

However, consider the case of an impossibly large sentence (n>1000). Do we really need to consider every character in the sentence to know that a specific letter is missing? I would argue that we only need to search through the letters of the sentence until we haven't exhausted every letter in the alphabet. This should stop us from doing a considerable amount of extra work in the case of very large sentences.

Thus, we set out with the reasoning that the worst possible case for this problem is *O(n)* time.

Now it's time to consider what data structure to use to track our letters. I immediately lean towards using a Python set (i.e. hashset). The reason is that we only have to consider unique appearances of a letter (and not every appearance). A set provides us with an average *O(1)* time for insertion and searches. Lets get started:

    import string
    import random

    def getMissingLetters(sentence=""):             # default argument: empty string --> should return "abcdef...xyz"

        alphabet = set(string.ascii_lowercase)      # set contains every letter of the alphabet
        appears = set()                             # set will hold unique letters we find in the sentence

        for x in sentence:
            if x.isalpha():                         # first check if x is even a letter
                appears.add(x.lower())              # only add lowercase letters to set
                if len(appears) == 26: break        # check if we've exhausted all possible letters

        solution = alphabet - appears               # set difference to get letters that don't appear at all in sentence

        solution = ''.join(sorted(solution))        # convert solution set to a sorted string
        return solution

To summarize, we've created a set of all letters *alphabet* and an empty set *appears*. For every letter we encounter in the sentence, we add its lowercase to the set *appears*. Finally, we take a set difference (set theory) to get the letters that haven't appeared in the sentence and we then perform a join operation on the sorted set to convert it into a string. Whenever we add letters to the set *appears*, we're careful and check that we in fact are looking at a letter and break from the loop if we've exhausted every letter of the alphabet (i.e. *appears* has 26 elements).

The following test cases were used:

    # Test cases:
    print(getMissingLetters("A quick brown fox jumps over the lazy dog"))
    print(getMissingLetters())
    print(getMissingLetters(''.join(random.choices(string.ascii_letters + string.digits + string.whitespace, k=100000000000))))

The program does not hang on the last test case (n=100000000000) so this is a satisfactory solution.

## Problem 2

**Problem:**
- Write a method *animate* that takes a positive integer *speed* and a string *init* giving the initial conditions of the particles
- The method returns an array of strings that represents the positions of the particles at each successive time step

**Assumptions:**
- The string 'init' will have either an 'L', 'R', or '.' at each position (leftwards, rightwards, empty)
- Assume initial conditions with size 0 < n < 50
- Initially, no position in the string will contain more than one particle at each position. For the animation phase however, this is entirely possible
- The first element of the return corresponds to the *init* string with an 'X' instead of an 'R' or 'L'
- The last element of the return shows the empty chamber at the first time interval it becomes empty
- Extra: produce a solution that also handles efficiently initial conditions with n > 100000 and speed > n/20

**Methodology:**

Let's start by once again defining the function and its parameters:

    def animate(speed, init):

The first things that comes to mind is that the particles move independently from one another. Apart from overlapping (i.e. sharing the same 'X'), they don't influence one another.

The next thing that became more obvious the longer I looked at the problem was that the position and movement of particles can be represented using bits. For each particle, we can use 1 to indicate a position is occupied and 0 for an empty position. Moving positions boils down to bitwise shifts and the number of shifts per time interval is determined by the speed.

In order to animate the particles at each step, we can go ahead and do a bitwise *or* operation. This will work for us even when two particles occupy the same position. See the script for the implementation and notes.
