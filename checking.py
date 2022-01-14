"""
This module focuses on checking if the input
given by the user is present in our database (csv file)
that contains information of artists and paintings.
It contains two functions where the user inputs the name of
the artist or the painting to know whether they are already
present in the "artists_paintings.csv file" respectively.
"""

import pandas as pd


class Check:

    def check_artist(self, artist):
        """
        This function controls if the input given
        by the user (i.e. an artist's name') is present
        in the artist column inside the csv file.
        If you try with Claude Monet, it should
        recognize that the artist is already present
        in the original csv file.
        If you try with "Bansky" (unless you have added
        it with the "inserter function") the
        function should return that the artist is not
        present in the file.
        """
        artist = artist.lower()
        db = pd.DataFrame(pd.read_csv('artists_paintings.csv'))
        artists = db["Name"].str.lower()
        if artist in artists.values:
            return True
        return False

    def check_paintings(self, painting):
        """
        This function controls if the input given
        by the user (i.e. a painting) is present
        in the artwork column inside the csv file.
        If you try with "There is always hope", the most
        famous Bansky work (unless you have added
        it with the "inserter function") the
        function should return that the painting is not
        present in the file.
        """
        painting = painting.lower()
        db = pd.DataFrame(pd.read_csv('artists_paintings.csv'))
        paintings = db["Artwork"].str.lower()
        if painting in paintings.values:
            return True
        return False
