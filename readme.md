# Movie Transcript Text Generation Project Readme

## /data/ Folder:
This folder contains the dataset for our project. It contains four subfolder and 4 text files.
- The data/high-rated and data/low-rated folders contain the raw transcripts (as well as unused scripts) for the movies.
- The data/ProcessedBadScripts and data/ProcessedGoodScripts contain those same scripts, but after pre-processing was performed on them.
- data/bottom100.txt and data/top250.txt are just a list of the bottom-rated and top-rated 250 movies on IMDb (although only 100 of the latter were used).
- data/sources-high-rated.txt and data/sources-low-rated.txt contain the exact links to where the first 25 movies from each group were sourced.

## /src/ Folder:
This folder contains the source code for our neural model, n-gram model, and the script used for pre-processing the data.
- src/neural contains the code for the LSTM, as well as saved weights for our final LSTM models, a folder containing the Word2Vec representation files.
- src/n-gram contains the source code for the n-gram model.
- src/preprocessing contains the source code for the script used to pre-process the data.