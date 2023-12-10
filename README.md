# hottp-pbb
Code and data to produce a text file of UBS's HOTTP (Hebrew OT Text Project) volumes compatible for Logos Personal Book Builder.

# Code

Code is a simple Python script that uses `python-docx` to create a word document based on the XML provided by UBS.

* `src/hottp2pbb.py` — Python script to convert UBS HOTTP XML to Logos Personal Book Builder format

# Data

Data created by the script is available in the `data/pbb` folder.

There are four word docs in the folder as well as one graphic. 

* `data/pbb/hottp_en.docx` — The Preliminary and Interim Report of the Hebrew Old Testament Text Project converted from XML openly licensed by UBS.
* `data/pbb/pbb_title.docx` — A title page for the PBB edition, with information from the README found in the [UBSICAP respository](https://github.com/ubsicap/ubs-open-license/tree/main/HOTTP).
* `data/pbb/ratings_en.docx` — A MSWord document created from the HTML edition of the Ratings document found in the [UBSICAP respository](https://github.com/ubsicap/ubs-open-license/tree/main/HOTTP).
* `data/pbb/factors_en.docx` — A MSWord document created from the HTML edition of the Factors document found in the [UBSICAP respository](https://github.com/ubsicap/ubs-open-license/tree/main/HOTTP).
* `data/pbb/hottp_cover.jpg` — An image of the cover of volume 1 of the Preliminary and Interim report of the HOTTP.

# License

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
