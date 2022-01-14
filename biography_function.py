"""
The function of the biography module
is to explain, in a more understandable way,
who was the artist with relative
most famous painting, the number of artworks that
has been made, movement, day of birth and death
that can be found into our database.
The function first checks if the input
the user inserted is present in
the database, if not the system will warn the user
and invite him to check if it is correctly written.

The user can also read and see the full biography with
the Wikipedia's link.
"""

import csv
import pandas as pd


def return_bio(Artist):
    """
    This function comes into play once the user inputs a value
    and wants to obtain as output the complete list of information that
    can be found inside the database, or when, after
    the input, the user writes the optional argument -bio.
    It recognizes the input if it is a name of an artist.
    """
    db = pd.DataFrame(pd.read_csv('artists_paintings.csv'))
    Artists = list(db["Name"])

    if Artist in Artists:
        print(db["Name"].loc[
            db["Name"].str.lower() == Artist.lower()].values[0], "is a/an", db[
                "Nationality"].loc[
                    db["Name"].str.lower() == Artist.lower()].values[
                    0], "artist who lived in these years:", db["Life"].loc[
                    db["Name"].str.lower() == Artist.lower()].values[
                    0], ". The artist painted in", db["Year"].loc[
                        db["Name"].str.lower() == Artist.lower()].values[
                            0], "the most famous painting," + "named:", db[
                                "Artwork"].loc[db["Name"].str.lower(
                                    ) == Artist.lower()].values[
                                        0], ",now displayed at the",  db[
                                            "Museum"].loc[
                                                db["Name"].str.lower() ==
            Artist.lower()].values[0], ". The painter belongs to: ", db[
                "Genre"].loc[db["Name"].str.lower() == Artist.lower()].values[
                    0], "movement(s)." +
                    " In addition to his/her" +
                    " most famous painting, she/he made", db[
                    "Paintings"].loc[
                        db["Name"].str.lower() == Artist.lower(
                            )].values[0], "artworks in total." +
                                          "Here you can find" +
                                          " the web link" +
                                          " to see" +
                                          " the complete biography: ", db[
                                          "wikipedia"].loc[db[
                                              "Name"].str.lower(
                                              ) == Artist.lower()].values[0])
    else:
        print(Artist + " seems not to be present in our database." +
                       "Are you sure that you wrote" +
                       " the name of the artist correctly?" +
                       " Use -d to check if it is already in our database," +
                       "maybe there is a spelling error in the input." +
                       " Check it and then try again, if it is not present," +
                       "use -a to insert the new artist," +
                       " thank you for your patience!")
