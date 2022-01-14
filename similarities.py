import pandas as pd


def similarities(column, parameter):
    """
    This function returns similarities between the
    artist given as an input and
    the other artists stored in our database.
    The code is structured in order to
    individuate similarities according to columns
    "Nationality", "Genre" and "paintings".
    The user should select the column she/he
    is interested in.
    If the user is looking for similarities according
    to the number of paintings,
    she/he is asked to specify if she/he is interested
    in more, less or equal number of artworks.
    """
    db = pd.DataFrame(pd.read_csv('artists_paintings.csv'))

    column = str(column)

    if type(parameter) == int:
        valore = str(input("Do you want to search for artists " +
                           "that have made more (>), less (<) or " +
                           "the same (==) number you provided as input?"))

        if valore == ">":
            result = db.loc[db[column] > parameter][["Name", column]]
            if len(result) > 1:
                print("The artists that painted more " +
                      "than {} artworks are the following: {}".format(
                       parameter, result))
            else:
                print("Sorry, there are no artists that painted " +
                      "more than {} artworks.".format(parameter))

        elif valore == "<":
            result = db.loc[db[column] < parameter][["Name", column]]
            if len(result) > 1:
                print("The artists that painted less " +
                      "than {} artworks are the following:{}".format(
                       parameter, result))
            else:
                print("Sorry, there are no artists that painted " +
                      "less than {} artworks. ".format(parameter))
        elif valore == "==":
            result = db.loc[db[column] == parameter][["Name", column]]
            if len(result) > 1:
                print("The artists that painted " +
                      "{} artworks are the following: {}".format(
                       parameter, result))
            elif len(result) == 1:
                print("The artist that painted " +
                      "{} artworks is the following: {}".format(
                       parameter, result))
            else:
                print("Sorry, there are no artists that " +
                      "painted {} artworks".format(parameter))
        else:
            print("You have to enter <, > or ==.")

    else:
        parameter = str(parameter)
        result = db.loc[db[column] == parameter][["Name"]]
        if column == ("Nationality"):
            if len(result) > 1:
                print("{} artists are the following:{}".format(
                       parameter, result))
            else:
                print("Sorry, there are not {} artists ".format(parameter))
        else:
            if len(result) > 1:
                print("Artists belonging to "
                      "{} movement(s) are the following: {}".format(
                       parameter, result))
            else:
                print("Sorry, there are not artists " +
                      "belonging to {} movement(s) ".format(parameter))
