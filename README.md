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

# Next steps
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
    
