def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

numbers = [4, 5, 9, 4, 9, 1, 5]
Result = remove_duplicates(numbers)
print(Result)