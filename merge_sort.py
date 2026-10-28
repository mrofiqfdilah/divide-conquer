def merge_sort(nilai_array):
    if len(nilai_array) <= 1:  
        return nilai_array

    mid = len(nilai_array) // 2
    kiri  = merge_sort(nilai_array[:mid])
    kanan = merge_sort(nilai_array[mid:])
    return merge(kiri, kanan)

def merge(kiri, kanan):
    hasil = []
    i = 0                              
    j = 0                                 

    while i < len(kiri) and j < len(kanan):    
        if kiri[i] <= kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    hasil.extend(kiri[i:])             
    hasil.extend(kanan[j:])
    return hasil                  

data = merge_sort([1, 13, 24, 2, 15, 27])
print(data)