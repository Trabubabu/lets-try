# Art :art:..

ArtDatabase is a software development project that allows users to 
obtain information about famous artists and their most iconic paintings. 
In addition, it allows to get information about artists belonging to the
same artistic movement or that have the same nationality and 
constructs a short biography on the fly.

If the name of the artist or painting given as input is not present or
not available, the program asks the user whether he/she wants to insert it. 
All of this can be managed directly from the user's machine terminal.

In the following paragraphs you'll find a general overview about the original CSV file from
which we have taken the initial data, as well as a short explanation of how the software 
works and the outputs the user can obtain.

# CSV file :page_facing_up:

In order to store all the paintings and authors, we created a CSV file called
 `artists_paintings.csv`, defined by the following properties:

- Artist's name;
- Date of birth and death;
- Most famous painting;
- Year of execution;
- Painting location (Museum);
- Artistic movement;
- Nationality of the artist;
- Number of paintings the artist did in his/her life;
- Link to the artist's Wikipedia page.

The original file contains 49 rows (corresponding to 49 different artists), but this 
structure can be changed by the user since there is a function that allows him/her to
add rows by simply inserting all the required data described above.

All the information is needed by the software to work properly and to perform the functions
we created.

# How to start :man_technologist:

The first thing to do in order to develop the main functionalities just described
is to clone the remote directory. 

To do this, the user can type:

`git clone https://github.com/Annanardo/Art/tree/main `

This will automatically download all the files the user needs to run the program.

# Functionalities :gear:

In order to develop a suitable structure for our project according to the intended goals,
we created 4 main functions and stored them into different modules:

-  `add_element` function;
-  `check_artist` and  `check_painting` functions;
-  `return_bio` function;
-  `similarities` function.

All these functions are called by argparse from the `main.py` module by the corresponding
optional arguments.

This means that if the user wants to get some insights from our functions, he/she
doesn't need to point to the specific module that contains the function, but in general 
it's enough to type:

```bash
python main.py "name of the artist/painting" -optional argument
```

The name of the artist or painting is indeed a positional argument that should always 
be included. 

No optional argument is required if the user only wants to know if the artist
is present in our database.. 


For example, if we want to know if Claude Monet is present, we only neeed to write:

```bash
python main.py "Claude Monet"
```

And the output will be:

```bash
Claude Monet is the artist of Impression, Sunrise
```

Instead, for more complicated queries, we can recall some optional arguments. 

Here follow some examples:


### •	Add a new artist (-a)

```bash
python main.py "Bansky" -a
```
This argument allows to insert a new artist to the database. The `-a` activates the 
`add_element` function which first checks if the artist already exists in our database 
and then generate a sequence of questions to insert all the necessary data, such as the ones
below:

```bash
Now enter the name of his/her most famous painting -> Baloon girl
Now enter the date of birth and death of the artist-> 1973 - still alive
Now enter the year(s) of realization of the most famous artwork of the artist-> 2002
Now enter the museum and place (museum - city) where the painting is placed-> Waterloo Bridge - London
Now enter the artistic movement of the artist-> Street-art
Now enter the nationality of the artist-> British
Now enter the total number of artworks realized by the artist-> 136
Now enter the link to the wikipedia page of the artist-> https://en.wikipedia.org/wiki/Banksy
Thank you for your contribution!
```

### •	Find manually if the artist/painting is present in the database (-d)

```bash
python main.py "Claude Monet" -d
```

After being called, the argument `-d` allows to get the database relation 
between all artists and paintings as follows:

```bash
Now you can see by yourself if the artist and his/her most famous painting are present in our database!
0                    Amedeo Modigliani : Reclining Nude
1                  Vasiliy Kandinskiy : Composition VII
2                        Diego Rivera : Street in Avila
3                    Claude Monet : Impression, Sunrise
4               Rene Magritte : The Treachery of Images
5             Salvador Dali : The persistence of memory
6             Edouard Manet : The Luncheon on the Grass
7                               Andrei Rublev : Trinity
8                   Vincent van Gogh : The Starry Night
9                               Gustav Klimt : The Kiss
10    Hieronymus Bosch : The Garden of Earthly Delights
11                      Kazimir Malevich : Black Square
12                    Mikhail Vrubel : The Demon Seated
13                             Pablo Picasso : Guernica
14    Peter Paul Rubens : The Massacre of the Innocents
15    Pierre-Auguste Renoir : Bal du moulin de la Ga...
16                       Francisco Goya : The nuda maja
17    Frida Kahlo : Self-potrait with thorn necklace...
18                   El Greco : Dormition of the Virgin
19                        Albrecht Dürer : Self-potrait
20                 Alfred Sisley : Snow at Louveciennes
21    Pieter Bruegel : Landscape with the Fall of Ic...
22                         Marc Chagall : The Promenade
23               Giotto di Bondone : Ognissanti Madonna
24               Sandro Botticelli : The Birth of Venus
25         Caravaggio : The Incredulity of Saint Thomas
26                         Leonardo da Vinci : Gioconda
27                        Diego Velazquez : Las Meninas
28                                Henri Matisse : Dance
29       Jan van Eyck : Portrait of man with red turban
30                        Edgar Degas : The dance class
31    Rembrandt : Christ in the storm on the Sea of ...
32                    Titian : Assumption of the Virgin
33      Henri de Toulouse-Lautrec : At the Moulin Rouge
34                 Gustave Courbet : The Stone Breakers
35    Camille Pissarro : Boulevard Montmartre, Effet...
36              William Turner : The fighting temeraire
37                            Edvard Munch : The Scream
38    Paul Cezanne : Mont Sainte-Victoire seen from ...
39      Eugene Delacroix : La Liberté guidant le peuple
40                  Henri Rousseau : The Sleeping Gypsy
41    Georges Seurat : Un dimanche après-midi à l'Îl...
42                              Paul Klee : Red Balloon
43               Piet Mondrian : Broadway Boogie-Woogie
44                 Joan Miro : The Harlequin's Carnival
45                    Andy Warhol : The Marilyn Diptych
46                     Paul Gauguin : The Yellow Christ
47                       Raphael : The School of Athens
48                             Michelangelo : The Pietà
49                         Jackson Pollock : Blue Poles
```

