class Movie:
    def __init__(self,title,year,genre) -> None:
        self.__title = title
        self.__year = year
        self.__genre = genre

    def __get_movie(self):
        print(f'title: {self.__title}\ngenre: {self.__genre}')

    #public สำหรับ private
    def print_detail(self):
        self.__get_movie()