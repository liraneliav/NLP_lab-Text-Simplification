# NLP_lab-Text-Simplification
The project deals with simplification of text by translation English text into Simple English text.

Simplifying the texts makes them more accessible to a wider audience and can improve readability and understanding (for example, non-native speakers of the language).

# This repository contains:
* 2 datasets: enwiki.txt, simplewiki.txt
* 7 code files:
    * Data relate:

      *	separate_into_texts.py

      *	clean_text.py

      *	same_files.ipynb
    * Sentence alignment relate:

      *	sentence_sep.ipynb

      *	sentence_alignment_SBERT.ipynb
    * T5 relate:

      * T5_model.ipynb

      * T5_generate_sentences.ipynb
* results directory:

  * trainer_state.json (logs from the training)

  * test_log.jsonl (logs from the testing)

  * transleated_by_trained_T5.txt (genereted Simple English sentences made by the trained T5 model and their similarity score to the original Simple English sentence).

# To run this project you need to execute the files in this order:
 1.	separate_into_texts.py
 2.	clean_text.py
 3.	same_files.ipynb
 4.	sentence_sep.ipynb
 5.	sentence_alignment_SBERT.ipynb
 6.	T5_model.ipynb
 7.	T5_generate_sentences.ipynb

* More detailed insturations and information are in the report.
* Pay attention that you have the original datasets to get the same results (The datasets that were uploaded - enwiki-small.txt , simplewiki-small.txt - are smaller then the original that are bigger sized then GitHub allow).
