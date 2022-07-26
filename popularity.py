
def popularity(text):
    text_low = text.lower().split(" ")
    text_low.sort()
    text_result = []
    text_resultat = []
    output_set = set()
    
    for str in range (len(text_low)) :
        result = text_low.count(text_low[str])
        if result ==3 :
            text_result.insert(0,text_low[str])  
        elif result == 2 :
            text_result.append(text_low[str])   
        else:
            text_result.append(text_low[str])

    for i in text_result:
        if i not in text_resultat:
            text_resultat.append(i)
    print (text_resultat)
        
    

    

        

popularity('apple kiwi pineapple kiwi apple kiwi') # ['kiwi', 'apple', 'pineapple']
popularity('aPPle pine Apple kiwi Apple kiwi') # ['apple', 'kiwi', 'pine']
popularity('aPPle pine Apple kiwi Apple kiwi') # ['apple', 'kiwi', 'pine']
popularity('aab aaa aac aab aac aaa x') # ['aaa', 'aab', 'aac', 'x']