f=open("PyPoll/Resources/election_data.csv","r")
print(f.readline())
for x in f:
    print(x)
    