It's possible to see them separated with the following commands:

- `python main.py "Impression, Sunrise" -p` which allows to see the entire list of paintings
- `python main.py "Claude Monet" -art`, to have access to the entire list of artists only.

### •	Print a bio of the artist (-bio)

The return_biography function can be used to explain the artist's life in a 
more understandable and complete way. 
The code is structured to compile together with the name and nationality some details 
that can be found in the columns of the dataset, and formulates a short biography 
of the artist. 

The function first checks if the input we inserted is present in the database;
if not the system will warn and invite you to check if you wrote it correctly. 

It's also possible to look at the complete biography using the link from Wikipedia, that 
will be printed at the end of the output, so that the user can get a complete overview of
the artist he/she is interested in.

To use the function the user should recall the optional argument -bio:

```bash
python main.py "Claude Monet" -bio
```

This will return a brief description of who the artist was, in which years has lived, 
which was his/her most famous painting and when it was painted. 
After that, you can find the museum where the artwork is displayed, the artistic movement 
the artist belongs to and the total number of artworks that have been done, 
along with the link to Wikipedia for a more detailed analysis.

Thus, the output will be:

```bash
Claude Monet is a/an French artist who lived in these years: 1840 - 1926 . 
The artist painted in 1872 the most famous painting, named: Impression, Sunrise ,
now displayed at the Musée Marmottan Monet - Paris . 
The painter belongs to:  Impressionism movement(s). 
in addition to his/her most famous painting, she/he made 73 artworks in total.
Here you can find the web link to see 
the complete biography:  http://en.wikipedia.org/wiki/Claude_Monet

```

### •	Compare different artists (-s)

The similarities function allows the user to make some comparisons between the artist 
of interest and other artists. 
The function uses the columns "Nationality", "Genre" and "Paintings" as criteria
for comparison. 

In order to use it the user should recall the optional argument `-s` in the following way:

```bash
python main.py "Claude Monet" -s
```

After having inserted the input, the user can choose between different options, according to
his/her preference to visualize similarities between artists based on:

- nationality (`nat`), 
- artistic movement (`mov`),  
- number of paintings (`nop`).

Here an example:

```bash
Do you want to see the similarities according to nationality, artistic movement or number of paintings? 
(nat, mov, nop) -> nat 
```

When the user selects `nat`, as in our example, the program will output all the artists that 
are born in the same Country of the artist he/she gave as input.

Here follows the output:

```bash
French artists are the following:
3                Claude Monet
6               Edouard Manet
15      Pierre-Auguste Renoir
28              Henri Matisse
30                Edgar Degas
33  Henri de Toulouse-Lautrec
34            Gustave Courbet
35           Camille Pissarro
38               Paul Cezanne
39           Eugene Delacroix
40             Henri Rousseau
41             Georges Seurat
46               Paul Gauguin
```

Similarly, when the user select `mov`, the program will output the list of artists
belonging to the same movement of the artist he/she gave as input.

On an other hand, if the user chooses to visualize the number of paintings by typing `nop`, 
she/he is asked if she/he wants to visualize the artists with an higher (>), smaller (<) 
or equal (==) number of artworks and, after the selection, the list of artists will be displayed.

For example:

```bash
Do you want to see the similarities according to nationality, artistic movement or number of paintings? 
(nat, mov, nop) -> nop

Do you want to search for artists that have made more (>), less (<) or the
same (==) number you provided as input? <
```

We wanted to know the artists that painted LESS artworks than Claude Monet, and so we 
inserted the `<`. 

The output will be:

```bash
The artists that painted less than 73 artworks are the following:
2       Diego Rivera         70
25        Caravaggio         55
34   Gustave Courbet         59
36    William Turner         66
37      Edvard Munch         67
38      Paul Cezanne         47
39  Eugene Delacroix         31
40    Henri Rousseau         70
41    Georges Seurat         43
48      Michelangelo         49
49   Jackson Pollock         24
```

# Contributing :handshake:

If you would like to contribute to the Artdatabase by adding more information, please feel free
to submit pull requests.
Please contact us if you wish to implement significant changes and test them before pulling.

# License :lock:

GNU License

# Authors :two_women_holding_hands::two_women_holding_hands:

- Vittoria Lazzer
- Melissa Mattioli
- Aurora Menegatto
- Anna Nardo
