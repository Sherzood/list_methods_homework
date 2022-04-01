def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i=0
    
    if fruits[i]=='apple':
        fruits.pop(i)
    i+=1
    if fruits[i]=='apple':
        fruits.pop(i)
    i+=1
    if fruits[i]=='apple':
        fruits.pop(i)
    i+=1
    if fruits[i]=='apple':
        fruits.pop(i)
   
    return fruits 
print(main(['kiwi','mango','apple','apple','applej']))    