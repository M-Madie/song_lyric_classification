# Song Lyrics (Text) Classification Project

This repository contains one of my projects as a data science student where i developed an NLP based model that classifies lyrics as belonging to one of two artists (Britney Spears or 50-Cent).

The data was scraped from the web (process for one of the artists is shown in the notebook).

<ins>The repository includes the following files:</ins>
* **task_web_scraping.ipynb** - notebook that includes example of lyrics scraping for one artist
* **task_b_fifty.ipynb** - data processing and model development and training (including feature engineering)
* **vector_1.pickle** - a pickled transformation vector (icludes all transformations)
* **model_1.pickle** - a pickled trained text classification model
* **task_b_fifty.py** - a script that uses the pickled model & vextorizer; takes lyrics from user and makes an artist prediction 
