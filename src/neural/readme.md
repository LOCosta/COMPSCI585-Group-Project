# Neural Model Readme

This neural model was designed to be run on a Google Colab VM and required quite a bit of fiddling with Google Drive. That said, the files and folders contained here are the following:
- Word2Vec folder: Contains the saved Word2Vec representations for both the vocabulary of the bad movies and the good movies, these are kept separately in word2vec_Bad_n, and word2vec_Good_n, where n is the number of dimensions for that representation. While we built 200-dimensional Word2Vec word models, we did not end up using them in our final model, but they are saved for posterity purposes. Of note is that the 300-dimensional models are compressed in .7z files, the reason being that they exceeded Github's file size limit for single files.
 - The .csv files contain the entire datasets compiled into two .csv files, one for the good movies and one for the bad. Each row indicates a separate sentence, and words are separated by commas.
- DeepScript.ipynb: This is the iPython notebook that contains all of the code for the LSTM model.
- Sample_Model_Outputs.txt: Contains 100 samples of predictions made by the good movie model on its test data set, and 100 samples of predictions made by the bad movie model on its test data set. The bad movie ones are first, and the good movie ones start on the line that contains the words "Good Movie Model"
- "Sentence Argmax Generation.txt": contains a few sentences we generated using our model using our models.

We tried to upload the final saved models to GitHub, although they exceed the file size limit, even after we tried compressing them. Thus the links to them on Google Drive are below. They should be accessible as long as you are logged into a UMass account on Drive.
[Bad Movie Model .h5 File](https://drive.google.com/file/d/1eZat2inYSL2nSOOYW1dkU3tSK0S1Ex5o/view?usp=sharing)
[Good Movie Model .h5 File](https://drive.google.com/file/d/1yyCarcA3OFSy9vNB2ofon5T2jqmA7LvE/view?usp=sharing)