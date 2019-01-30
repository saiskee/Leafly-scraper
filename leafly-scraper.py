import psutil
import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup
import datetime
date = datetime.datetime.now()

def weedStrainScraper():
    weed_file = open("weed_file.txt","a+")
    for i in range(57):
        html = requests.get("https://www.leafly.com/explore/page-"+str(i)+"/sort-alpha").text
        soup = BeautifulSoup(html,'html.parser')
        a = soup.findAll("a",{"class":"ga_Explore_Strain_Tile"})
        for link in a:
            b = link.findChildren("text",{"ng-if":"!name"})
            c = b[0].findAll(text=True)
            for item in c:
                if item == "\n":
                    c.remove(item)
            output = (link.get('href')+": " + c[0]).encode('ascii',errors='ignore').decode()
            weed_file.write(output + "\n")
    weed_file.close()


def reviewLinkScraper(url):
    result = []
    
    for i in range(10000):
        # print(psutil.cpu_percent())
        print(url+"?page="+str(i)+"&sort=rating")
        html1 = requests.get(url+"?page="+str(i)+"&sort=rating").text
        soup1 = BeautifulSoup(html1, 'html.parser')
        review_divs = soup1.findAll("div", {"class": "m-review"})

        if len(review_divs) == 0:
            print("hello")
            break
        for div in review_divs:
            username = div.findChild(
                "h3", {"class": "copy--xl padding-rowItem no-margin"})
            review = div.findChild("p", {"class": "copy--xs copy-md--md"})
            full_review_link = div.findChild(
                "a", {"class": "copy--xs copy-md--md"})
            output = username.getText().replace("\n", "") + "," + "https://www.leafly.com" + \
                full_review_link.get(
                    'href') + ",\""+review.getText().encode('ascii', errors='ignore').decode() + "\""
            result.append(output.encode('ascii', errors='ignore').decode())
            # 9 reviews per page
    return result


def getUrl(lines):
    result = []
    for line in lines:
        linearray = line.split(":")
        result.append("https://www.leafly.com" +
                    linearray[0].strip() + "/reviews")
    return result


def writeToTextfile(line):
    linearray = line.split(":")
    print("Scraping "+linearray[1].strip())
    url = "https://www.leafly.com"+linearray[0].strip()+"/reviews"
    print("URLSCRAPE " + url)
    strain = linearray[0].split('/')[2]
    fileurl = "results/"+strain+".csv"
    output_text = open(fileurl, "w")
    array = reviewLinkScraper(url)
    output_text.write(linearray[1].strip() + "\n" + linearray[0].strip() + "\n")
    output_text.write("=============" + "\n")
    output_text.close()
    file = open(fileurl, "a+")
    for elem in array:
        file.write(elem + "\n")
    file.close()


#run the below method to collect strains into weed-file.txt
# weedStrainScraper()

#run the below method to 
threads = 1
weedfile = open("weed_file.txt", "r")
lines = weedfile.readlines()
if __name__ == '__main__':
    p = Pool(threads)
    records = p.map(writeToTextfile, lines)
