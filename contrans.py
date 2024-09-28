import numpy as np
import pandas as pd
import os


class contrans:
        def __init__(self):
                self.mypassword = os.getenv('mypassword')
        """
        Initialize a contrans object, getting the mypassword from environment
        variable `mypassword`.
        """

        def get_votes(self):
                url = 'https://voteview.com/static/data/out/votes/H118_votes.csv'
        """
        Get the 118th House of Representatives' votes.

        This function will return a dataframe of the 118th House of
        Representatives' votes. The dataframe will have the following columns:
        - congress: The congress number.
        - chamber: The chamber of congress.
        - rollnumber: The vote number.
        - icpsr: The ICPSR number of the member.
        - cast_code: The code of the vote cast by the member.
        - prob: The probability of the member voting for the bill.

        Returns:
            A dataframe of the 118th House of Representatives' votes.
        """
                votes = pd.read_csv(url)
                return votes
        
        def get_ideology(self):
                url = 'https://voteview.com/static/data/out/members/H118_members.csv'
        """
        Get the 118th House of Representatives' members' ideology.

        This function will return a dataframe of the 118th House of
        Representatives' members' ideology. The dataframe will have the following columns:
        - bioname: The name of the member.
        - icpsr: The ICPSR number of the member.
        - party_code: The party of the member.
        - dw_nominate_dim1: The DW-NOMINATE score of the member.

        Returns:
            A dataframe of the 118th House of Representatives' members' ideology.
        """
                members = pd.read_csv(url)
                return members