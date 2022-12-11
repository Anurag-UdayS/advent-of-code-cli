Advent of Code: CLI
===
Python branch
---

This is a tool used for solving <a href="www.adventofcode.com"> Advent of Code </a> puzzles right from the terminal.
(This branch is based on Python)

---

### Features I plan to implement:

_**1. .templates**_

_**2. Setup directory.**_
   + command to create a year directory.
   + all other functionality allowed only here.
   + JSON file that stores settings (`.aocsettings`)
   + JSON specifications:
      + *dirtype*: "year"
      + *year*: 20XX
      + in app settings, have a format "ydirname"
      + fmt %Y: Year in full, %y: Last 2 digits of year, %~y: First 2 digits of year
      + fmt.default: %Y

_**3. Setup inner directories:**_
   + command to create a day directory.
   + Directory Structure:

   + `.aocsettings`
      + *dirtype*: "day"
      + *day*: (int day)
      
   + fmt %D: Day and date (Monday 1st), %d: Date (1), %~D: Day (Monday), %~d: Short Day (Mon)

_**4. Instruction viewer:**_
   + view instructions of a particular day.
   + render as a full screen view
   + format code blocks separately (separate fg, hi, bg color).
