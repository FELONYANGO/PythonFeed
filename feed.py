import feedparser
 
NewsFeed = feedparser.parse("https://www.standardmedia.co.ke/rss/kenya.php")

entry= NewsFeed.entries[1]


print ("     ")
print (entry.title)
print ("     ")
print (entry.published)
print ("     ")
print (entry.summary)
print ("     ")
print (entry.links)