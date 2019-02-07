import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    
    for testwords in range(test_set.num_items):
        best_word=None
        
        X,lengths= test_set.get_item_Xlengths(testwords)     #getting sequence and length 
        probability={}
        for word, model in models.items():                  ##iterating through all words and corresponding model
            try:                                       
                probability[word]= model.score(X, lengths)              #log likelihood for each word  
                
            except:
                probability[word]=float("-inf") 
                continue
        
        probabilities.append(probability)
        #thanks to mentor for the suggestion
        best_guess= max(probability, key=probability.get)
        guesses.append(best_guess)
        
        assert len(probabilities)==len(guesses)
            
    return probabilities, guesses