# Election Analysis

## Overview of Election Audit: 

Colorado election officials are interested in upgrading their methodology of counting ballots. They currently use Excel to calculate election results, but they are interested in an automated process which could be interchangeably used for elections from the local to federal level. We will begin with a congressional precinct which spans three counties. These are our findings:

  - A total of 369,711 votes were cast. Excel would have told us this just as easily as our code with Python, but we have a much greater degree of flexibility with how we can use a breakdown of these votes.
  - 38,855 votes were cast in Jefferson county, or 10.5% of the total vote. 306,055 votes were cast in Denver county for 82.8% of the total vote. 24,801 were cast in Arapahoe County for 6.7% of total votes cast. Excel would have given us these figures rather easily as well, but with our code we could feed in different election results with almost no modifications, and get accurate results.
  - Denver County had, by a wide margin, the largest number of votes with 306,055, or 82.8%.
  
### Breakdown of the number of votes and the percentage of the total votes for each candidate:

Disgraced Republican incumbant Charles Casper Stockham struggled to convince voters that he was a 'new man' after a series of scandals which left his marriage in tatters and the 'nonprofit' of his namesake in financial ruin. His disappointing return of 85,213, or 23.0% of the votes cast was not much of a surprise to many analysts.

Diana DeGette was able to unify progressives and moderate Democrats and muster up a whopping 73.8% of the vote with 272,892 ballots cast in her name.

Libertarian Raymon Anthony Doane was the beneficiary of Stockham's many scandals, but voters were reluctant to overlook his eccentricities and his penchant for referring to himself as "the smartest man you've ever met" (his words). Somehow, he still seemed overjoyed to receive 11,606 votes, or 3.1% of the total votes.


Diana DeGette handily won this election with 73.8% of the votes cast or 272,892 total votes. Her 'big tent' campaign resonated with a wide spectrum of voters already on the left, as well as many moderate Republicans who could no longer stomach the incumbent's disregard of public indecency law.

### Election-Audit Summary:

This code is designed to be applicable for the tallying votes of candidates, as well as vote counts for particular regions. We could easily modify the code to incorporate any additional data like precinct and non-identifying voter information. As different electoral systems gain popularity, we could also modify the code to interpret electoral results for systems like ranked-choice voting or approval voting.



