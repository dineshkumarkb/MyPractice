def solution(S):
    # write your code in Python 3.6
    music_types = ["mp3", "aac", "flac"]
    image_types = ["jpg", "bmp", "gif"]
    movie_types = ["mp4", "avi", "mkv"]

    music_size = 0
    movie_size = 0
    image_size = 0
    other_size = 0

    file_lst = S.split("\n")

    for i in file_lst:
        file, size = i.split()
        extension = file.split(".")[-1]
        size = size.split("b")[0]
        if extension in music_types:
            music_size += int(size)
        elif extension in image_types:
            image_size += int(size)
        elif extension in movie_types:
            movie_size += int(size)
        else:
            other_size += int(size)

    return f"""music {str(music_size)+"b"}\nimages {str(image_size)+"b"}\nmovies {str(movie_size)+"b"}\nother {str(other_size)+"b"}"""



S = """my.song.mp3 1100b
greatSong.flac 1000b
not3.txt 5b
video.mp4 200b
game.exe 100b
mov!e.mkv 10000b"""

print(solution(S))