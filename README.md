# Leafly Multi-threading Review Scraper

A python web scraper using the ```requests``` library to scrape reviews from the popular cannabis rating website, Leafly.com. Also takes advantage of multi-threading through the ```multiprocessing``` library to speed up scraping, which comes with python3 by default, utilizing more CPU to scrape up to 70 sites at once.



### Prerequisites

The following libraries are needed:
psutil (if logging cpu usage), requests, BeautifulSoup, datetime

```
pip install psutil
pip install requests
pip install bs4
pip install datetime
```

### Running

A step by step series of examples that tell you how to get the scraper running



## Scrape Cannabis strains from Leafly.com in order for preperation

Append / Uncomment ```weedStrainScraper()``` to the end of the leafly-scraper.py file


This runs the weedStrainScraper, which gets the name and urls to individual strains, to be used later in the process.


##Running The Scraper for Reviews

In the same directory as yur leafly-scraper.py, create a ```results``` folder. This is where the final csv's will go.

Append / Uncomment the following code at the end of the leafly-scraper.py file

```
threads = 1 #The amount of threads you want to run this at
weedfile = open("weed_file.txt", "r")
lines = weedfile.readlines()
if __name__ == '__main__':
    p = Pool(threads)
    records = p.map(writeToTextfile, lines)
```

Change the amount of threads based on how much the CPU can handle. A recommended amount is around 10 threads


## Running

From the command-line, run
```python leafly-scraper.py```
and watch the reviews come in!


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
