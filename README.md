# hottp-pbb
Code and data to produce a `*.docx` file of UBS's HOTTP (Hebrew OT Text Project) volumes compatible for Logos Personal Book Builder.

# Code

Code is a simple Python script that uses `python-docx` to create a word document based on the XML provided by UBS.

* `src/hottp2pbb.py` — Python script to convert UBS HOTTP XML to Logos Personal Book Builder format

# Source Data

This code relies on data in the [UBSICAP UBS Open License repository](https://github.com/ubsicap/ubs-open-license). It assumes you've cloned or forked that repo locally.

If you're only looking for the Logos PBB source and don't want to clone repos and stuff, totally cool. Read the next section: :down-arrow:

# Created Data (Logos PBB Input)

Data created by the script is available in the `data/pbb` folder.

There are four word docs in the folder as well as one graphic. 

* [`data/pbb/hottp_en.docx`](data/pbb/hottp_en.docx) — The Preliminary and Interim Report of the Hebrew Old Testament Text Project converted from [XML openly licensed by UBS](https://github.com/ubsicap/ubs-open-license/tree/main/HOTTP).
* [`data/pbb/pbb_title.docx`](data/pbb/pbb_title.docx) — A title page for the PBB edition, with information from the README found in the [UBSICAP respository](https://github.com/ubsicap/ubs-open-license/tree/main/HOTTP).
* [`data/pbb/ratings_en.docx`](data/pbb/ratings_en.docx) — A MSWord document created from the HTML edition of the Ratings document found in the [UBSICAP respository](https://github.com/ubsicap/ubs-open-license/tree/main/HOTTP).
* [`data/pbb/factors_en.docx`](data/pbb/factors_en.docx) — A MSWord document created from the HTML edition of the Factors document found in the [UBSICAP respository](https://github.com/ubsicap/ubs-open-license/tree/main/HOTTP).
* [`data/pbb/hottp_cover.jpg`](data/pbb/hottp_cover.jpg) — An image of the cover of volume 1 of the Preliminary and Interim report of the HOTTP.

If you'd like to just download the PBB files without cloning the entire repo, click the link to the file in the above bulleted list. 

* For `*.docx` files: Click the **View raw** link. Your browser should download the file.
* For `*.jpg` file: After clicking the file link, you can either right-click and save locally, or click the download file button (looks like a down-arrow pointing toward a tray).

# License

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

# Using with Logos

The `*.docx` and `*.jpg` files are suitable for use to create a Personal Book Builder (PBB) resource for Logos Bible Software.

Creation of the resource is left as an excercise to the reader/user. Search the help docs for "PBB" or "Personal Book" and follow the instructions.

Here's some metadata you can use:

* **Title:** The Preliminary and Interim Report of the Hebrew Old Testament Text Project
* **Author/Creator:** United Bible Societies
* **Description:** This is a concise textual analysis of the Old Testament, created by a committee consisting of key Hebrew scholars, in which they discuss a large number of OT passages with text-critical issues. For each passage alternatives are given and the preferred reading is assigned a rating (A, B, C, D).
* **Type:** Use either _Bible Commentary_ or _Bible Apparatus_
* **Language:** English
* **Add Field:** To the standard metadata, use the _Add field_ dropdown to add:
  * _Abbreviated Title:_ HOTTP

Include the files in the following order. In the dialog, you can drag the file name up or down to achieve the correct order.

* `pbb_title.docx`
* `ratings_en.docx`
* `factors_en.docx`
* `hottp_en.docx`

If you get stumped, ask for some help on the Logos Users Forums: https://community.logos.com .
