import tkinter as tk
from utils.tone_analyzer_util import load_and_convert
from utils.tone_analyzer_util import create_table
from utils.tone_analyzer_util import separate_verses


def main():
    def handle_automatic_analyze(event):
        lyricEntryLabel = tk.Label(text="Enter Lyrics")
        lyricEntryLabel.pack()
        lyricEntry = tk.Text()
        lyricEntry.pack()

        def handle_submit(event):
            text = lyricEntry.get("1.0", tk.END)
            # print(text)
            separate_verses(text)

        submitButton = tk.Button(
            text="Analyze",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
        )
        submitButton.bind("<Button-1>", handle_submit)
        submitButton.pack()

    def handle_manual_analyze(event):
        print('manual')

    window = tk.Tk()
    header = tk.Label(text="Tone Analyzer")
    header.pack()

    numVersesLabel = tk.Label(text="Number of Verses")
    numVersesEntry = tk.Entry()
    numVersesLabel.pack()
    numVersesEntry.pack()

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