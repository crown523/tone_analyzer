import tkinter as tk
from utils.tone_analyzer_util import manual_load_and_convert
from utils.tone_analyzer_util import load_and_convert
from utils.tone_analyzer_util import create_table
from utils.tone_analyzer_util import separate_verses

# manual analysis variables
verses = []
cur_step = 0
num_verses = 0

def main():
    window = tk.Tk()
    header = tk.Label(text="Tone Analyzer")
    header.pack()

    main_frame = tk.Frame()

    # widget defs for automatic analyze
    automatic_analysis_frame = tk.Frame()

    def go_home():
        automatic_analysis_frame.pack_forget()
        song_info_frame.pack_forget()
        main_frame.pack()

    homeButton = tk.Button(
        master=automatic_analysis_frame,
        text="Home",
        width=25,
        height=5,
        bg="blue",
        fg="black",
        command=lambda: go_home()
    )
    homeButton.pack()

    lyricEntryLabel = tk.Label(master=automatic_analysis_frame, text="Enter Lyrics")
    lyricEntryLabel.pack()
    lyricEntry = tk.Text(master=automatic_analysis_frame)
    lyricEntry.pack()

    song_info_frame = tk.Frame()

    artistNameLabel = tk.Label(master=song_info_frame, text="Artist Name")
    artistNameEntry = tk.Entry(master=song_info_frame)
    artistNameLabel.pack()
    artistNameEntry.pack()

    songNameLabel = tk.Label(master=song_info_frame, text="Song Title")
    songNameEntry = tk.Entry(master=song_info_frame)
    songNameLabel.pack()
    songNameEntry.pack()

    songYearLabel = tk.Label(master=song_info_frame, text="Year")
    songYearEntry = tk.Entry(master=song_info_frame)
    songYearLabel.pack()
    songYearEntry.pack()

    song_info_frame.pack()
    song_info_frame.pack_forget()

    def handle_submit():
        lyrics = lyricEntry.get("1.0", tk.END)
        lyricEntry.delete("1.0", tk.END)
        # print(text)
        artist = artistNameEntry.get()
        artistNameEntry.delete(0, tk.END)
        song = songNameEntry.get()
        songNameEntry.delete(0, tk.END)
        year = songYearEntry.get()
        songYearEntry.delete(0, tk.END)

        verses = separate_verses(lyrics)
        load_and_convert(verses, (artist, song, year))

        # should clear the text boxes after

    submitButton = tk.Button(
        master=automatic_analysis_frame,
        text="Analyze",
        width=25,
        height=5,
        bg="blue",
        fg="black",
        command=lambda: handle_submit()
    )
    # submitButton.bind("<Button-1>", handle_submit())
    submitButton.pack()

    automatic_analysis_frame.pack()
    automatic_analysis_frame.pack_forget()

    # manual analysis widget defs
    manual_analysis_frame = tk.Frame()

    numVersesLabel = tk.Label(master=manual_analysis_frame, text="Number of Verses")
    numVersesEntry = tk.Entry(master=manual_analysis_frame)
    numVersesLabel.pack()
    numVersesEntry.pack()

    verse_entry_frame = tk.Frame(master=manual_analysis_frame)

    lyricEntryLabel2 = tk.Label(master=verse_entry_frame, text="Enter Lyrics")
    lyricEntryLabel2.pack()
    lyricEntry2 = tk.Text(master=verse_entry_frame)
    lyricEntry2.pack()

    verse_entry_frame.pack()
    verse_entry_frame.pack_forget()    

    def go_next():
        print('gg')
        global cur_step
        global num_verses
        num_verses += 1

        print(cur_step)
        
        nextButton.pack_forget()
        if cur_step == 0:
            num_verses = int(numVersesEntry.get())
            numVersesEntry.delete(0, tk.END)
            numVersesLabel.pack_forget()
            numVersesEntry.pack_forget()
            verse_entry_frame.pack()
            cur_step += 1
        else:
            if cur_step == num_verses - 1:
                lyricEntryLabel2.config(text="Enter Hook")
                nextButton['text'] = 'Analyze'
                song_info_frame.pack()
                lyrics = lyricEntry2.get("1.0", tk.END)
                lyricEntry2.delete("1.0", tk.END)
                lines = lyrics.splitlines()
                verses.append(lines)
                print(verses)
            elif cur_step == num_verses:
                # pass to analyzer
                artist = artistNameEntry.get()
                artistNameEntry.delete(0, tk.END)
                song = songNameEntry.get()
                songNameEntry.delete(0, tk.END)
                year = songYearEntry.get()
                songYearEntry.delete(0, tk.END)

                load_and_convert(verses, (artist, song, year))
                manual_analysis_frame.pack_forget()
                song_info_frame.pack_forget()
                main_frame.pack()
            else:
                lyrics = lyricEntry2.get("1.0", tk.END)
                lyricEntry2.delete("1.0", tk.END)
                lines = lyrics.splitlines()
                verses.append(lines)
                print(verses)
            cur_step += 1
        nextButton.pack()

    nextButton = tk.Button(
        master=manual_analysis_frame,
        text="Next",
        width=25,
        height=5,
        bg="blue",
        fg="black",
        command=lambda: go_next()
    )
    nextButton.pack()

    manual_analysis_frame.pack()
    manual_analysis_frame.pack_forget()

    # starting screen widget defs

    def handle_automatic_analyze():
        automatic_analysis_frame.pack()
        song_info_frame.pack()
        main_frame.pack_forget()

    button = tk.Button(
        master=main_frame,
        text="Automatic",
        width=25,
        height=5,
        bg="blue",
        fg="black",
        command=lambda: handle_automatic_analyze()
    )
    button.pack()

    def handle_manual_analyze():
        manual_analysis_frame.pack()
        main_frame.pack_forget()

    button2 = tk.Button(
        master=main_frame,
        text="Manual",
        width=25,
        height=5,
        bg="blue",
        fg="black",
        command=lambda: handle_manual_analyze()
    )
    button2.pack()

    main_frame.pack()

    window.mainloop()


if __name__ == "__main__":
    main()