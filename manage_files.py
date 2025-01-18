import datetime

#current goals
#take string and save it to a new file named with today's date if such file does not exist
#if file with today's date already exists, append file with string

#create file with todays date according to local timezone
print(datetime.date.today()) #this will give a date according to local timezone (gotten from posix timestamp)
                             #local timezone obviously based off where program is running, could correct to user's
                             #timezone by getting location user is connecting from and adding timedelta to localtime
#now I need to convert date to string so it can
today = datetime.date.today() #create date object
today_string = today.strftime('%Y-%m-%d') #convert to string
print(today_string) #check
today_string += ".txt"
print(today_string)
with open(today_string, 'a') as file:
    file.write("add this line to the file\n")
with open(today_string, 'r') as reader:
    for line in reader:
        print(line, end = " ")