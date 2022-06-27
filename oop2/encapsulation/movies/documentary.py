from movie_protected import Movie

class Documentary(Movie):
    def __init__(self) -> None:
        super().__init__()
        self.channel = None

    def add_channel(self,ch:str):
        self.channel = ch