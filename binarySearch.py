def search (L, e, low, high):
    mid = (low + high)//2
    
    if high == low:
        return L[low] == e
    if L[mid] == e:
        return True
    
    elif e > L[mid]:
        return search(L,e,mid+1,high)
    elif e < L[mid]:
        return search(L,e,low,mid-1)

print search([1,2,3,4,5,6],e=7,low=0,high=5)
    
