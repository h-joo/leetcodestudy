# leetcode study

This is a repository for a leetcode group study to assist the organizational
matter and also to hand over assignments, and also to present sample solution
written by myself. I made some effort on the hope that this material is
reusable for future use.

# Target audience and reasoning

The problem selection and the group study structure is tailored to be 
challenging for university students in their undergraduate degree which might
ot be as fluent as a full time software engineer, but still have basic 
understanding in data structure and algorithms and also have a solid
coding experience in at least one programming language.

The situation might be different between regions, but I feel the education
system at least in South Korea and Germany which I have experienced, 
understandably, doesn't offer to learn how to be competent at leetcode style
interviews, as the purpose of studying in the university is not for getting
a job in tech industry.

The problem solving skills people can usually pick up and train on their own,
but what I think is difficult to train without an industry experience is 
writing code in a consistent style. That's the reason why we have a separate
[StyleGuide](./StyleGuide.md) page to describe which style for each programming
language they should follow, as a part of the training.

# Group study structure

The owner of this repository will be acting as a tutor, mainly involved in
the the assignments handouts and reviewing attendees' solution via github pull
requests on a weekly basis. The weekly assignments are selected in a way that
attendees would not be able to finish in five hours, so they have to timebox on
which problem they will be solving. 

This is because unlike regular univesity courses, the activity in this study
group is only a voluntary and non evaluative, and I wanted attendees who are 
already in a competent level to be able to spend enough time practicing, 
while making everyone else not be overwhelmed and make aware that the weekly
assignments are not meant to be solved within five hours. To see how to sumbit
your assignments, please go to [Assignment submission](#assignment-handout-submission-code-review-and-discussion-session)

Also, after submitting solutions every week we will meet and the attendees
will explain their approach of how they solved the problem. I feel that 
people also get little chance in the university on explaining their technical
thoughts to others in a comprehensible manner, which as a regular SWE you grow
the skill over time, but is also critical for these kinds of interviews to
train them beforehand.

In the very beginning of the course, there will be a 
[level testing](#level-testing) session for each attendee with the tutor,
to have an idea on the group in general and to plan how to tailor the problems
appropriately.

# Level testing

There will be a one hour session for the tutor to understand the group, please
refer to some sample problems that I put in each study directory 
(e.g. [study0/LevelTest.md](./study0/LevelTest.md)). I will ask one or two
questions out of the two depending on how the attendees go along with them.

# Assignment handout, submission, code review, and discussion session.

## Assignment handout

The assignments will be posted in studyX/assignments.md 
(e.g. [study0/assignments.md](./study0/assignments.md)) every week.

## Setup for assignment submission

1. Create a public repository 
1. Create a directory for each week.

## Problem Solving

The submission tools in leetcode run and test your code against the visible and
hidden test cases. As it's running on a server, they are usually slower than 
when you run the result on the local machine. Thus, it's better that you have
the programming language installed on your local machine for better throughput
for testing at least for the visible test cases. 

So for the better utilization of your time, please pick up the test cases which 
are visible through its UI, so test your program with those before your actual
attempt to submit it.

## Submitting solutions

When you have a valid solution (a solution that passes on leetcode), create
a pull request and assign [h-joo](https://github.com/h-joo) to the PR.

Follow these steps to structure the file and PR: 

1. Create a branch for a submission of a solution to a single problem. 
   (Do NOT submit everything at once, because this will make me overloaded at the end of a week cycle)
2. Create a directory with a week number (e.g. week0)
3. Create a file following the name of the problem (`valid-boomerang`) with underscore instead of a hyphen (e.g. `week0/valid_boomerang.py`)
4. Put a comment at the top of the submitted files, a link to the problem e.g. :
```python
# https://leetcode.com/problems/valid-boomerang/
import math
...
```
You may submit multiple working solutions to the same problem, but then please
name the files with the number of attempt (e.g. `week0/valid_boomerang_01.py`)
and submit them in a separate PR.

## Discussion session

We will gather in groups and every attendees will explain their approach
and how they solved their problem. This might involve explaining the time
or spacial complexity, and I might ask for clarifications if I think the
explanation wasn't clear enough.
