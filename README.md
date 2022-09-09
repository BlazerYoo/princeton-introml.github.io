# About

This repository hosts the Github Pages website for distributing course notes for COS 324 - Introduction to Machine Learning course at Princeton University. It is based on the template [Just the Class](https://github.com/kevinlin1/just-the-class).

## How to Update the Notes
1. Run `git pull` to make sure you local repository is up to date.
2. Download the newly updated course notes from Overleaf into the ``/files/`` folder on your local repository. The name should be `COS324_Course_Notes.pdf`.
3. If the number of chapters or parts in the notes have changed, update the corresponding data in the `pdf_split.py` file:
    - Line 2: `NUM_CHAPTERS` should equal to the current number of chapters
    - Line 3: `PART_MARKERS` should equal to the list of all Roman numerals for the parts of the notes
4. Run `python3 pdf_split.py` to automatically generate the pdf files for individual chapters. (You will have to install `pip install PyPDF2` if you have not already.)
5. Double check that the generated pdf files for individual chapters are correct. Some things to check for are:
    - First page of each file is indeed the first page of each chapter
    - Last page of each file is indeed the last page of each chapter (or a blank page)
6. If the names/number of the chapters or parts in the notes have changed, update the corresponding data in the `_modules/part*.md` files.
7. Commit and push the changes made.
8. The website will be automatically rendered. It may take up to a few minutes.
