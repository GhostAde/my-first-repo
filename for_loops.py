playlist_length = int(input("How many songs would you like to add to your playlist? "))
song_durations = []
for i in range(playlist_length):
    duration = float(input(f"Enter the duration of song {i + 1} in minutes: "))
    song_durations.append(duration)
    print("Song durations:", song_durations)