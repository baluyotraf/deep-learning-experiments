import json

def read_file(path, target_keys=('sentence1', 'sentence2', 'gold_label'), label_filters=None):
    """
    Reads an SNLI dataset file
    
    :param path: path of the file to open
    :param target_keys: data to be extracted from the jsonl file
    :param label_filters: target labels to be read
    :returns: A generator containing a dictionary of the data from the file
    """
    with open(path) as file:
        for line in file:
            line_json = json.loads(line)
            label = line_json['gold_label']
            if label_filters is None or label in label_filters:
                data = {k: line_json[k] for k in target_keys}
                yield data