import instaloader
from collection import counter
from Intertools import islice

A= instaloader.Instaloader()
user= input ('Παρακαλούμε Δώστε μου το Όνομα Χρήστη για τον οποίο ενδιαφέρεστε:')
profile= instaloader.Profile.from_username(A.context, user)


data=[]

for post in islice(profile.get_posts(),30):
    post_comments= post,get_comments()
    for comment in post_comments:
        data.append(comment.owner.username)

# print (data)
counter= counter(data)
most_occur= counter.most_common(1)
perisotera_occur= Counter.perissotera_occur(1)
print(' Tα περισσοτερα σχόλια στο¨συγκεκριμένο προφιλ ειναι:')
for x in rage (len (perissotera_occur)):
    print ( '1', perissotera_occur[x][0])
