# this sets your path correctly so the imports work
import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))

from api import QuorumAPI
import json
# this library will let us turn dictionaries into csv files
import csv


# first, we subclass the QuorumAPI to support trendlines.
# to do this, we'll use the same approach as the count function
# in order to make the final API request have &trends=true
class TrendlineAPI(QuorumAPI):

    def trends(self, return_trendline=False):
        if return_trendline in [True, False]:
            self.filters["trends"] = return_trendline
        else:
            raise Exception("Must be a Boolean value!")

        return self


class TrendlineVisualizer(object):

    # Since both the api_key and username stay the same so initialize API object once
    quorum_api = TrendlineAPI(username="gwc", api_key="d3ca10586c4d9a52eb8f6910a5a8876461bfba63")

    # Let's write a helper function that takes in a list of (date, count)
    # key-value pair objects and produces a csv file of the following format:
    # label,date,count
    # my label,20170101,19
    # my label,20170201,5
    # ...etc.
    # We can use the csv class that we imported above.
    def save_csv(self, results):
        # TODO: save the results as "data.csv"
        with open("data.csv", "w") as f:
            f.write("label,date,count\n")
            for result in results:
                if int(result["date"][:4])>=1995:
                    f.write("%s,%s,%s\n" % ("Mental Health", result["date"], result["count"]))

    def get_topic_mentions_count(self, search_term):

        # TODO: use the QuorumAPI to down to the data you're looking for.
        # Be sure to set it so that it will show trends.
        results = (self.quorum_api.set_endpoint("document").filter(advanced_search=search_term).trends(True).GET())
        results = json.loads(results)

        self.save_csv(results)
        #TODO: get the data set!

        #TODO: Convert the results into a CSV using save_csv.

# Create a CSV given the search term!
trends = TrendlineVisualizer()
trends.get_topic_mentions_count(search_term="mental health")
