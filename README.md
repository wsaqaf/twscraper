# TWScraper 

A simple Python script that allows extracting, viewing and converting posts on Twitter web search results to CSV for further analysis. Requires no API access.

## Description

It is currently difficult to extract data from Twitter search results since API access is limited and prevents access to results going back longer than ten days.
The data can be extracted manually but it is labor-intensive. So this script does the job for you. All you need to do is save the results in a local HTML file using Inspect (instructions to follow) and let the script do the rest.

The data fetched for each post includes:
1- User name (@ handle) of the user publishing the tweet
2- Avatar link of the user
3- Text of the tweet
4- Number of replies
5- Number of retweets
6- Number of favorites

## Getting Started

### Dependencies

You need python 3+ and the libraries below:

* BeautifulSoup
* csv
  
### Installing

Simply store the file in its own folder and ensure that all the libraries are there (use pip install X, where X is the missing python package)

### Executing program

- First you need to go to search for the results on Twitter as you would normally do 
- Then you need to open the page and scroll down to load all the data you need to get (ajax dynamic loading makes it necessary to scroll)
- Once ready, simply right click and select 'Inspect' and open the Elements tab
- Right click on the <body>..</body> and have it collapsed, then select Copy Outer HTML
- Create a text editor with a file entitled X.html, where X is the name of the search results page
- Paste the data copied in the earlier step into the newly created file.
- Save the file to the data directory where the fbscraper.py is
- Do the above steps for as many searches as you want. Each search results need to be in a separate file ending with .html
- Then simply run the command prompt in the terminal window while in the same directory:
```
python twscraper.py X
```
where X is the name of the locally saved search files (saved in the data folder as X.html).

If successful, you will soon find X.csv in the data folder.

### Batch processing

You can also run the tool to process a batch of files. You can do this with the same command as above and have the file names of the pages listed as arguments as follows:
```
python fbscraper.py X1 X2 X3 X4
```
where X1,X2,X3 are the names of the locally saved search files saved as X1.html, X2.html, X3.html, etc.

The tool would then loop through them to extract data and save it as one CSV file per source: (X1.csv, X2.csv,..) The text of the tweets will be UTF-8 encoded.

## Author 

The principal author is Walid Al-Saqaf, a developer and senior lecturer at Södertörn University in Stockholm

Reach out to the developer by emailing to walid.al-saqaf@sh.se

## Version History

* 0.1
    * Initial Release

## License

This project is meant for educational purposes and is licensed under GNU General Public License (GPL)
