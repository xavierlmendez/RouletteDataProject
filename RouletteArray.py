class RA:
    def __init__(self):
        self.entryTally = []
        #array designed to have 3 rows with 10 entries including zero
        #in order to match the roulette table design
        #so that complex bets are intuititivly calculable
        self.array = [[0,6,9,12,15,18,21,24,30,33,36],[0,2,5,8,11,14,17,20,23,26,29,32,35],[0,1,4,7,10,13,16,19,22,25,28,31,34]]
        self.entryData = [[0],
                          [1, 'R'],[2, 'B'],[3, 'R'],[4, 'B'],[5, 'R'],[6, 'B'],[7, 'R'],[8, 'B'],[9, 'R'],
                          [10, 'B'],[11, 'B'],[12, 'R'],[13, 'B'],[14, 'R'],[15, 'B'],[16, 'R'],[17, 'B'],[18, 'R'],
                          [19, 'R'],[20, 'B'],[21, 'R'],[22, 'B'],[23, 'R'],[24, 'B'],[25, 'R'],[26, 'B'],[27, 'R'],
                          [28, 'B'],[29, 'B'],[30, 'R'],[31, 'B'],[32, 'R'],[33, 'B'],[34], 'R',[35, 'B'],[36, 'R']]

    #returns the entree with best probability (for red/black even odd only)
    def returnProb(self, entry):
        print("returnProb in class RA activated: best solution would be posted")
        print("entered entry ", + entry)
        #add entry to tally
        self.tally(self, entry)
        if( (entry%2) == 1):
            if(self.entryData.index(entry, 2)=='B'):
                print("pick even red")
            if(self.entryData.index(entry, 2)=='R'):
                print("pick even black")
        elif(entry != 0):
            if (self.entryData.index(entry, 2) == 'B'):
                print("pick odd red")
            if (self.entryData.index(entry, 2) == 'R'):
                print("pick even red")
        else:
            print('dont pick zero')


        #prelimenary function whole function will be commented out and replaced with more complex calculations
    def tally(self, entry):
        print("tally in class RA has been activated: tally the entry")
        self.entryTally.append(entry)

