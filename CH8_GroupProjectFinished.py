"""
Program: CH8_GroupProject.py
Authors: Peggy Walsh, Jason Dusek, and Jeremy Hinz
Created: November 8, 2020
Last Modified: November 8, 2020

Request: To create GUI version of the Election program

"""

from breezypythongui import EasyFrame
import random  # imports the random function to draw random numbers


class LectureNotes(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, width=300, height=150, title="Election Calculator")
        self.setResizable(False)  # Locks the window so it can't be resized

        # Event handler that happens when the button is clicked.
        self.tallyBtn = self.addButton(text="Tally Votes", row=0, column=0, command=self.votes)

        self.addLabel(text="Biden Votes", row=1, column=0)
        self.BidenVotes = self.addIntegerField(value="", row=2, column=0, sticky="W", state="readonly")

        self.addLabel(text="Trump Votes", row=1, column=1)
        self.TrumpVotes = self.addIntegerField(value="", row=2, column=1, sticky="W", state="readonly")

        self.addLabel(text="Anup Votes", row=1, column=2)
        self.AnupVotes = self.addIntegerField(value="", row=2, column=2, sticky="W", state="readonly")

        self.addLabel(text="Winner!!", row=3, column=1)
        self.ElectionWinner = self.addTextField(text="", row=4, column=1, columnspan=2, sticky="W", state="readonly")

    def votes(self):

        BidenVote = 0
        TrumpVote = 0
        AnupVote = 0

        votingAttempts = 1  # Starts with the first vote

        while (votingAttempts <= 1000):  # Makes sure that only 1,000 votes are casted

            voteDecision = random.randint(1, 3)  # Used to determine who earned a vote

            if (voteDecision == 1):  # If random number generator equals 1 Biden gets a vote
                votingAttempts += 1
                BidenVote += 1

            if (voteDecision == 2):  # If random number generator equals 2 Trump gets a vote
                votingAttempts += 1
                TrumpVote += 1

            if (voteDecision == 3):  # If random number generator equals 3 Hinz gets a vote
                votingAttempts += 1
                AnupVote += 1

        self.BidenVotes.setNumber(BidenVote)
        self.TrumpVotes.setNumber(TrumpVote)
        self.AnupVotes.setNumber(AnupVote)

        BidenWinner = "Biden"
        TrumpWinner = "Trump"
        AnupWinner = "Anup"

        threeWayTie = "Biden, Trump, and Anup"

        BidenTrumpWinner = "Biden and Trump - Tie!"
        BidenAnupWinner = "Biden and Anup - Tie!"
        TrumpAnupWinner = "Trump and Anup - Tie!"

        """Clear Winner for the first 3"""
        if (BidenVote > TrumpVote and BidenVote > AnupVote):
            self.ElectionWinner.setText(BidenWinner)

        elif (TrumpVote > BidenVote and TrumpVote > AnupVote):
            self.ElectionWinner.setText(TrumpWinner)

        elif (AnupVote > BidenVote and AnupVote > TrumpVote):
            self.ElectionWinner.setText(AnupWinner)

            #  If there is a 3-way tie
        elif (BidenVote == TrumpVote and BidenVote == AnupVote):
            self.ElectionWinner.setText(threeWayTie)

            #  If there is a 2-way tie
        elif (BidenVote == TrumpVote and BidenVote > AnupVote):
            self.ElectionWinner.setText(BidenTrumpWinner)

        elif (BidenVote == AnupVote and BidenVote > TrumpVote):
            self.ElectionWinner.setText(BidenAnupWinner)

        elif (TrumpVote == AnupVote and TrumpVote > BidenVote):
            self.ElectionWinner.setText(TrumpAnupWinner)


def main():
    LectureNotes().mainloop()


if __name__ == "__main__":
    main()
