"""
The function of the inserter module
allows to append new artists with relative
most famous painting into our database.
The function first checks if the input
the user wants to insert is already present in
the database, if not it asks if the inserted
value is the name of an artist
or painting.
After that it requires to add all the
other additional information, to generate
a list of 10 items.
Finally the list is inserted in a new
row becoming part
of our database.
"""

import csv
import pandas as pd
from checking import Check
from csv import writer


def add_element(a_or_p, response=""):

    """
    This function comes into play once the user inputs a value
    that is not inside the database, or when, after
    the input, the user writes the optional argument -a.,,
    It asks if the input is a name of an artist or a painting,
    then it asks for the remaining values to insert in all the 10 columns
    of the database.
    """
    db = pd.DataFrame(pd.read_csv('artists_paintings.csv'))

    if Check().check_artist(a_or_p):
        return print("Sorry, but " + a_or_p + " is already present " +
                     "in the database, thank you anyway")
    elif Check().check_paintings(a_or_p):
        return print("Sorry, but " + a_or_p + " is already " +
                     "present in the database. {} is a painting of {}."
                     .format(a_or_p, db["Name"].loc[
                         db["Artwork"].str.lower() == a_or_p.lower()]
                             .values[0]))

    else:
        if response == "a":
            name1 = "a"
            name2 = "Monet's painting"
        elif response == "p":
            name1 = "p"
            name2 = "Monet"
        else:
            name1 = input(
                "Is he/she an artist or is it a painting (a or p) -> ")

        if name1 == "a":
            if response == "":
                name2 = input(
                    "Now enter the name of his/her most famous painting -> ")
                while(name2 == ""):
                    name2 = input("You can't enter nothing... " +
                                  "so please... put anything -> ")
            life = input(
                "Now enter the date of birth and death of the artist->")
            while(life == ""):
                life = input(
                    "You can't enter nothing..." + "please put anything ->")
            year = input(
                "Now enter the year(s) of realization " +
                "of the most famous artwork of the artist->")
            while(year == ""):
                year = input(
                    "You can't enter nothing..." + "please put anything ->")
            museum = input(
               "Now enter the museum and place (museum - city) " +
               "where the painting is placed->")
            while(museum == ""):
                museum = input(
                    "You can't enter nothing..." + "please put anything ->")
            genre = input(
               "Now enter the artistic movement of the artist->")
            while(genre == ""):
                genre = input(
                    "You can't enter nothing..." + "please put anything ->")
            nationality = input(
                "Now enter the nationality of the artist->")
            while(nationality == ""):
                nationality = input(
                    "You can't enter nothing..." + "please put anything ->")
            paintings = input(
                "Now enter the total number of artworks " +
                "realized by the artist->")
            while(paintings == ""):
                paintings = input(
                    "You can't enter nothing..." + "please put anything ->")
            wiki = input(
                "Now enter the link to the wikipedia page of the artist->")
            while(wiki == ""):
                wiki = input(
                    "You can't enter nothing..." + "please put anything ->")

            with open(r'artists_paintings.csv', 'a') as write_obj:
                writer = csv.writer(write_obj)
                row = len(db)
                write_obj.write("\n")
                writer.writerow([row, a_or_p, life, name2, year,
                                 museum, genre, nationality, paintings, wiki])
                write_obj.close()
            return print("Thank you for your contribution!")

        elif name1 == "p":
            if response == "":
                name2 = input("Now enter the name of the artist -> ")
                while(name2 == ""):
                    name2 = input("You can't enter nothing..." +
                                  "so please... put anything -> ")
            life = input(
                "Now enter the date of birth and death of the artist->")
            while(life == ""):
                life = input(
                    "You can't enter nothing..." + "please put anything ->")
            artwork = input(
                "Now enter the the most famous artwork of the artist->")
            while(artwork == ""):
                artwork = input(
                    "You can't enter nothing..." + "please put anything ->")
            year = input(
                "Now enter the year(s) of realization of " +
                "the most famous artwork of the artist->")
            while(year == ""):
                year = input(
                    "You can't enter nothing..." + "please put anything ->")
            museum = input(
                "Now enter the museum and place (museum, city) " +
                "where the painting is placed->")
            while(museum == ""):
                museum = input(
                    "You can't enter nothing..." + "please put anything ->")
            genre = input("Now enter the artistic movement of the artist->")
            while(genre == ""):
                genre = input(
                    "You can't enter nothing..." + "please put anything ->")
            nationality = input("Now enter the nationality of the artist->")
            while(nationality == ""):
                nationality = input(
                    "You can't enter nothing..." + "please put anything ->")
            paintings = input(
                "Now enter the total number of artworks " +
                "realized by the artist->")
            while(paintings == ""):
                paintings = input(
                    "You can't enter nothing..." + "please put anything ->")
            wiki = input(
                "Now enter the link to the wikipedia page of the artist->")
            while(wiki == ""):
                wiki = input(
                    "You can't enter nothing..." + "please put anything ->")

            with open(r'artists_paintings.csv', 'a') as write_obj:
                writer = csv.writer(write_obj)
                row = len(db)
                write_obj.write("\n")
                writer.writerow([row, name2, life, a_or_p, year,
                                 museum, genre, nationality, paintings, wiki])
                write_obj.close()
            return print("Thank you for your contribution!")
        else:
            return input("You need to input a or p")
