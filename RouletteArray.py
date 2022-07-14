class RA:
    def __init__(self, name):
        self.name = name
        #array designed to have 3 rows with 10 entries including zero
        #in order to match the roulette table design
        #so that complex bets are intuititivly calculable
        self.array = [[0,6,9,12,15,18,21,24,30,33,36],[0,2,5,8,11,14,17,20,23,26,29,32,35],[0,1,4,7,10,13,16,19,22,25,28,31,34]]


    def returnProb(self, entry):
        print("returnProb in class RA activated: best solution would be posted")
        #prelimenary function whole function will be commented out and replaced with more complex calculations
    def tally(self, entry):
        print("tally in class RA has been activated: tally the entry")

