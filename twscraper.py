#!/usr/bin/env python3
#Load the required libraries

from bs4 import BeautifulSoup
import sys,csv

#The below function scrapes data from each file individually and stores it in a separate CSV file
######################
def get_twitter_data(filename):
	try:
		with open("data/"+filename+".html", 'r') as content_file:
			content = content_file.read()
	except:
		print ("Could not read contents of file data/"+filename)
		sys.exit(-1)

#Indicate that scraping has started

	print ("Scraping:"+filename+"\n")

#Create the first soup instance from the content of the page
	soup = BeautifulSoup(content, 'html.parser')

#Identify and keep the main stream block of the twitter results. Discard the rest.
	tw_stream=soup.find(class_='stream')

# We can now extract all tweet blocks from the stream and put them in one list for further processing
	tweet_blocks=tw_stream.find_all(class_='content')

# Let us see how many blocks we have
	total_tweets=len(tweet_blocks)

	tweet_data=[]

#We want the data to be saved in a CSV file, so we initialize the first row with names of the variables

	tweet_data.append(['tweeter_id','avatar_url','tw_time','tw_text','tw_replies','tw_retweets','tw_favorites'])
	for tweet in tweet_blocks:
		tweeter_id=tweet(class_='username u-dir u-textTruncate')[0].b.get_text()
		avatar_url=tweet(class_='avatar js-action-profile-avatar')[0]['src']
		tw_time=tweet(class_='time')[0].a['title']
		tw_text=tweet(class_='js-tweet-text-container')[0].p.get_text().encode('utf-8')
 		tw_replies=tweet(class_='ProfileTweet-actionButton js-actionButton js-actionReply')[0](class_='ProfileTweet-actionCountForPresentation')[0].get_text()
 		if (tw_replies==''):
			tw_replies='0'
 		tw_retweets=tweet(class_='ProfileTweet-actionButton js-actionButton js-actionRetweet')[0](class_='ProfileTweet-actionCountForPresentation')[0].get_text()
  		if (tw_retweets==''):
       			tw_retweets='0'
   		tw_favorites=tweet(class_='ProfileTweet-actionButton js-actionButton js-actionFavorite')[0](class_='ProfileTweet-actionCountForPresentation')[0].get_text()
   		if (tw_favorites==''):
       			tw_favorites='0'
    
		tweet_data.append([tweeter_id,avatar_url,tw_time,tw_text,tw_replies,tw_retweets,tw_favorites])

# Save the results in a CSV file under the same name but with the extension 'csv'

	with open("data/"+filename+".csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(tweet_data)

#As an argument, take the file name (without the .html extension) of the file to scrape. Return an error if none or invalid
#############################

if len(sys.argv)<2:
        filenames=raw_input("File to scrape, use spaces for multiple files: ")
        if (len(filenames)==0):
                sys.exit()
	#Convert the string into a list with all the file names
	file_list = filenames.split(" ")
else:
        file_list=sys.argv[1:]

#Call the function "get_twitter_data()" with the filename as an argument for each file in the list

for filename in file_list:
	get_twitter_data(filename)

print ("Extraction done. See: data/ folder for the CSV files")
