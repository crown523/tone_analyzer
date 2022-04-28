# fangyan_tones

Repo for the study of tonal composition of chinese music, specifically rap


To setup the project, run 
```pip install .``` or ``` pip install -e .``` for an editable version

You should then be able to run chinese_to_pinyin_demo.py in scripts to pass in chinese text

After passing in the song lyrics, by inputting "Analyze" you can output the Tone table for the line endings.

In order to download wavs using download_wavs.py, you must be on a debian based os or MacOS.

On debian, install ```sudo apt install ffmpeg```.

Otherwise on MacOS, ```brew install ffmpeg```
