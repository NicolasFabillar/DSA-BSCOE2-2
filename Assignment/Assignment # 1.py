print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}')

options = {
       'A':['    *    ','   * *   ','  *****  ',' *     * ','*       *'],
       'D':['*****  ','*    * ','*     *','*    * ','*****  '],
       'N':['*   *','**  *','* * *','*  **','*   *'],
        }

Name = "DAN"
# Number of Rows required to print the name:
for row in range(5):
    # The position of letter, is it 1st or second?
    for LetterPosition,_ in enumerate(Name):
        # Putting the preset stars in their proper position with correct order and putting space between the letters.
        print(options[Name[LetterPosition]][row] + "   ", end = "")

    # Printing the stars per row.
    print()


