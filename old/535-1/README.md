CS 535: Pattern Recognition
Professor Vladimir Pavlovic
Sakib Jalal sfj19 158005883
Mini-Project 1 -- Fall 2017

Problem 1
To run the project, put "p1.py" and "marketing.data" to the same
directory and run `python p1.py`. The code at the bottom is what
I modified to check out some examples of association rules found
by the Apriori algorithm. "real_marketing.info" contains the set
of new mappings of dummy variables to distinct number ranges. This
will help make sense of the association rules that the script finds.

Problem 2
To run the project, move "p2.py" to this dir and run `python run.py`
dir: scikit-learn/doc/tutorial/text_analytics/data/twenty_newsgroups/

There are three sections of code, 2.2, 2.3.2, and 2.3.3, each of which
run algorithms that output 3 graphs each, one for each vector space
representation of the documents in the 20 newsgroups dataset.

Feel free to comment segments out at your discretion. Also, in the
section of code for Problem 2.3.3, feel free to modify the variable
`ONE_OUT_OF` to what you see fit - it represents a sampling rate of
queries to judge the newsgroup vectors against, and the graphs in
my report were obtained when it was set to 100 (sampling rate of
1/100). This is because it took exorbitant amounts of time to compute.
