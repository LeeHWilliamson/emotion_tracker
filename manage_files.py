import datetime
import json

#current goals
#take string and save it to a new file named with today's date if such file does not exist
#if file with today's date already exists, append file with string

#create file with todays date according to local timezone
print(datetime.datetime.today()) #this will give a date according to local timezone (gotten from posix timestamp)
                             #local timezone obviously based off where program is running, could correct to user's
                             #timezone by getting location user is connecting from and adding timedelta to localtime
                            #now I need to convert date to string so it can
print("hello")
def get_current_datetime():
    now = datetime.datetime.today() #create date object
    now_string = now.strftime('%Y-%m-%d %H:%M:%S') #convert to string
    print(now_string) #check
    today, current_time = now_string.split(" ", 1)
    print(today)
    print(current_time)
    return today, current_time

def write_thought_to_file(file_name, thought, timestamp):
    try:
        with open(file_name, 'r', encoding = "utf-8") as file:
            #file.write(f"{timestamp} --> {thought}\n")
            data = json.load(file)
        thought_dic = {timestamp : thought}
        data.update(thought_dic)
        print(json.dumps(data))
        with open(file_name, 'w', encoding = "utf-8") as file:
            json.dump(data, file)
            print(f"Your thought has been recorded under today's date, {file_name}")
    except FileNotFoundError:
        with open(file_name, 'w', encoding = 'utf-8') as file:
            thought_dic = {timestamp : thought}
            print(json.dumps(thought_dic))
            json.dump(thought_dic, file)
def read_file(file):
    try:
        with open(file, 'r', encoding = 'utf-8') as reader:
                data = json.load(reader)
                return data
    except FileNotFoundError:
        return[]

def main():
    today, current_time = get_current_datetime()
    file_name = f"{today}.json"
    thought = input("Please type whatever thought is going through your mind: ") #input allows us to accept user input
    write_thought_to_file(file_name, thought, current_time)

    print("\nTodays thoughts are...") #recall that calling print() initiates a new line so no need for trailing \n
    thought_to_read = read_file(file_name)
    print(thought_to_read)
    # for line in read_file(file_name):
    #     print(line, end="")

if __name__=="__main__":
    main()