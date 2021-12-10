# RMIT AI21 - Project - Pacman Capture the Flag

You must read fully and carefully the assignment specification and instructions detailed in this file. You are NOT to modify this file in any way.

* **Course:** [COSC1125/1127 Artificial Intelligence](http://www1.rmit.edu.au/courses/004123) @ Semester 2, 2021
* **Instructor:** Prof. Sebastian Sardina
* **Deadlines:**
  * **Preliminary Submission:** Sunday September 26rd, 2021 @ 11:59pm (end of Week 9)
  * **Final Submission:** Sunday October 17th, 2021 @ 11:59pm (end of Week 12)
  * **Wiki+Video Submission:** Sunday October 24th, 2021 @ 11:59pm (end of Week 13)
* **Course Weight:** 10%/15% (performance preliminary/final) + 10% (Wiki report) + 10% (Video)
* **Assignment type:**: Groups of 3 (other set-ups with explicit permission)
* **CLOs covered:** 1-6
* **Submission method:** via git tagging (see below for instructions)

The purpose of this project is to implement a Pacman Autonomous Agent that can play and compete in the RMIT AI21 _Pacman Capture the Flag tournament_:

 <p align="center"> 
    <img src="img/logo-capture_the_flag.png" alt="logo project 2" width="400">
    <img src="img/rmitlogo.png" alt="logo project 2" width="400">
 </p>
 
Note that the Pacman tournament has different rules as it is a game of two teams, where your Pacmans become ghosts in certain areas of the grid. Please read carefully the rules of the Pacman tournament. Understanding it well and designing a controller for it is part of the expectations for this project. Additional technical information on the contest project can be found in file [CONTEST.md](CONTEST.md). 

### Table of contents

- [RMIT AI21 - Project - Pacman Capture the Flag](#rmit-ai21---project---pacman-capture-the-flag)
    - [Table of contents](#table-of-contents)
  - [1. Your task](#1-your-task)
    - [Basic rules & guidelines](#basic-rules--guidelines)
  - [2. Deliverables and submission](#2-deliverables-and-submission)
    - [Preliminary code submission (Week 9, Sunday Sept 26th)](#preliminary-code-submission-week-9-sunday-sept-26th)
    - [Final code submission (Week 12, Sunday October 17th)](#final-code-submission-week-12-sunday-october-17th)
    - [Wiki report & Video (Week 13, Sunday October 24th)](#wiki-report--video-week-13-sunday-october-24th)
  - [3. Pre-contest feedback tournaments](#3-pre-contest-feedback-tournaments)
  - [4. Marking criteria](#4-marking-criteria)
  - [5. Inter-University Competition](#5-inter-university-competition)
  - [6. Important information](#6-important-information)
  - [7. AI21 Code of Honour & Fair Play](#7-ai21-code-of-honour--fair-play)
  - [8. Conclusion](#8-conclusion)
    - [Acknowledgements](#acknowledgements)

## 1. Your task

This is a **group project**. By now, one of the team member should have registered the team in the [Project Contest Team Registration Form](https://docs.google.com/forms/d/e/1FAIpQLSf5Q_zlQkYaZp1V-68kdCZFEmcJRmzbspkClZScz2xp4DzXNw/viewform) and tell the other students to join the team in GitHub Classroom. 

**Your task** is to develop an autonomous Pacman agent team to play the [Pacman Capture the Flag Contest](http://ai.berkeley.edu/contest.html) by suitably modifying file `myTeam.py` (and possibly some other auxiliary files you may implement). The code submitted should be internally commented at high standards and be error-free and _never crash_. 

In your solution, you have to use at **least 2 AI-related techniques** (**3 techniques at least for groups of 4**) that have been discussed in the subject or explored by you independently, and you can combine them in any form. Some candidate techniques that you may consider are:

1. Heuristic Search Algorithms (using general or Pacman specific heuristic functions).
2. Classical Planning (PDDL and calling a classical planner).
3. Value Iteration (Model-Based MDP).
4. Monte Carlo Tree Search or UCT (Model-Free MDP).
5. Reinforcement Learning – classical, approximate or deep Q-learning (Model-Free MDP).
6. Goal Recognition techniques (to infer intentions of opponents).
7. Game Theoretic Methods.
8. Bayesian inference.

You can always use hand coded decision trees to express behaviour specific to Pacman, but they won't count as a required technique. You are allowed to express domain knowledge, but remember that we are interested in "autonomy", and hence using techniques that generalise well. The 7 techniques mentioned above can cope with different rules much easier than any decision tree (if-else rules). If you decide to compute a policy, you can save it into a file and load it at the beginning of the game, as you have 15 seconds before every game to perform any pre-computation.

Together with your actual code solution, you will need to develop a Wiki report, documenting and describing your solution (both what ended up in the final system and what didn't), as well as a 5-min recorded video demonstrating your work in the project. Both these components are very important, as it can be seen by their weights.
 
### Basic rules & guidelines

When developing and submitting a solution, please make absolutely sure you adhere to the following base rules and guidelines:

* You must ALWAYS keep your fork **private** and **never share it** with anybody in or outside the course, except your teammates, _even after the course is completed_. You are **not allowed to make another repository copy outside the provided GitHub Classroom** without the written permission of the teaching staff. Please respect the [authors request](http://ai.berkeley.edu/project_instructions.html):

  > **_Please do not distribute or post solutions to any of the projects._**

* Your code **must run _error-free_ on Python 3.6/3.8**. Staff will not debug/fix any code. If your code crashes in any execution, it will be disqualified from the contest.
    * You can install Python 3.6 from the [official site](https://www.python.org/dev/peps/pep-0494/), or set up a [Conda environment](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/) or an environment with [PIP+virtualenv](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/). See also [this question in the FAQ](https://github.com/RMIT-COSC1127-1125-AI21/AI21-DOC/blob/main/FAQ-PACMAN.md#how-do-i-setup-a-system-in-windows-with-python-36).

* Your code **must not contain any personal information**, like your student number or your name. That info should go in the [TEAM.md](TEAM.md) file, as per instructions below. If you use an IDE that inserts your name, student number, or username, you should disable that.

* You are **not to change or affect (e.g., redirect) the standard output or error channels** (`sys.stdout` and `sys.stderr`) beyond just printing on standard output. If your file mentions any of them it will be breaking the "fair play" of the course (see below). These are used to report each game output and errors, and they should not be altered as you will be interfering negatively with the contest and with the other team's printouts. 

* Being a group assignment, you must **use your project Github** repository and GitHub team to collaborate among the members. The group will have write access to the same repository, and also be members of a GitHub team, where members can, and are expected to, engage in discussions and collaboration. Refer to the marking criteria below. 

## 2. Deliverables and submission

There will be two code submissions for this project and one wiki+video submission. 

Always submit substantially before the deadline, preferably one day before. Submitting close to the deadline could be risky and you may fail to submit on time, for example due to loss of Internet connection or server delays. 

### Preliminary code submission (Week 9, Sunday Sept 26th)

In the **preliminary submission** you are to:
 
1. Submit your first working version of your solution, by tagging the commit as "`preliminary`". 
2. Fill the [Project Certification \& Contribution Form (PRELIMINARY)](https://forms.gle/m4z7L21JApWSRNjt6).
    * Each member of the team should fill a separate certification form. Members who do not certify will not be marked and will be awarded zero marks.

### Final code submission (Week 12, Sunday October 17th)

In the **final submission** you are to submit your final submission to the project, which includes:

1. The `myTeam.py` implementing your AI-based Pacman agent team as per instructions above by tagging the relevant commit as "`submission`". 
2. A completed [TEAM.md](TEAM.md) file, with all the team member details. 

### Wiki report & Video (Week 13, Sunday October 24th)

As part of the final project, you will be need to submit:

1. A **Wiki report** in your GitHub team repository, documenting and critically analysing your Pacman agent system. 
   * At the very minimum the Wiki should describe the approaches implemented, a small table comparing the different agents/techniques you tried showing their performances in several scenarios, and an analysis of the strengths and weaknesses of your solution. For example, you may want to show how the addition of a given technique or improvement affected your system at some important point in the development. 
   * The description and analysis should include the techniques that made it to the final system, but you are encourage to report on techniques that you tried enough but did not make it to the final system. Explain why some techniques were not used in the final system, future extensions or improvements on your system, etc.
2. A **recorded 5-minute oral presentation** that outlines the theoretical and/or experimental basis for the design of your agents (i.e. why you did what you did), challenges faced, and what you would do differently if you had
more time. 
   * Your presentation must end with a live demo of your different implementations, i.e. showing how the different techniques your tried work. 
   * The video will be shared with us through an unlisted youtube link in the Wiki of your GitHub repository and via a corresponding form that will be made available in due time (if youtube is not possible, we will accept other submissions).
3. A filled [Project Certification & Contribution Form (FINAL)](https://forms.gle/RyUUiP6so6JuLirN8).
    * Each member of the team should fill a separate certification form. Members who do not certify will not be marked and will be awarded zero marks.
    * You will reflect on the team contribution with respect to the codebase, report, and video.

**IMPORTANT:** As can be seen by their weighting, the report and video are important components of the project. We strongly recommend working on them *during the development of the project and your system*, for example, by collecting data, screenshots, videos, notes, observations, etc. that is relevant and potentially useful. Do not leave these components to the last minute, as you may not have enough time to put them together at a high-quality.

## 3. Pre-contest feedback tournaments

We will be running **informal tournaments** based on preliminary versions of teams' agents in the weeks before the final project submission. We will start once **five teams** have submitted their preliminary agents by tagging their repos with "`testing`".

Participating in these pre-contests will give you **a lot of insights** on how your solution is performing and how to improve it. Results, including replays for every game, will be available only for those teams that have submitted. 

You can re-submit multiple times, and we will just run the version tagged `testing`. These tournaments carry no marking at all; they are just designed for **continuous feedback** for you to  analyse and improve your solution! You do not need to certify these versions.

We will try to run these pre-competitions frequently, at least once a day once enough teams are submitting versions.

The earlier you submit your agents, the more feedback you will receive and the better your chances of earning a high ranking!

## 4. Marking criteria

The overall project marks (worth 45% total of the course) are as follows:

| Component                                    | Marks  |
|--------------------------------------------- | ------ |
| Performance of the preliminary submission    | 10     |
| Performance of the final submission          | 15     |
| Quality of Wiki and types of techniques used | 10     |
| Quality of Video presentation                | 10     |
| Total                                        | 45     |

Note that the Wiki and Video are a *major* component of the project: they are  important places where you can demonstrate your knowledge of the material covered. This implies that you may achieve good marks without a top-top agent, as long as you are able to show concrete evidence in your Wiki+Video of the knowledge and skills you achieved during the project (including showing an analysis of what was tried but did not work!)

In both the preliminary and final submissions, a "contest" will be ran between each submission and a set of *predefined reference* staff teams over many fixed and random layouts (there will be no games among submissions themselves). Then, the performance of each submitted team is evaluated relative to the % of points it managed to attract when playing all the reference teams as follows (won game = 3 points, tie games = 1 point, and loss game = 0 points):

| % of points in contest  | Preliminary Contest Marks | Final Contest Marks |
| -----------------     | ------------------- | ------------- |
| 25%                   | 4                   | 1             |
| 38%                   | 7                   | 4             |
| 53%                   | 8                   | 9             |
| 88%                   | 10                  | 15            |
| Winner of contest     | 1 (bonus)           | 2 (bonus)     |

The precise number of marks will be calculated between the above % bands in a linear way. The only exception is the top band: once a submitted team attracts 88% of the contest points, it will earn full points (10 or 15). 

NOTE: The above % bands of attracted points in a contest are based on the performance of four _baseline_ agents when these play the reference agents. For example, our extremely basic agent which has very little intelligence and uses rudimentary techniques manages to attract 25% of the points when playing the reference teams. For an agent to demonstrate some level of AI knowledge and skills, it needs to perform above that (in the final contest). Note that the requirements are much less for the preliminary contest, in which obtaining 25% of the contest points already yields 4 of 10 marks.

In the final submission, the top-8 will enter into a playoff series to play quarterfinals, semi-finals and finals, time permitting live in the last day of class or in week 13 in a day specified for that (these final phases will not be part of the marking criteria, just bonus marks). Diplomas will be awarded to all teams entering the final playoff series.

Additional technical details can be found in [CONTEST.md](CONTEST.md). 

The final performance marks together with the **quality of the Wiki and the video** will determine the marks earned for the *final* submission (out of 35; without taking the preliminary submission), then finally adjusted as per **individual contribution** and **SE quality practices** (see below) as needed. So, for example:

* A PASS (17.5 marks out of 35) can be achieved by getting 80% for Wiki+Video and attracting just a bit more than 25% in the final contest (i.e., performing a bit better than the staff basic system). Alternatively, a PASS can be reached as well with 50% of the Wiki+Video's marks (10 in total) and 7.5 marks in the final contest (i.e., close to 50% of points attracted).
* An HD (28 marks out of 35) cannot be achieved without attracting 50%+ points in the contest (even with a perfect Wiki and Video), which corresponds to performing comparable to our top baseline agents.

Besides the correctness and performance of your solutions, you must **follow good and professional SE practices**, including good use of git and professional communication and team-work during your development such as:

* _Commit early, commit often:_ single or few commits with all the solution or big chunks of it, is not good practice.
* _Use meaningful commit messages:_ as a comment in your code, the message should clearly summarize what the commit is about. Messages like "fix", "work", "commit", "changes" are poor and do not help us understand what was done.
* _Use atomic commits:_ avoid commits doing many things; let alone one commit solving many questions of the project. Each commit should be about one (little but interesting) thing. 
* _Do not just upload files:_ git for software development should not be used as a storage service. Setup your system to do proper meaningful commits and do not use GitHub's upload button.
* _Commit evenly across the group team members_ (for team project/assignment components). This means there should be meaningful commits from _all_ participating members. Note that [peer programming](https://en.wikipedia.org/wiki/Pair_programming), which we encourage, does _not_ mean one member always or mostly acts as the "driver" and commit; *all* members should take turns, be the "driver" and commit to the repo. 
  * When peer-programming, make use of the [co-author facility](https://docs.github.com/en/github/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors) in GitHub to be accounted in the contributions. See [this post](https://gitbetter.substack.com/p/how-to-add-multiple-authors-to-a) and [this post](https://github.blog/2018-01-29-commit-together-with-co-authors/) as well about co-authors commits. You can conveniently include multiple co-authors to a commit via GitHub Desktop or via VScode (or otherwise by writing special commit messages) as explained in the links given.
* _Use the Issue Tracker:_ use issues to keep track of tasks, enhancements, and bugs for your projects. They are also a great way to collaborate in a team, by assigning issues and discussing on them directly. Check GitHub [Mastering Issues Guide](https://guides.github.com/features/issues/).
* _Follow good workflow:_ use the standard branch-based development workflow, it will make your team much more productive and robust! Check GitHub [Workflow Guide](https://guides.github.com/introduction/flow/). 
* _Communicate in the GitHub Team:_ members of the group are expected to communicate, in an adequate and professional way, in the GitHub team created along the repo. For example, you could use GitHub team discussions, use issues and pull requests to track development status, or create project plans in the Wiki. Video and voice chats outside of GitHub are permissible (and encouraged), but text communication should be through the GitHub team where possible.

**We will inspect the commit history in your remote repo** and the **GitHub team** to check for good ad proper SE practices and evidence of meaningful contributions of _all_ members. The results of these checks can affect the overall individual marks significantly, as point deductions may be applied when poor SE practices have been used or no clear evidence of contributions can be found. For example, few commits with a lot of code changes, or no or poor communication in the corresponding GitHub team may result in deductions, even if the performance of the submission is excellent. **We reserve the right to call for team and/or individual interviews when needed.**

## 5. Inter-University Competition

The top teams of the final tournament will be inducted to the [RMIT-UoM Pacman Hall of Fame](https://sites.google.com/view/pacman-capture-hall-fame/) and will qualify to the yearly championship across RMIT and The University of Melbourne, which runs every year with the best teams since 2017 onward (given you grant us permission, of course). This is just "for fun" and will attract no marks, but is something that previous students have stated in their CVs!

## 6. Important information

**Corrections:** From time to time, students or staff find errors (e.g., typos, unclear instructions, etc.) in the assignment specification. In that case, a corrected version of this file will be produced, announced, and distributed for you to commit and push into your repository.  Because of that, you are NOT to modify this file in any way to avoid conflicts.

**Late submissions & extensions:** A penalty of 10% of the maximum mark per day will apply to late assignments up to a maximum of five days, and 100% penalty thereafter (see [this question](https://docs.google.com/document/d/1MmfCuBPDQ6Q-_N0G98jEO0e46UwRg57BENvWKHQGhxI/edit?pli=1#heading=h.qys48nw89cxs) in the course FAQs. Extensions will only be permitted in _exceptional_ circumstances; see [this question](https://github.com/RMIT-COSC1127-1125-AI21/AI21-DOC/blob/main/CODE-INTEGRITY.md) in the course FAQs.

**Academic Dishonesty:** This is an advanced course, so we expect full professionalism and ethical conduct.  Plagiarism is a serious offense. Please **don't let us down and risk our trust**. Sophisticated _plagiarism detection_ software via [Codequiry](https://codequiry.com/) will be used in this edition to check submitted code against other submissions in the class as well as resources available on the web. These systems are really smart, so just do not risk it and keep professional and safe. We trust you all to submit your own work only; again, don't let us down. If you do, we will pursue the strongest consequences available to us according to the **University Academic Integrity policy**. In a nutshell, **never look at solution done by others**, either in (e.g., classmate) or outside (e.g., web) the course: they have already done their learning, this is your opportunity! If you refrain from this behavior, you are safe. For more information on this see file [Academic Integrity](ACADEMIC_INTEGRITY.md).

**We are here to help!:** We are here to help you! But we don't know you need help unless you tell us. We expect reasonable effort from your side, but if you get stuck or have doubts, please seek help. We will run a drop-in lab to support these projects, so use that! While you have to be careful to not post spoilers in the forum, you can always ask general questions about the techniques that are required to solve the projects. If in doubt whether a questions is appropriate, post a Private post to the instructors.

**Silence Policy:** A silence policy will take effect 2 days before this assignment is due. This means that no question about this assignment will be answered, whether it is asked on the newsgroup, by email, or in person after that time.


## 7. AI21 Code of Honour & Fair Play

We expect every RMIT student taking this course to adhere to the **AI21 Course Code of Honour** under which every learner-student should:

* Submit their own original work.
* Do not share answers with others.
* Report suspected violations.
* Not engage in any other activities that will dishonestly improve their results or dishonestly improve or damage the results of others.

Being a contest, we expect **fair play** of all teams in this project. If you are in doubt of whether something would break the good spirit of the project, you must check with us early, not wait to be discovered. Any behaviour or code providing an unfair advantage or causing harm will be treated very seriously. We trust you, do not let us down and be a fair player.

Unethical behaviour is extremely serious and consequences are painful for everyone. We expect enrolled students/learners to take full **ownership** of your work and **respect** the work of teachers and other students.


## 8. Conclusion

This is the end of the project assessment specification. Remember to also read the [CONTEST.md](CONTEST.md) file containing technical information that will come very useful (including chocolate prizes for the winners!).

If you still have doubts about the project and/or this specification do not hesitate asking in the [Course EdStem Discussion Forum](https://edstem.org/au/courses/6081/discussion/) and we will try to address it as quickly as we can!

**I very much hope you enjoy this final contest project and learn from it a lot**. 

**GOOD LUCK & HAPPY PACMAN!**

Sebastian

### Acknowledgements

This is [Pacman Capture the Flag Contest](http://ai.berkeley.edu/contest.html) from the set of [UC Pacman Projects](http://ai.berkeley.edu/project_overview.html). I am very grateful to UC Berkeley CS188 for developing and sharing their system with us for teaching and learning purposes.

I also acknowledge the fantastic support from tutor Andrew Chester in setting up and running this sophisticated project assessment. 