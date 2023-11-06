# Text-Analysis-Project: Analysing World Event from Different Perspectives

## Project Overview

For this project I used two data sources: Newspaper API and Wikipedia API. The objective was to analyze one topic from several perspectives by looking at various sources. I chose the ongoing Israel-Hamas war as the topic, seeing that it is controversial, yet has some common ground that all sources might meet on. The analysis was done by conducting a sentiment analysis on 5 articles and a wiki page, along with looking at the most common words found in each of these sources.

## Implementation

To start, I downloaded the necessary programs and API's. For the sentiment analysis I used NLTK as my primary source to parse, tokenize, and eventually analyze the data. For the data I downloaded and parsed 5 articles from newspapers individually and conducted a simple sentiment analysis. Here I used a list to initially parse all articles and then a list to collect the scores. On a side note, I also made sure that all the articles were realeased around a similar time and were all 'explainers' instead of breaking news. 

The wiki page was manually found and then the sections containing the 'background' and 'events' of the topic were selected for parsing and sentiment analysis. For the wiki I did not use any data structure, just simply printed the result.

The word count was done by using NLTK, from where I used its 'stopwords' variable and 'Counter' class to tokenize and analyze common words in each source. I began this process by using the dataset 'stopwords.txt' and applying the code we looked at in class, but then soon ran into trouble as I couldn't remove all the relevant values (alpha numeric values). I searched for an alternative and found that NLTK had a module to help with this. I then turned to ChatGPT for further explanation, and ended up modifying the code it provided for my use. The conversation between Chat and I is linked at the end of this file.

## Results

I wanted to see if I could get any interesting insights on two fronts. Firstly, if wikipedia is relatively more neutral than its news counterparts. And the sentiment analysis indicates that most likely yes, wikipedia holds more neutral. Its score of -0.84 was slightly higher than all the news articles scores. Given the morbidity of the topic, this was surprising to see. However, amonngst the news articles, it was hard to deduce something from their sentiment scores which ranged from -0.88 to -1. This made it hard to answer my second question: what were some key differences in each sources approach?

Thus the word count analysis. At first it seemed fruitless but once I started looking at the words carefully, there were some common words that were only used by specific articles. For example, Article 5 (Vox) is the only one that has 'biden' and 'us' in its top 10 words. Similary, Article 1 (The Guardian) contains 'intifada', a word not found anywhere else. The true insight came after closer inspection. Article 5 focuses on how US foreign policy and negligence has led to the current situation, thus implicating the US as a perpetrator. In Article 1, intifada - meaning civilian uprising - is used in a positive context to defend the palestinian movement. My understanding is that Article 1 and Article 5 were more sympathetic to the palestinian cause compared to the others.

## Reflection

This was a fun project. I enjoyed it a lot more than anything else we've done in class. Mainly because of the design aspect of the assignment. Which also ended up being the hardest part. It took me several days just to come up with a good plan, selecting the right tools and sources, and then putting it all in words. The coding itself became straightforward after I knew where to look. I ended up using the NLTK guide quite often. It was interesting to read documentation, then try the code, then go back, and so forth. When it got frustrating, I would start asking ChatGPT questions about my plan, to see if it had any ideas. Involving AI in the brainstorming process also helped me feel like I wasn't doing this alone. This is something I would like to leverage more of in the future.

In terms of scope, I think the project was appropriate for me, seeing that I tried all the things that interested me and also, hopefully, hit the criteria of the assignment. I do think visuals could've helped however. I just didn't plan for them early enough and ran out of time. I also completely forgot to end my functions with return and make them editable for the main function. So I ended up copying my two files into one and then running main. I tried correcting the error, but then I started messing up my code, and decided to let it be.

Overall, great fun. Going forward, allowing more time for design and planning is the plan. I feel more confident running my own projects going forward, and have a good idea of what I'd like to do for the final!


## Sources 
https://chat.openai.com/c/8949bb65-f738-4183-9782-17fd70e578ec
https://newspaper.readthedocs.io/en/latest/
https://www.nltk.org/howto/corpus.html
https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#performing-nlp-on-an-article
https://stackoverflow.com/questions/7185288/how-can-i-get-wikipedia-content-using-wikipedias-api