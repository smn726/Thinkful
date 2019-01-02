# Goal 1: Describe your dataset

    # This data set consists of Video game sales from Vgcharts and corresponding ratings from Metacritic. VGCharts is a video
    # game sales tracking website that provides weekly sales figures of console software and hardware by region. Metacritic
    # is a website that aggregates reviews of media products. For each product, the scores from each review are averaged.

    # This dataset comes from kaggle.com, an online community of data scientists and machine learners that allow users to
    # upload data sets for public use.

    # This dataset is interesting in that it contains sales data for over 13,000 game titles, by region and globally, as well
    # as basic information such as year of release, platform, genre, developer and publisher. The set also
    # contains review score data from metacritic staff professionals and metacritic users.

# Goal 2: Ask and answer analytic questions

    # Which big publisher releases the highest rated games on average?
    # We could analyze Critic_Score, User_Score and an aggregate of the two.
    # Problem: How do we define 'Big publisher' - list of publishers with the most games released?
    # 582 unique publishers. My definition: Big publisher = 50 or more published games.

    # Which publisher has the most total global sales for all games released?
    # I will look at the total number of games sold over for each publisher and their combined Global_sales.

    # Which indie developer has released the highest rated game under their own publishing?
    # Problem: How do we define 'Indie' developer? Developers with the least games released and without external publishing.
    # We will take only those games whose developer was also it's publisher.
    # We could extract the indie developers from the list and analyze Critic_score, User_score and an aggregate of the two.

# Goal 3: Propose further research

    # Some questions one might ask are:
    # Do any developers/publishers with multiple released games show better sales in any specific markets consistently?
    # Could you predict the success rate (sales/review score) of a future game title by a specific developer/publisher? released
    # in a specific region? released on a specific platform?