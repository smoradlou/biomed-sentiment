# biomed-sentiment

The notebooks go through

(1) data exploration and initial modeling 

(2) data augmentation ideas and NLPAug library

(3) modeling with augmented data

The helper codes for several augmentation strategies and preprocessing are in src/data
For the in domain pre-trained embeddings BioWord2Vec was used, and can be downloaded from https://github.com/ncbi-nlp/BioWordVec to the folder ./models

"Bio_embedding_extrinsic" is for extrinsic tasks and used as the input for various downstream NLP tasks, such as relation extraction or text classification. Both sets are in binary format and contain 2,324,849 distinct words in total. All words were converted to lowercase and the number of dimensions is 200.



Dependencies can be installed using 

`pipenv install`

## Summary of results
With data augmentation and parameter optimization on a hold out evaluation set of original data, we we able to 
achieve accuracy of .75 and macro F1 of .65. The majority class classifier would get an accuracy of about .6 
and macro F1 of about .25, if the class frequencies are stable. What is the inter-annotator agreement, and kappa?


Model: SVC(C=10, kernel='linear')
with augmented dataset size of 955. Validation dataset of 40 original sentences, and Test dataset of 40 holdout original 
sentences, all stratified to reflect original class frequencies. 
## Next steps
- Due to lack of time, thorough comparisons between different augmentation strategies were not made
- Explanations and error analysis is also missing -- This can inform additional features, like particular sentential frames that might signal class membership:
  e.g. Some observations:
  
        positive:
        clinical benefit
        significant effect
        better outcome
        clinically meaningful
        positive effect
        considered demonstrated
        provides support
        data supports
        this has been appropriately covered by
        studied in sufficient number of 
        adverse events were in line with 
        
        
        negative:
        still considered very limited
        no significant additional benefit
        study is requested to

- If we had access to the following, it could inform a data collection/augmentation and modeling loop, which in my experience, is often more useful that tweaking the models themselves
    - details of the use case (i.e. What is the whole pipeline? How will the classifications be used? What other features might be available?)
    - annotation guidelines or schema
  
- Multi-label classification might be a better paradigm for this problem, as both models and humans seem to have trouble distinguishing between neutral and negative items, to be able to make informed suggestions here.
- Again will need access to the annotation guidelines and details of the complete pipeline including extraction of the sentences
- External data from scientific citation sentiment classification tasks: 
  I found 2 datasets on this. The task is to classify citation containing sentences for sentiment polarity 
  and/or intent of the citing author. There might be quite some potential for expanding what there is to learn, 
  as the tasks seem to be fundamentally vert similar --more similiar than our task is to common sentiment analysis, I would say. 
See https://github.com/DominiqueMercier/ImpactCite and related work. The other dataset, SentiCiteDB, is not publicly available, however I got access to a sample through the author.
    
