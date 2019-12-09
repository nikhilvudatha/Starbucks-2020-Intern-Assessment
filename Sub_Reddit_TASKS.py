import praw

reddit = praw.Reddit(client_id='iYjUSs5_cXAOMA',
                     client_secret='0Hi2FgQCyreh7HizK9VZStprSQA',
                     user_agent='my user agent')

i = 0
Task0 = []
Task1 = []
Task2 = []
Task5 = []
finalTask = []
authorArray = []
titleArray = []
subredditArray = []
scoreArray = []
idArray = []
urlArray = []
comm_numArray = []


class allDataObject:

    def __init__(self):
        self.titleArray = []
        self.subredditArray = []
        self.scoreArray = []
        self.idArray = []
        self.urlArray = []
        self.comm_numArray = []
        self.authorArray = []

    def print_allDataObject(self):
        print ("Title: ", self.titleArray)
        print ("Subreddit: ", self.subredditArray[0])
        print ("# of Upvotes: ", self.scoreArray)
        print ("# of Comments: ", self.comm_numArray)
        print ("Submission ID: ", self.idArray)
        print ("URL: ", self.urlArray)
        if authorArray is not None:
            print ("Author: ", self.authorArray)


def add(s, submission):
    submission.titleArray.insert(s, submissions.title)
    submission.subredditArray.insert(s, submissions.subreddit)
    submission.scoreArray.insert(s, submissions.score)
    submission.idArray.insert(s, submissions.id)
    submission.urlArray.insert(s, submissions.url)
    submission.comm_numArray.insert(s, submissions.num_comments)


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j].scoreArray < arr[j + 1].scoreArray:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


for submissions in reddit.subreddit('popular').hot(limit=100):

    author = submissions.is_original_content

    OriginalList = allDataObject()
    Object = allDataObject()
    Object1k = allDataObject()
    Object_unique = allDataObject()
    Object_multireddit = allDataObject()

    add(i, OriginalList)
    Task0.insert(i, OriginalList)

    if author is False:
        add(i, Object)
        Object.authorArray.insert(i, submissions.author)
        Task1.insert(i, Object)

    if submissions.num_comments > 1000:
        add(i, Object1k)
        Task2.insert(i, Object1k)

    i = i + 1

print("\nThis is the Original Content(OC) by Redditor Task:\n")
for o in range(len(Task1)):
    print (Task1[o].print_allDataObject())
    print ("\n")

print("\nThis is the Over 1k comments Task:\n")
for k in range(len(Task2)):
    print (Task2[k].print_allDataObject())
    print ("\n")

bubbleSort(Task0)

print("\nThis is the Top 10 Upvotes Task:\n")
for v in range(10):
    print (Task0[v].print_allDataObject())
    print ("\n")

print("\nThis is the Unique Subreddits Task:\n")
uniqList = set()
for u in range(len(Task0)):
    uniqList.add(Task0[u].subredditArray[0])

for x in uniqList:
    print("r/", x)

print("\nThis is the MultiReddit Task:\n")

unilist = []
key = ''
first = False

for x in range(len(Task0)):
    if Task0[x].subredditArray[0] not in unilist:
        unilist.append(Task0[x].subredditArray[0])

    elif Task0[x].subredditArray[0] in uniqList:
        if first:
            key += str(Task0[x].subredditArray[0])
        else:
            key += '+' + str(Task0[x].subredditArray[0])

# print(key)
for submissions in reddit.subreddit(key).hot(limit=100):
    finalobj = allDataObject()
    add(i, finalobj)
    Task5.insert(i, finalobj)

for cx in range(len(Task5)):
    print(Task5[cx].print_allDataObject())
    print("\n")
