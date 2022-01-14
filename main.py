"""
This is the main file where we created
the interaction between the user and the
database of artists.
We used the argparse module to configure
all the positional and optional arguments.
Depending on the arguments given,
the program leads the user to a series of steps
to either check the presence of an artist or painting
inside the database and/or add them to it.
There is also the possibility to check out
the association between artists and paintings,
the list of paintings and the list of artists.
"""

from inserter import add_element
from checking import Check
from similarities import similarities
from biography_function import return_bio
import argparse
import pandas as pd

db = pd.DataFrame(pd.read_csv('artists_paintings.csv'))
parser = argparse.ArgumentParser(description='This program will' +
                                             ' check if the name you put is' +
                                             ' inside our database of ' +
                                             'artists and their ' +
                                             'most famous artwork.' +
                                             ' If the names have ' +
                                             'more than one space, ' +
                                             'wrap them ' +
                                             'around quotes ("").')
group = parser.add_mutually_exclusive_group()
parser.add_argument("name",
                    help="input the name of a known artist or painting")
group.add_argument("-a", "--add", action="store_true",
                   help="add a new artist or painting")
group.add_argument("-d", "--database", action="store_true",
                   help="show artist and relative painting")
group.add_argument("-p", "--paintings", action="store_true",
                   help="show the list of paintings")
group.add_argument("-art", "--artist", action="store_true",
                   help="show the list of artists")
group.add_argument("-s", "--similarities", action="store_true",
                   help="show similar artits by nat/mov/nop")
group.add_argument("-bio", "--biography", action="store_true",
                   help="entire biography of the artist")
args = parser.parse_args()
answer = args.name

check = Check()

if args.paintings:
    print("Now you can see by yourself if the painting " +
          "is present in our database!")
    print(db["Artwork"])
elif args.artist:
    print("Now you can see by yourself if the painting " +
          "is present in our database!")
    print(db["Name"])

if args.similarities:
    response2 = input("Do you want to see the similarities according " +
                      "to nationality, artistic movement or number " +
                      "of paintings? (nat, mov, nop) -> ")
    if response2 == "nat":
        similarities("Nationality", db.loc[
            db['Name'] == answer, 'Nationality'].iloc[0])
    elif response2 == "mov":
        similarities("Genre", db.loc[db['Name'] == answer, 'Genre'].iloc[0])
    else:
        similarities("Paintings", int(db.loc[
            db['Name'] == answer, 'Paintings'].iloc[0]))

elif args.biography:
    return_bio(answer)

elif args.database:
    print("Now you can see by yourself if the artist and his/her " +
          "most famous painting are present in our database!")
    print(db["Name"] + " : " + db["Artwork"])
else:
    if args.add:
        add_element(answer)
    elif check.check_paintings(answer):
        print("The artist of", db["Artwork"]
              .loc[db["Artwork"].str.lower() == answer.lower()].values[0],
              "is", db["Name"].loc[db["Artwork"].str.lower() ==
              answer.lower()].values[0])
    elif check.check_artist(answer):
        print(db["Name"].loc[db["Name"].str.lower() == answer.lower()]
              .values[0], "is the artist of",
              db["Artwork"].loc[db["Name"].str.lower() ==
              answer.lower()].values[0])
    else:
        response = input(answer + " is not present in our database. Are you " +
                         "sure that you wrote it correctly " +
                         "(use -d to check if it is " +
                         "already in our database)?(y or n) -> ")
        if response == "y":
            response1 = input(
                "Great! Do you want to add she/her/it? (y or n) -> ")
            if response1 == "y":
                add_element(answer)
            else:
                print("Thank you anyway")
        else:
            print("Use -d to check if it is already in our database, " +
                  "maybe there is a spelling error in the input. " +
                  "Then try again, thank you for your patiance!")
