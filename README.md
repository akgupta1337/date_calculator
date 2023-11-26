# Date Calculator

## Overview

Welcome to the **Date Calculator** repository! This simple Python script (`date_calculator.py`) allows you to calculate the total number of days between two given dates without importing any external libraries.

## How It Works

The `date_calculator.py` script takes two dates as input: `dob` (date of birth) and `tod` (today's date), in the format `DDMMYYYY`. It then computes the total number of days between them, including both the start and end dates.

## Usage

To use the Date Calculator:

1. Open the [date_calculator.py](date_calculator.py) file.
2. Modify the `dob` and `tod` variables with your desired dates in the format `DDMMYYYY`.

   ```python
   # Example Input
   dob = "15031990"  # March 15, 1990
   tod = "01122022"  # December 1, 2022

   # Convert to integers
   dd = int(dob[:2])
   mm = int(dob[2:4])
   yy = int(dob[4:])

   dd1 = int(tod[:2])
   mm1 = int(tod[2:4])
   yy1 = int(tod[4:])
