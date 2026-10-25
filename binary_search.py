def binary_search(isi_array, target_angka, nilai_minimal,nilai_maksimal):
    if nilai_minimal > nilai_maksimal: # cek index bukan nilai
        return -1

    mid = (nilai_minimal + nilai_maksimal) // 2

    if isi_array[mid] == target_angka: 
        return mid

    if target_angka < isi_array[mid]:
        return binary_search(isi_array, target_angka, nilai_minimal, mid - 1) # ini artinya index nya di kurang 1
    else :
        return binary_search(isi_array, target_angka, mid + 1, nilai_maksimal)

data = [2, 5, 8, 12, 16, 23, 38]
hasil = binary_search(data, 23, 0, 6)
print(hasil)


