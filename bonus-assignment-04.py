# You will still submit this as a pull request on github to
# *your* bonus repo: `firstname-lastname-bonus-repo`

# When I say the second element, I mean the element with index 1
# When I say element two, I mean the element with index 2

# Question 1. consider the following list
a = [1, 2, 3, 4, 45, 5, 3, 5, 6, 7, 77]
# Select the third element using a positive index
a[2]
# Select the third element using a negative index
a[-9]
# Select the first 4 elements
a[0:4]
a[:4]
# Select the last 4 elements
a[-4:]
# Select the 5th and 7th item (result should be a list)
a[5]
[a[6], a[8]] 
a[1]
a[0:1]
# OR
[a[-5], a[-3]]
# OR
a[6:9:2]

# Add the elements [5, 5, 9] to the end of `a`
a.extend([5, 5, 9])
a
# Question 2. Explain (not code) why mutability is good.
#
# Written answer:


# Question 3. Explain (not code) why mutability is bad.
#
# Written answer:


# Question 4. Consider `a` and `b``. Run the following lines:
a = [1, 2, 3]
b = a
# Next, change `a` to [100, 2, 3] by *recreating* `a``.
# Then inspect the value of `a` and `b`.
a = [100, 2, 3]
a
b
# Did `b` change to `[100, 2, 3]`?
#no,  recreating a changes a and b to point to different places in memory
# Written answer:


# Question 5. Consider a and b. Run the following lines:
a = [1, 2, 3]
b = a
# Next change `a` to [100, 2, 3] by *subsetting `a` and assigning 100 to the subset*.
# Then inspect the value of `a` and `b`.
a[0] = 100
a
b

# Did `b` change to `[100, 2, 3]`?
#
# Written answer:
#yes, a and b point to the same place in memory, changing the first element
# for that list affects the same data structure they both point to.

# Question 6: Put tuples through the same tests and report on the results
a = (1, 2, 3)
b =  a 
a = (100, 2, 3)
a
b
# Written answer:


# Question 7: Translate the math in the below linked image into python code
# https://utk.instructure.com/courses/180504/files?preview=17838225
# x and y provided:
y = [35, 40, 65, 100, 95]
x = [10, 20, 30, 40, 50]


# What's this math/code doing? Write a little description of what task it does.
#
# Written answer:
