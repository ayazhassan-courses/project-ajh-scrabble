import os 


f = open('dic.txt', "r")
words=[]
for line in f:
    tmp = line[0:(len(line)-1)]
    words.append(tmp.upper())
f.close()


##############################################################
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

#words=["zafar","babar","ali","boba"]


def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 



def sort_dictionary(words):
    #l=len(words)
    #quickSort(words,0,l-1)
    words.sort()

    #testing
    if os.path.exists("dic.txt"): 
        os.remove("dic.txt") 
    
    file = open("dic.txt", "w")
    for k in words:
        file.write(k+"\n") 
    file.close()
    
    return words

words = sort_dictionary(words)

#################################################################


    
