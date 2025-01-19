import datetime

#current goals
#take string and save it to a new file named with today's date if such file does not exist
#if file with today's date already exists, append file with string

#create file with todays date according to local timezone
print(datetime.datetime.today()) #this will give a date according to local timezone (gotten from posix timestamp)
                             #local timezone obviously based off where program is running, could correct to user's
                             #timezone by getting location user is connecting from and adding timedelta to localtime
                            #now I need to convert date to string so it can
def get_current_datetime():
    now = datetime.datetime.today() #create date object
    now_string = now.strftime('%Y-%m-%d %H:%M:%S') #convert to string
    print(now_string) #check
    today, current_time = now_string.split(" ", 1)
    print(today)
    print(current_time)
    return today, current_time

def write_thought_to_file(file_name, thought, timestamp):
    with open(file_name, 'a') as file:
        file.write(f"{timestamp} --> {thought}\n")
        print(f"Your thought has been recorded under today's date, {file_name}")
def read_file(file):
    try:
        with open(file, 'r') as reader:
            return reader.readlines() #recall this will return a list of strings with each item being a line from the file
    except FileNotFoundError:
        return[]

def main():
    today, current_time = get_current_datetime()
    file_name = f"{today}.txt"
    thought = input("Please type whatever thought is going through your mind: ") #input allows us to accept user input
    write_thought_to_file(file_name, thought, current_time)

    print("\nTodays thoughts are...") #recall that calling print() initiates a new line so no need for trailing \n
    for line in read_file(file_name):
        print(line, end="")

if __name__=="__main__":
    main()