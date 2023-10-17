class Player(object):
    def __init__(self, name):
        self.name = name
        self.games = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.gamesFor = 0
        self.gamesAgainst = 0
        self.gamesDiff = 0
        self.total = 0
        self.form = ""

    # setters
    def setName(self, name): self.name = name
    def setGames(self, games): self.games = games
    def setWins(self, wins): self.wins = wins
    def setLosses(self, losses): self.losses = losses
    def setDraws(self, draws): self.draws = draws
    def setGamesFor(self, gamesFor): self.gamesFor = gamesFor
    def setGamesAgainst(self, gamesAgainst): self.gamesAgainst = gamesAgainst
    def setGamesDiff(self, gamesDiff): self.gamesDiff = gamesDiff
    def setTotal(self, total): self.total = total
    def setForm(self, form): self.form = form

    # getters
    def getName(self, name): return self.name 
    def getGames(self, games): return self.games 
    def getWins(self, wins): return self.wins 
    def getLosses(self, losses): return self.losses 
    def getDraws(self, draws): return self.draws 
    def getGamesFor(self, gamesFor): return self.gamesFor 
    def getGamesAgainst(self, gamesAgainst): return self.gamesAgainst 
    def getGamesDiff(self, gamesDiff): return self.gamesDiff 
    def getTotal(self, total): return self.total 
    def getForm(self, form): return self.form
