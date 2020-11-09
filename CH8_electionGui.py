"""
Program: votesgui.py
Author: Jason Dusek
Date:   11/08/2020

randomly chooses a candidate and writes to the file... 1000 times. 

inputs? none

outputs = file named votes.txt with 1000 "votes" which are a random selection
of the 3 candidate's last names. 

imports votes.txt reads the file, creates a dictionary with candidate and
vote count, displays the votes for each candidate, and declares a winner based
on the most votes received.

inputs = votes.txt file, 

outputs = votes dictionary with vote count as the key, printed dictionary
showing vote counts, declared winner printd based on most votes.

"""

from breezypythongui import *

import random

class Election(EasyFrame):

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Election", width = 320,
                           height = 320)
        self.setBackground("#989ca3")

        self.addButton(text="Get Votes",row = 0, column = 0,
                       columnspan = 2, command =self.votes)
        self.addButton(text="Count Votes", row = 1, column = 0,
                       columnspan = 2, command = self.read_votes)
        self.addButton(text="Declare Winner", row =3, column = 0,
                       columnspan = 2, command = self.declare_winner)

        self.outputArea = self.addTextArea("", row = 5, column = 0,
                         columnspan = 2, width = 3, height = 5)
        self.addLabel(text="Winner: ", row = 4, column = 0)
        self.winner = self.addTextField(text="", row = 4, column = 1)

    def votes(self):
        candidates = ['Biden ','Dusek ','Trump ']
        f = open("votes.txt",'w') #create file for election.py
        i = 0
        while i < 1000:
            f.write(random.choice(candidates))
            i += 1
        f.close()

    def read_votes(self):
        f = open("votes.txt",'r') #open file from votes.py
        votes = {}
        for candidate in f.read().split():
            if candidate not in votes:
                votes[candidate] = 1
            else:
                votes[candidate] += 1
        f.close();
        for candidate in votes:
            self.outputArea.setText(votes)
            #self.outputArea.setText("{0} {1} ".format(candidate, votes[candidate]))
        return votes
    
    def declare_winner(self):
        
        votes = self.read_votes()
        v = list(votes.values())
        k = list(votes.keys())
        winText1 = (k[v.index(max(v))])
        winText = (winText1 + " is the Winner!")
        self.winner.setText(winText)

def main():
    """Instantiate and pop up the window."""
    Election().mainloop()

if __name__ == "__main__":
    main()
