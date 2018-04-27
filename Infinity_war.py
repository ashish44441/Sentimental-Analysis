import tweepy
from textblob import TextBlob

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


consumer_key='vLFJhlGQQsLaKfG8DKiY0LXxu'
consumer_secret='ukAduQyU7AEPEnbnKA3zaPhPmRZ5epveAzo5eP79em7d7lt9nb'

access_token='175753801-6jVfPdLReeuIcKC2mF0aLdf1J6Fafg3nZtcViibz'
access_token_secret='thLWXpBLxMKWfBoZFFdD5tDJ6fA1EKhFUx4mkukDQjCJS'

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api=tweepy.API(auth)

searchTerm = input("Enter Keyword to search about: ")

tweets = tweepy.Cursor(api.search, q=searchTerm).items(500)

#public_tweets=api.search('AvengersInfinityWar')
im= []
b = []
t=[]
h=[]
ca=[]
ds=[]
bp=[]
n=[]
g=[]
th=[]
sh=[]

for tweet in tweets:
	analysis= TextBlob(tweet.text)
	im1=analysis.word_counts['ironman']
	im.append(im1)
	
	b1=analysis.word_counts['bucky']
	b.append(b1)

	t1=analysis.word_counts['thor']
	t.append(t1)

	h1=analysis.word_counts['hulk']
	h.append(h1)

	ca1=analysis.word_counts['captainamerica']
	ca.append(ca1)

	ds1=analysis.word_counts['doctorstrange']
	ds.append(ds1)

	bp1=analysis.word_counts['blackpanther']
	bp.append(bp1)

	n1=analysis.word_counts['nebula']
	n.append(n1)

	g1=analysis.word_counts['groot']
	g.append(g1)

	th1=analysis.word_counts['thanos']
	th.append(th1)

	sh1=analysis.word_counts['shuri']
	sh.append(sh1)



ironman=sum(im)
bucky=sum(b)
thor=sum(t)
hulk=sum(h)
captainamerica=sum(ca)
doctorstrange=sum(ds)
blackpanther=sum(bp)
nebula=sum(n)
groot=sum(g)
thanos=sum(th)
shuri=sum(sh)


print("Ironman: " + str(ironman))
print("Bucky: " + str(bucky))
print("Thor: " + str(thor))
print("Hulk: " + str(hulk))
print("Captainamerica: " + str(captainamerica))
print("Doctorstrange: " + str(doctorstrange))
print("Blackpanther: " + str(blackpanther))
print("Nebula: " + str(nebula))
print("Groot: " + str(groot))
print("Thanos: " + str(thanos))
print("Shuri: " + str(shuri))


objects = ('IronMan','Bucky','Thor','Hulk','Captain','Strange','Panther','Groot','Thanos')
y_pos = np.arange(len(objects))
performance = [ironman,bucky,thor,hulk,captainamerica,doctorstrange,blackpanther,groot,thanos]
 
plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('How many times mentioned')
plt.title('Who is the most popular in Infinity War')
 
plt.show()
