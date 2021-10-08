import random
import time

def generatestory():
    while True:
        when = ['A few years ago', 'Yesterday', 'Today', 'Once upon a time', 'Last year', 'On 7th jun', 'Tonight']
        who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
        residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
        went = ['cinema', 'university','seminar', 'school', 'laundry']
        happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
        print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
        time.sleep(3)
