import numpy as np
import pandas as pd
import os


class contrans:
    def __init__(self):
        """
        Initialize a contrans object.  This object provides access to several
        functions that are useful for accessing data related to the US Congress.

        
        """
        self.mypassword = os.getenv('mypassword')

    def get_votes(self):
        """
        Download vote data for the 118th US House of Representatives from 
        Voteview.com and return it as a pandas DataFrame.

        Returns
        -------
        votes : pandas DataFrame
            A DataFrame containing vote data for the 118th US House of 
            Representatives.  The columns are:
            
            * ``congress``: The number of the congress (e.g. 118)
            - ``chamber``: The chamber of Congress (e.g. House or Senate)
            - ``legislator``: The last name of the legislator
            - ``leg_id``: A unique identifier for the legislator
            - ``vote_id``: A unique identifier for the vote
            - ``issue_id``: A unique identifier for the issue
            - ``vote_date``: The date of the vote (in the format 
                ``YYYY-MM-DD``)
            - ``vote_desc``: A description of the vote
            - ``vote_category``: A categorization of the vote (e.g. 
                ``Democrat``, ``Republican``, ``Independent``)
            - ``ayes``: The number of ``aye`` votes
            - ``nays``: The number of ``nay`` votes
            - ``total_votes``: The total number of votes cast
            - ``dems_in_favor``: The number of Democratic votes in favor
            - ``repubs_in_favor``: The number of Republican votes in favor
            - ``independents_in_favor``: The number of Independent votes in 
                favor
            - ``democrats``: The number of Democratic votes
            - ``republicans``: The number of Republican votes
            - ``independents``: The number of Independent votes
            - ``democratic_share``: The proportion of Democratic votes
            - ``republican_share``: The proportion of Republican votes
            - ``independent_share``: The proportion of Independent votes
            - ``bipartisan_vote``: A boolean indicating whether the vote was 
                bipartisan (i.e. whether members of more than one party voted 
                in favor)
        """
        url = 'https://voteview.com/static/data/out/votes/H118_votes.csv'
        votes = pd.read_csv(url)
        return votes
    def get_ideology(self):
        """
        Download ideology data for members of the 118th US House of 
        Representatives from Voteview.com and return it as a pandas DataFrame.

        Returns
        -------
        members : pandas DataFrame
            A DataFrame containing ideology data for the 118th US House of 
            Representatives.  The columns are:
            
            * ``leg_id``: A unique identifier for the legislator
            - ``chamber``: The chamber of Congress (e.g. House or Senate)
            - ``congress``: The number of the congress (e.g. 118)
            - ``state_abbrev``: The two letter abbreviation for the state
            - ``district``: The number of the district (e.g. 1, 2, 3, etc.)
            - ``party_code``: A code indicating the party affiliation of the 
                legislator (e.g. 100 for Democrats, 200 for Republicans, 
                328 for Independents)
            - ``party``: A string indicating the party affiliation of the 
                legislator (e.g. 'Democrat', 'Republican', 'Independent')
            - ``name``: The full name of the legislator
            - ``nominate_dim1``: The first dimension of the Nominate score
            - ``nominate_dim2``: The second dimension of the Nominate score
            - ``nominate_dim1_prev_term``: The first dimension of the Nominate 
                score for the previous term
            - ``nominate_dim2_prev_term``: The second dimension of the Nominate 
                score for the previous term
        """
        url = 'https://voteview.com/static/data/out/votes/H118_votes.csv'
        members = pd.read_csv(url)
        return members
    
    
        
        