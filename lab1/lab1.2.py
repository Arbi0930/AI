from textblob import TextBlob
def get_sentiment_analysis(text, coins):
    sentiment = []
    blob = TextBlob(text)
    for sentence in blob.sentences:
        lowercase_words = [x.lower() for x in sentence.words]
        for coin in coins:
            if coin[0].lower() in lowercase_words or coin[1].lower() in lowercase_words:
                try:
                 sentiment[coin] += sentence.sentiment.polarity
                except:
                 sentiment[coin] = sentence.sentiment.polarity
	
    return sentiment, blob.sentiment.polarity 



def create_data(X: dt.Frame = None) -> Union[str, List[str],
                                                 dt.Frame, List[dt.Frame],
                                                 np.ndarray, List[np.ndarray],
                                                 pd.DataFrame, List[pd.DataFrame]]:
        # exit gracefully if method is called as a data upload rather than data modify
        if X is None:
            return []
        import os
        from h2oaicore.systemutils import config
        from textblob import TextBlob

        X = dt.Frame(X).to_pandas()
        for text_colname in text_colnames:
            X["sentiment_dai_" + text_colname] = X[text_colname].astype(str).fillna("NA").apply(
                lambda x: TextBlob(x).sentiment[0])

        temp_path = os.path.join(config.data_directory, config.contrib_relative_directory)
        os.makedirs(temp_path, exist_ok=True)

        # Save files to disk
        file_train = os.path.join(temp_path, output_dataset_name + ".csv")
        X.to_csv(file_train, index=False)

        return [file_train] 
	