def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    k=[fruits.count('apple')]
    i=0
    if fruits[i]=='apple':
        k.append(i)
    i+=1
    if fruits[i]=='apple':
        k.append(i)
    i+=1
    if fruits[i]=='apple':
        k.append(i)
    i+=1
    if fruits[i]=='apple':
        k.append(i)
    i+=1
    if fruits[i]=='apple':
        k.append(i)        

        
    return k
print(main(['apple','banana','apple','pear','apple']))    