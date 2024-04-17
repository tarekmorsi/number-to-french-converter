# number-to-french-converter

Number can be hard to write in French.

[https://fr.wikipedia.org/wiki/Nombres_en_français](https://fr.wikipedia.org/wiki/Nombres_en_fran%C3%A7ais)

This Python program converts numbers into their French word equivalents. It reads a list of numbers from an input file, converts each number to French, and writes the results to an output file.

### Requirements

> Python 3.x

### Setup

Clone this repository and navigate into the project directory and run the program using the following command:

> python main.py

This will read the numbers from `input.txt`, convert them into French.

### Input File

Replace the contents of `input.txt` and follow the following format:

>[0, 1, 5, 10, 11, 15]

Ensure that the numbers are formatted correctly and saved in the `input.txt` file before running the program.

### Output File

The converted numbers will be stored in `output.txt`. Each French number representation will be on a new line corresponding to the order of numbers in `input.txt`.

### Example

If `input.txt` contains:
> [0, 1, 2]

After running the program, `output.txt` will contain:
> zéro, un, deux

------------------

### T**he units**

> less than 16 follow no rules but each has a specific name."zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"(from 0 to 16)
> 

### T**he tens**

> as French up to 60, or using Belgium-French (septante, huitante, nonante), up to 90, follow the same pattern :
  - "dix", 
  - "vingt", 
  - "trente", 
  - "quarante", 
  - "cinquante", 
  - "soixante", 
  - "septante", 
  - "huitante", 
  - "nonante"(from 10 to 90)"huitante" could also be "octante".
> 

> In French from France, the pattern change at 70:
  - 70 = 60 + 10 = "soixante-dix"
  - 80 = 4 * 20 = "quatre-vingts"
  - 90 = 4 * 20 + 10 = "quatre-vingt-dix" (because why not!)
> 

### N**umbers from 22 to 29, then 32 to 39 ...**

> The rule is easy:
  **-** 22 = 20 + 2 = "vingt-deux", 
with a dash in between From 17 to 19, it follows this rule 
  **-** 17 = 10 + 7 = "dix-sept"
> 

### N**umbers ending with 1:**

> The rule is the same as above, but with "-et-" which means "and" instead of "-":
  **-** 21 = "vingt-et-un"
Before 1990, the writing was "vingt et un" but since [the 1990 simplification reform](https://fr.wiktionary.org/wiki/Annexe:Rectifications_orthographiques_du_fran%C3%A7ais_en_1990#Num%C3%A9raux_compos%C3%A9s), all words used for numbers are joined-up with dashes.
> 

### N**umbers after 70 and 90:**

> **-** 74 = 60 + 14 = "soixante-quatorze"
 **-**  77 = 60 + 17 = 60 + 10 + 7 = "soixante-dix-sept"
 **-**  95 = 4   * 20 + 15 = "quatre-vingt-quinze"
 **-**  99 = 4 * 20 + 10 + 9 = "quatre-vingt-dix-neuf"
> 

> ***plurals of "quatre-vingt":** 
  - ****80 : 4 * 20 = ****"quatre-vingt**s**" → means 4 times 20 so 20 is plural, thus "vingt**s**" ends with an "s". 
**But** when it is not the ending of the word, the plural form disappear:
  **-** 82 = 4 * 4 +2 =  "quatre-vingt-deux", without an "s" at "vingt".*
> 

### **71, 81, 91**

> For some unknown reasons, 71 use an "-et-", 81 and 91 use a dash.
  **-** 71 = 60 + 11 = "soixante-et-onze"
  **-** 81 = 4 * 20 + 1 = "quatre-vingt-un"
  **-** 91 = 4 * 20 + 11 = "quatre-vingt-onze"
> 

### **100 and more**

> One hundred is "cent". 
One thousand is "mille". 
The rule is joining this and the rest with a dash:
  **-** 130 = 100 + 30 = "cent-trente"
  **-** 1110 = 1000 + 1000 + 10 = "mille-cent-dix"
> 

> **plurals of "cent" and "mille:**
Like 80, 100 and 1000 can be plural if it ends a word and then takes an S: "cents", "milles"
  **-** 200 = 2 * 100 = "deux-cents"
  **-** 3 000 = 3 * 1000 = "trois-milles"

When "cent" or "mille" is not ending the word, then it is not plural:
  **-** 252 = 2 * 100 + 52 = "deux-cent-cinquante-deux"
  **-** 2045 = 2 * 1000 + 45 = "deux-mille-quarante-cinq" 
  **-** 200000 = 2 * 100 * 1000 = "deux-cent-milles", without S at "cents", but with S at "milles"
  **-** 180000 = (100 + 4 * 20) * 1000 = "cent-quatre-vingt-milles", without S at "vingt", but with S at "milles"
>
