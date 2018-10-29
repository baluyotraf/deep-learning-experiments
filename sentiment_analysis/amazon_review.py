import gzip

def read(path, target_classes, data_per_class, f=lambda x: True):
    """
    Reads an amazon view file
    
    :param path: path of the gzipped review file
    :param target_classes: list of scores to be read
    :param data_per_class: the number of data per target class to be read
    :param f: a filter function to further filter the results
    :return: Generator for the data inside the file
    """
    counter = {tc:0 for tc in target_classes}
    done = 0
    with gzip.open(path, 'r') as g:
        for l in g:
            if done == len(target_classes):
                break
            d = eval(l)
            key = d['overall']
            if counter.get(key, data_per_class) < data_per_class:
                if f(d):
                    counter[key] += 1
                    if counter[key] == data_per_class:
                        done += 1
                    yield d
                    
def length_between(x, min_l, max_l):
    """
    Checks if a length of the review is between the specified values
    
    :param x: Amazon review dictionary data
    :param min_l: minimum length, inclusive
    :param max_l: maximum length, inclusive
    :return: True if within lengths else False
    """
    length = len(x['reviewText'])
    return max_l >= length >= min_l