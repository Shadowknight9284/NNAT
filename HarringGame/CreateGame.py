class Game():
    def __init__(self):
        self.ending = 0
        self.p1Points = 25
        self.p2Points = 25
        self.p1Wins = 0
        self.p2Wins = 0
        
    def display_info(self):
        print("Player 1 Points: " + str(self.p1Points))
        print("Player 2 Points: " + str(self.p2Points))
        print("Player 1 Wins: " + str(self.p1Wins))
        print("Player 2 Wins: " + str(self.p2Wins))
        
    def wager(self, p1Wager, p2Wager):
        if(p1Wager > self.p1Points):
            print("Player 1 does not have enough points to wager. Please try again.")
            return
        if(p2Wager > self.p2Points):
            print("Player 2 does not have enough points to wager. Please try again.")
            return
        self.p1Points -= p1Wager
        self.p2Points -= p2Wager
        if(p1Wager > p2Wager):
            self.p1Wins += 1
        elif(p1Wager < p2Wager):
            self.p2Wins += 1
        else:
            self.p1Wins += .5
            self.p2Wins += .5
            
    def check_ending(self):
        if((self.p1Wins + self.p2Wins )== 7):
            self.ending = 1
            print("Game Over")
            if(self.p1Wins > self.p2Wins):
                print("Player 1 Wins")
            elif(self.p1Wins < self.p2Wins):
                print("Player 2 Wins")
            else:
                print("Tie")
            print("Games Played: " + str(self.p1Wins + self.p2Wins))
        elif(self.p1Wins == 4):
            self.ending = 1
            print("Game Over")
            print("Player 1 Wins")
            print("Games Played: " + str(self.p1Wins + self.p2Wins))
        elif(self.p2Wins == 4):
            self.ending = 1
            print("Game Over")
            print("Player 2 Wins")
            print("Games Played: " + str(self.p1Wins + self.p2Wins))
            
    def play(self):
        while self.ending == 0:
            self.display_info()
            p1Wager = int(input("Player 1, how many points would you like to wager?"))
            while p1Wager <= 0:
                print("Please enter a positive integer.")
                p1Wager = int(input("Player 1, how many points would you like to wager?"))
            
            p2Wager = int(input("Player 2, how many points would you like to wager?"))
            while p2Wager <= 0:
                print("Please enter a positive integer.")
                p2Wager = int(input("Player 2, how many points would you like to wager?"))
            self.wager(p1Wager, p2Wager)
            self.check_ending()
