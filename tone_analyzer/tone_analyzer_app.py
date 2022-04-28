import tkinter as tk
from utils.tone_analyzer_util import load_and_convert
from utils.tone_analyzer_util import create_table


def main():
    def handle_automatic_analyze(event):
        text = lyricEntry.get("1.0", tk.END)
        print(text)

    def handle_manual_analyze(event):
        print('manual')

    window = tk.Tk()
    header = tk.Label(text="Tone Analyzer")
    header.pack()

    numVersesLabel = tk.Label(text="Number of Verses")
    numVersesEntry = tk.Entry()
    numVersesLabel.pack()
    numVersesEntry.pack()

    lyricEntryLabel = tk.Label(text="Enter Lyrics")
    lyricEntryLabel.pack()
    lyricEntry = tk.Text()
    lyricEntry.pack()

    lyricEntry.get("1.0", tk.END)

    button = tk.Button(
        text="Automatic",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
    )
    button.bind("<Button-1>", handle_automatic_analyze)
    button.pack()

    button2 = tk.Button(
        text="Manual",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
    )
    button2.bind("<Button-1>", handle_manual_analyze)
    button2.pack()

    window.mainloop()


if __name__ == "__main__":
    main()