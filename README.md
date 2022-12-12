Advent of Code: CLI
===
Python branch
---

This is a tool used for solving [Advent of Code](www.adventofcode.com) puzzles right from the terminal.
(This branch is based on Python)

---

### Features I plan to implement:

_**1. `fmt` - A formatting features:**_

_**2. .templates:**_

_**3. Setup directory.**_
   + command to create a year directory.
   + all other functionality allowed only here.
   + JSON file that stores settings (`.aocsettings`) specifications:
      - *dirtype*: "year"
      - *year*: 20XX
      - in app settings, have a format "ydirname"
      - fmt %Y: Year in full, %y: Last 2 digits of year, %~y: First 2 digits of year
      - fmt.default: %Y

_**4. Setup inner directories:**_
   + command to create a day directory.
   + Directory Structure:

   + `.aocsettings`
      + *dirtype*: "day"
      + *day*: (int day)
      
   + fmt %D: Day and date (Monday 1st), %d: Date (1), %~D: Day (Monday), %~d: Short Day (Mon)

_**5. Instruction viewer:**_
   + view instructions of a particular day.
   + render as a full screen view
   + format code blocks separately (separate fg, hi, bg color).

_**6. Test as per directory structure:**_
   + test as per directory structure.

_**7. Fetch both sample input and main input:**_

_**8. Submit straight away:**_
   + submit main answer from CLI
   + option to submit without confirmation.
