1. Problem Statement

  Traditional digital cricket games often suffer from high complexity, long match durations, and heavy resource requirements. Casual fans and coding enthusiasts     lack a lightweight, text-based simulation that captures the core psychological thrill of the sport—the duel between batsman and bowler—without the need for         advanced graphics or hours of commitment. There is a need for a condensed, rapid-fire cricket simulation that focuses purely on strategy, probability, and the      "Hand Cricket" mechanic of prediction.

2. Scope of the Project

  The project involves the development of a Python-based console application that simulates a truncated version of a cricket match.
  
  In-Scope:
  
  Core Gameplay Engine: Implementation of a single-player vs. Computer logic using the random module.
  
  Match Logic: A strict 12-ball (2-over) innings limit per side.
  
  Wicket System: A customized "Sudden Death" mechanic where only 2 wickets are allowed per team; a match occurs when the User and Computer generate the exact same    integer.
  
  User Controls: The user controls the Toss decision (Bat/Bowl) and input selection (Runs 1-6).
  
  Scoring System: Automatic calculation of runs, wicket tracking, and target chasing.
  
  Win/Loss Determination: Logic to compare final scores and declare a Winner or a Tie.
  
  Out-of-Scope:
  
  Graphical User Interface (GUI).
  
  Multiplayer (PvP) functionality over a network.
  
  Complex cricket rules (Wide balls, No-balls, LBW, or fielding positions).
  
  Persistent data storage (High scores or player profiles).

3. Target Users

  Casual Gamers: Individuals looking for a quick, engaging distraction that takes less than 5 minutes to play.
  
  Cricket Enthusiasts: Fans of the sport who enjoy the statistical and strategic elements of "Hand Cricket."
  
  Programming Students: Learners seeking to understand game loop logic, state management, and random number generation in Python.

4. High-Level Features

  A. The "RNG" Bowler Engine

  The core opponent is driven by Python’s random.randint function. It generates unpredictable deliveries (integers 1-6) in real-time, ensuring no two matches are     ever the same.

  B. The "Hand Cricket" Dismissal Mechanic
  
  Unlike traditional cricket games where hitboxes determine outs, this project uses integer matching. If User Input == Computer Input, a wicket is lost immediately. This simulates the classic childhood game of Hand Cricket.
  
  C. The "Sprint" Innings Structure
  
  The game enforces a high-pressure environment with two hard limits:
  
  Ball Limit: Maximum of 12 iterations per loop.
  
  Wicket Limit: Maximum of 2 dismissals allowed.
  The innings ends instantly whichever limit is reached first.
  
  D. Strategic Toss Control
  
  To balance the difficulty of the RNG, the User is granted a permanent advantage: they automatically win the toss. This allows the user to strategize based on their preference for setting a target or chasing one.
  
  E. Real-Time Chase Tracker
  
  During the second innings, the system actively tracks the chasing team's score against the target. It provides real-time feedback on "Runs Needed" and "Balls Remaining," adding tension to the final moments of the game.
