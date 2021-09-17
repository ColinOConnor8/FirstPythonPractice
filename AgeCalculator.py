#current year variable when this was updated(2021)
curyear = 2021

#inputs to find day/month/year variables
year = int(input('What year were you born? '))
month = int(input('What month were you born? '))
day = int(input('What day were you born? '))

#if they were born before month updated(september) use this function
def printold():
    old = curyear - year
    print('You are ' + str(old) + ' years old!')

#if they were born after month updated(september) use this function
def printyoung():
    young = curyear - year - 1
    print('You are ' + str(young) + ' years old!')

#if they were born on month updated(september) but before the day this was updated(17th) use this function
def printoldday():
    oldday = curyear - year
    print('You are ' + str(oldday) + ' years old!')

#if they were born on month updated(september) but after the day this was updated(17th) use this function
def printyoungday():
    youngday = curyear - year - 1
    print('You are ' + str(youngday) + ' years old!')

#if born before month updated(september)
if month == 1:
    printold()
if month == 2:
    printold()
if month == 3:
    printold()
if month == 4:
    printold()
if month == 5:
    printold()
if month == 6:
    printold()
if month == 7:
    printold()
if month == 8:
    printold()

#if born after month updated(september)
if month == 10:
    printyoung()
if month == 11:
    printyoung()
if month == 12:
    printyoung()

#if born on month updated(september)
if month == 9:
    #if born before day updated(17th)
    if day == 1:
        printoldday()
    if day == 2:
        printoldday()
    if day == 3:
        printoldday()
    if day == 4:
        printoldday()
    if day == 5:
        printoldday()
    if day == 6:
        printoldday()
    if day == 7:
        printoldday()
    if day == 8:
        printoldday()
    if day == 9:
        printoldday()
    if day == 10:
        printoldday()
    if day == 11:
        printoldday()
    if day == 12:
        printoldday()
    if day == 13:
        printoldday()
    if day == 14:
        printoldday()
    if day == 15:
        printoldday()
    if day == 16:
        printoldday()
    
    #if born after day updated(17th)
    if day == 18:
        printyoungday()
    if day == 19:
        printyoungday()
    if day == 20:
        printyoungday()
    if day == 21:
        printyoungday()
    if day == 22:
        printyoungday()
    if day == 23:
        printyoungday()
    if day == 24:
        printyoungday()
    if day == 25:
        printyoungday()
    if day == 26:
        printyoungday()
    if day == 27:
        printyoungday()
    if day == 28:
        printyoungday()
    if day == 29:
        printyoungday()
    if day == 30:
        printyoungday()
    
    #if born on the day updated(17th)
    if day == 17:
        printoldday()
        print('Today is also your Birthday! Happy Birthday!')