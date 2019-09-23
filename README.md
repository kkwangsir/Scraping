# Scraping
This project has 2 part, one is scraping indeed.ca by beautifulSoap and selenium, then save csv file, 2nd part is data visulization, infuture it will have GUI by PyQt5

The scrape processing

I used the selenium and webdriver to read the real web pages, and iterate innerhtml the of id:result to collect the few tags of data, 
and when indeed show promotion page I added a script to find close buttom


click the pic or link below to go to youtube 
[![Watch the video](https://img.youtube.com/vi/irgcfEXtVkk/maxresdefault.jpg)](https://youtu.be/irgcfEXtVkk)

https://youtu.be/irgcfEXtVkk

********************************************

Data Analysis

Through the spider, we got two csv files, which are job advertisements for Saskatchewan python and Java programmers. 
First I cleaned up the duplicates, and then sorted the employers who posted the job ads, and then got the top ten companies.
<p align="center">
  <img src="https://github.com/kkwangsir/Scraping/blob/master/img/companies.png" width="1000" title="hover text">0
</p>


Finally, I analyzed the job description and took the keywords for the programmer's level. Through the previous data, I know that there are 77 positions. Through the keyword chart, I know that the Saskatchewan IT company has a strong demand for senior programmers, and the demand for entry level programmers is not high.
I think that most entry programmers work in companies that come through the school's coop or intern , so public information sites can hardly see a large number of entry programmers' job advertisements.

<p align="center">
  <img src="https://github.com/kkwangsir/Scraping/blob/master/img/level.png" width="1000" title="hover text">0
</p
