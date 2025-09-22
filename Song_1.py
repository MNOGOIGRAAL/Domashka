class Song:
    def __init__(self, song_title, author, year_creation):
        self.song_title = song_title
        self.author = author
        self.year_creation = year_creation



class Album:
    def __init__(self, album_title, year_creation):
        self.album_title = album_title
        self.year_creation = year_creation
        self.list_songs = []

    def add_song(self, song):
        self.list_songs.append(song)

    def all_list_songs(self): #получение списка всех песен в альбоме
        all_list_songs = []
        for i in self.list_songs:
            all_list_songs.append(i.song_title)
        return all_list_songs

    def all_autor(self): #получение всех уникальных авторов в альбоме
        list_author = []
        for i in self.list_songs:
            if i.author not in list_author:
                list_author.append(i.author)
        return list_author

    def find_song(self, name): #поиск песни
        for i in self.list_songs:
            if i.song_title == name:
                return True
        return False



class MusicLibrary:
    def __init__(self):
        self.list_album = []

    def add_album(self, album): #добавление альбомов в фонотеку
        self.list_album.append(album)

    def all_song_from_all_album_autor(self, author): #получение всех уникальных песен одного автора из всех альбомов
        list_unique_songs = []
        for i in self.list_album:
            for j in i.list_songs:
                if j.author == author and j.song_title not in list_unique_songs:
                    list_unique_songs.append(j.song_title)
        return list_unique_songs

    def song_from_all_albums(self):
        repository = []
        reference_list = set()

        for i in self.list_album[0].list_songs:
            repository.append(i.song_title)

        for i in self.list_album[1:]:
            for j in i.list_songs:
                if j.song_title in repository:
                    reference_list.add(j.song_title)
                elif j.song_title not in repository:
                    repository.append(j.song_title)

        return list(reference_list)


song_1 = Song("Песня без слов", "Виктор Цой", "1989")
song_2 = Song("Пачка сигарет", "Виктор Цой", "1989")
song_3 = Song("Back in Black", "AC/DC", "1980")
song_4 = Song("Кто ходит в гости по утрам", "Винни_пух", "1969")
song_5 = Song("Thunderstruck", "AC/DC", "1990")
all_song = [song_1, song_2, song_3, song_4, song_5]

album_1 = Album("Мой 1 альбом", "2001")
album_1.add_song(song_1)
album_1.add_song(song_2)
album_1.add_song(song_3)
album_1.add_song(song_4)
album_1.add_song(song_5)

album_2 = Album("Мой 2 альбом", "2002")
album_2.add_song(song_2)
#album_2.add_song(song_3)
album_2.add_song(song_5)

album_3 = Album("Мой 3 альбом", "2003")
#album_3.add_song(song_1)
album_3.add_song(song_2)
#album_3.add_song(song_3)

music_library = MusicLibrary()
music_library.add_album(album_1)
music_library.add_album(album_2)
music_library.add_album(album_3)
#print(music_library.all_song_from_all_album_autor("Виктор Цой"))
#print(f"Песня которая содежится во всех альбомах: \n{music_library.song_from_all_albums()}")
print(music_library.song_from_all_albums())

#print(f"Получение списка всех песен в альбоме 'Мой 1 альбом':\n{album_1.all_list_songs()}")
#print(album_1.all_autor())
#print(album_1.find_song("Пачка сигарет"))

