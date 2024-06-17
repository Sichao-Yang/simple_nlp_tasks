FLAG=--no-check-certificate

cd ~/stanford_parser
# wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip $FLAG
# unzip stanford-corenlp-full-2018-02-27.zip
cd stanford-corenlp-full-2018-02-27

# Get the Chinese model 
# wget http://nlp.stanford.edu/software/stanford-chinese-corenlp-2018-02-27-models.jar $FLAG
wget https://raw.githubusercontent.com/stanfordnlp/CoreNLP/master/src/edu/stanford/nlp/pipeline/StanfordCoreNLP-chinese.properties 

# Get the Arabic model
# wget http://nlp.stanford.edu/software/stanford-arabic-corenlp-2018-02-27-models.jar $FLAG
wget https://raw.githubusercontent.com/stanfordnlp/CoreNLP/master/src/edu/stanford/nlp/pipeline/StanfordCoreNLP-arabic.properties 

# Get the French model
# wget http://nlp.stanford.edu/software/stanford-french-corenlp-2018-02-27-models.jar $FLAG
wget https://raw.githubusercontent.com/stanfordnlp/CoreNLP/master/src/edu/stanford/nlp/pipeline/StanfordCoreNLP-french.properties 

# Get the German model
# wget http://nlp.stanford.edu/software/stanford-german-corenlp-2018-02-27-models.jar $FLAG
wget https://raw.githubusercontent.com/stanfordnlp/CoreNLP/master/src/edu/stanford/nlp/pipeline/StanfordCoreNLP-german.properties 


# Get the Spanish model
# wget http://nlp.stanford.edu/software/stanford-spanish-corenlp-2018-02-27-models.jar $FLAG
wget https://raw.githubusercontent.com/stanfordnlp/CoreNLP/master/src/edu/stanford/nlp/pipeline/StanfordCoreNLP-spanish.properties 