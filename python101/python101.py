

class Attendee(object):
    def __init__(self, slack_handle, line_count=0):
        self.slack_handle = slack_handle
        self.line_count = line_count
    def __str__(self):
        return self.slack_handle

attendee_list = list()
while True:
    add_new = raw_input("Do you want to add a new person?")
    if add_new == "y":
        slack_handle = raw_input("Enter person's slack handle.")
        line_count = raw_input("Enter person's line count.")
        line_count= int(line_count)
        new_attendee = Attendee(slack_handle, line_count)
        attendee_list.append(new_attendee)
        if len(attendee_list) > 4: #Change to 48
            for i, attendee in enumerate(attendee_list):
                if i % 4 == 0:
                    print('Group:')
                print(attendee)
    else:
        if len(attendee_list) % 4 != 0:
            print("Please keep going")
        else:
            break

# we have a list of all of the attendees we want
attendee_list.sort(key = lambda a: a.line_count)

while len(attendee_list) > 0:
    median_index = len(attendee_list) / 2
    slackers = (attendee_list[median_index - 2], attendee_list[median_index - 1])
    overachievers = (attendee_list[median_index], attendee_list[median_index + 1]) 
    for slacker in slackers:
        print("{} wrote less than median with {} lines of code".format(slacker.slack_handle, slacker.line_count))
        attendee_list.remove(slacker)
    for over in overachievers:
        print("{} wrote more than median with {} lines of code".format(over.slack_handle, over.line_count))
        attendee_list.remove(over)


def test_attendee():
    a = Attendee("Anish", 8)
    assert a.slack_handle == "Anish"
    assert type(a.line_count) is int


