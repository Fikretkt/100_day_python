def wellen_array(array):
    n = len(array)
    #ich tausche paar
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


if __name__ == "__main__":
    # es ruft array von hier
    arr = [1, 2, 3, 4, 5, 6]
    print("Eingabe:", arr)
    print("WellenArray :", wellen_array(arr))
