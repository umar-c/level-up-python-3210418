def index_all(list_to_search, value_to_search):
  list_of_indices = []
    
  for index, element in enumerate(list_to_search):
    if value_to_search == element:
      list_of_indices.append([index])
    elif isinstance(element, list):
      for i in index_all(element, value_to_search):
        list_of_indices.append([index] + i)
  
  return list_of_indices

# commands used in solution video for reference
if __name__ == '__main__':
    # ex = [1, 2, 3]
    # ex = [[1, 2, 3], 2]
    ex = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]

    val_to_search = [1 ,3]
    print(f'index_all(ex, {val_to_search}) = {index_all(ex, val_to_search)}')

    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]
