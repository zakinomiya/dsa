def check_heap(data):
    i = 0
    ll = len(data)
    l, r = 0, 0
    try: 
        while i < ll:
            l, r = (2*i)+1, (2*i)+2
            if ll > l:
                assert data[i] <= data[l]

            if ll > r:
                assert data[i] <= data[r]
            i+=1
    except AssertionError:
        print(i, l, r)
        print(data[i], data[l], data[r])

def sift_down(i, data):
    if len(data) <= (2*i)+1:
        return

    parent_index = i
    l = 2*i+1
    r = l
    if len(data) > (2*i)+2:
        r = (2*i)+2

    if data[parent_index] > min(data[l], data[r]):
        if data[l] < data[r]:
            data[parent_index], data[l] = data[l], data[parent_index]
            return sift_down(l, data)
        else:
            data[parent_index], data[r] = data[r], data[parent_index]
            return sift_down(r, data)
        
def build_heap(data):
    for i in range(len(data)-1, -1, -1):
        sift_down(i, data)

    return data

