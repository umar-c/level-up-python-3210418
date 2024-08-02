import pickle

def pickle_dict(dictionary, filename):
  with open(filename, "wb") as file:
    pickle.dump(dictionary, file)

def unpickle_dict(filename):
  with open(filename, "rb") as file:
    return pickle.load(file)

# commands used in solution video for reference
if __name__ == '__main__':
    test_dict = {1: 'a', 2: 'b', 3: 'c'}
    pickle_dict(test_dict, 'test_dict.jsn')
    recovered = unpickle_dict('test_dict.jsn')
    print(recovered)  # {1: 'a', 2: 'b', 3: 'c'}

    test_dict = {1: 'a', 2: 'b', 3: ['c', 'd', {4: ['e', 'f'], 5: (6,7)}]}
    pickle_dict(test_dict, 'test_dict.pickle')
    recovered = unpickle_dict('test_dict.pickle')
    print(recovered)
