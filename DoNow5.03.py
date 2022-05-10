'''
#################
Do Now 5.03
#################
1. In your Console
-------------------
Type the following:
weekend_dates = {
  'April 2018': [7, 8, 14, 15, 21, 22, 28, 29],
  'May 2018': [5, 6, 12, 13, 19, 20, 26, 27]
}

print(weekend_dates['April 2018'])

In your Notebook
----------------
Respond to the following:
What type is weekend_dates? dictionary

What type the are keys? april 2018 and may 2018

What type the are values? the numbers

2. In your Console
-------------------
Challenge yourself with the following:
The 2018 Memorial Day holiday is observed on Monday, May 28, which makes it a long-weekend day.

Write a new line of code that adds May 28th to the list associated with 'May 2018'

So that its value becomes [5, 6, 12, 13, 19, 20, 26, 27, 28].
'''
weekend_dates = {
  'April 2018': [7, 8, 14, 15, 21, 22, 28, 29],
  'May 2018': [5, 6, 12, 13, 19, 20, 26, 27]
}

print(weekend_dates['April 2018'])

mylist = [28]

weekend_dates['May 2018'] + mylist

print(weekend_dates[f'May 2018' + {mylist}])
