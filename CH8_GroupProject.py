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
        EasyFrame.__init__(self, width=300, height=300, title="Election Calculator")

        # Event handler that happens when the button is clicked.
        self.tallyBtn = self.addButton(text="Tally Votes", row=0, column=0, command=self.votes)
        self.displayBtn = self.addButton(text="Display Votes Count", row=0, column=1, command=self.voteReader)

    def votes(self):

        votingAttempts = 1  # Starts with the first vote
        recordKeeper = open("votes2020.txt", 'w')  # Initializes the file votes.txt to write data

        while (votingAttempts <= 1000):  # Makes sure that only 1,000 votes are casted

            voteDecision = random.randint(1, 3)  # Used to determine who earned a vote

            if (voteDecision == 1):  # If random number generator equals 1 Biden gets a vote
                recordKeeper.write("Biden\n")
                votingAttempts += 1

            if (voteDecision == 2):  # If random number generator equals 2 Trump gets a vote
                recordKeeper.write("Trump\n")
                votingAttempts += 1

            if (voteDecision == 3):  # If random number generator equals 3 Hinz gets a vote
                recordKeeper.write("Hinz\n")
                votingAttempts += 1

        recordKeeper.close()  # Closes the file connection to make sure there is no buffering issues

        print("\nThe file votes2020.txt has been created in the same directory as this program.")
        print("This file holds each individual vote and is ready to be used by the election.py program.")

    def voteReader(self):  # Places each vote into a list

        completeRecord = []

        votingRecord = open("votes2020.txt", 'r')  # File that has each vote recorded
        while True:
            singleVote = votingRecord.readline()  # Reads each line which has one vote
            if (singleVote == ""):  # If the end of the file is reach stop
                break
            completeRecord.append(singleVote)  # Append the voting results to he list

        voteTracker(completeRecord)  # Passes the voting list to the next function to be tallied

    def voteTracker(vote):  # Tallies each vote

        """Initializes each candidates start vote to zero"""
        BidenVote = 0
        TrumpVote = 0
        HinzVote = 0

        for index in range(len(vote)):
            if (vote[index] == "Biden\n"):  # If vote for Biden increment by 1
                BidenVote += 1
            elif (vote[index] == "Trump\n"):  # If vote for Trump increment by 1
                TrumpVote += 1
            else:  # If vote is for neither Biden or Trump, increase Hinz by 1
                HinzVote += 1

        voteDisplay(BidenVote, TrumpVote, HinzVote)  # Takes total tally to be transferred to display

    def voteDisplay(BidenTotal, TrumpTotal, HinzTotal):  # Prints how many votes each candidate received

        print("Joe Biden received a total of " + str(BidenTotal) + " votes!")
        print("Donald Trump received a total of " + str(TrumpTotal) + " votes!")
        print("Jeremy Hinz received a total of " + str(HinzTotal) + " votes!")

        voteWinner(BidenTotal, TrumpTotal, HinzTotal)

    def voteWinner(BidenWinner, TrumpWinner, HinzWinner):  # Decision Matrix on who won or tied

        """Clear Winner for the first 3"""
        if (BidenWinner > TrumpWinner and BidenWinner > HinzWinner):
            print("\nJoe Biden is the winner of the 2020 Presidential Election!")

        elif (TrumpWinner > BidenWinner and TrumpWinner > HinzWinner):
            print("\nDonald Trump is the winner of the 2020 Presidential Election!")

        elif (HinzWinner > BidenWinner and HinzWinner > TrumpWinner):
            print("\nJeremy Hinz is the winner of the 2020 Presidential Election!")

            #  If there is a 3-way tie
        elif (BidenWinner == TrumpWinner and BidenWinner == HinzWinner):
            print("\nThere is a 3-way tie for Presidential Election!")

            #  If there is a 2-way tie
        elif (BidenWinner == TrumpWinner and BidenWinner > HinzWinner):
            print("\nJoe Biden and Donald Trump tied for the Presidential Election!")

        elif (BidenWinner == HinzWinner and BidenWinner > TrumpWinner):
            print("\nJoe Biden and Jeremy Hinz tied for the Presidential Election!")

        elif (TrumpWinner == HinzWinner and TrumpWinner > BidenWinner):
            print("\nDonald Trump and Jeremy Hinz tied for the Presidential Election!")


def main():
    LectureNotes().mainloop()


if __name__ == "__main__":
    main()
