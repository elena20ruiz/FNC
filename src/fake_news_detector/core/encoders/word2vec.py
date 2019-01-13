from gensim import models
from gensim.models import LdaMulticore
import numpy as np

##############################
## TOPIC MODELING WITH LDA ###
##############################


class Word2Vec_model():

    def __init__(self, num_features, num_features, context):
        self.num_features = dictionary
        self.min_word_count = num_topics
        self.num_workers = 4
        self.context = context
        self.model = None
        self.downsampling = 1e-3

    # LDA Model
    def create_model(self, sententes):
        return  Word2Vec(sentences=sentences,
                    sg = 1,
                    hs = 0,
                    workers = self.num_workers,
                    size = self.num_features,
                    min_count = self.min_word_count,
                    window = self.context,
                    sample = self.downsampling,
                    negative=5,
                    iter=6)

    # Transformations
    def get_document_distribution(self,document, min_prob=0):
        topic_importances = self.lda_model.get_document_topics(document, minimum_probability=min_prob)
        topic_importances = np.array(topic_importances)
        return topic_importances[:,1]


    # Getters
    def get_model(self):
        return self.lda_model
    
    def get_dictionary(self):
        return self.dictionary


    # USAGE
    # Create LDA Model
    # Tranform data to LDA
    def run_modeling(self, train_data, test_data):

        # Create LDA model & fit
        self.lda_model = self.create_model(train_data)

        # Get train document distributions
        train_lda_data = list(map(lambda doc:
                                        self.get_document_distribution(doc),
                                        train_data))

        # Get test document distributions
        test_lda_data = list(map(lambda doc:
                                        self.get_document_distribution(doc),
                                        test_data))

        return train_lda_data, test_lda_data

    # MODEL INFO
    def print_topics(self):
        for idx, topic in self.lda_model.print_topics(-1):
            print('Topic: {} \nWords: {}'.format(idx, topic))