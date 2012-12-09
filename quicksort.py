numofcmp=0

def partition(list, start, end):
    pivot = list[start]                          # Partition around the last value
    i=start+1
    for j in range(start+1,end+1):
        if list[j]<pivot:
            tmp=list[j]
            list[j]=list[i]
            list[i]=tmp
            i+=1
    tmp=list[i-1]
    list[i-1]=pivot
    list[start]=tmp
    return i-1


def quicksort(list, start, end):
    global numofcmp
    if start < end:                            # If there are two or more elements...
        split = partition(list, start, end)    # ... partition the sublist...
        numofcmp+=end-start
        quicksort(list, start, split-1)        # ... and sort both halves.
        quicksort(list, split+1, end)
    else:
        return

    
if __name__=="__main__":                       # If this script is run as a program:
    import sys
    filehandle=open(sys.argv[1])
    list=[]
    for arri in filehandle.readlines():
        list.append(int(arri))
    start = 0
    end = len(list)-1
    quicksort(list,start,end)                  # Sort the entire list of arguments
    import string
    print numofcmp           # Print out the sorted list
    print list