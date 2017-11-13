import pickle


# load pickle file
def load_pickle(file_path):
    with open(file_path, 'rb') as f:
        file_pickle = pickle.load(f)
    return file_pickle


# save pickle file
def save_pickle(data, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)


# is subset of another list
def is_subset(top_list, sub_list):
    return set(sub_list).issubset(set(top_list))


# lower the list of str
def lstr_lower(lstr):
    return [s.lower() for s in lstr]






