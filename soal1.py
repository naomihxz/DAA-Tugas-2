# Jawaban soal 1

# membuat list berisi tuple (<index ke-i>, <weights ke-i>, <profit ke-i>)
def convert_tuple(weights, profits):
    if len(weights) != len(profits):
        return []
    res = []
    l = len(weighths)
    for i in range(l):
        res.append((i, weighths[i], profits[i]))
    
    return res

# membuat himpunan bagian dari tuple-tuple item
def make_powerset(items):
    res = [[]]
    for item in items:
        newset = [r+[item] for r in res]
        res.extend(newset)

    return res

# brute force untuk knapsack
def solve_bf(K, items):
    knapsack = []
    best_wg = 0
    best_val = 0

    ps = make_powerset(items)
    print('\nSeluruh himpunan bagian : ')
    for p in ps:
        print(p)

    print('\nKombinasi semua item : ')
    i = 0
    for item_tp in ps:
        set_wg = sum([e[1] for e in item_tp])
        set_val = sum([e[2] for e in item_tp])
        print('Item ke-' + str(i) + ' : P = ' + str(set_wg) + ' V = ' + str(set_val))
        i+=1
        if set_wg <= K and set_val > best_val:
            best_wg = set_wg
            best_val = set_val
            knapsack = item_tp
    
    return knapsack, best_wg, best_val

if __name__ == "__main__":
    import time

    start_time = time.perf_counter()

    # Array dari soal
    weighths = [2, 5, 10, 5]
    profits = [2000, 3000, 5000, 100]
    K = 16

    tp = convert_tuple(weighths, profits)
    print('Item : ', tp)

    knapsack = solve_bf(K, tp)
    print('\nKNAPSACK\nKombinasi item : ', knapsack[0])
    print('Total weight : ', knapsack[1])
    print('Kombinasi value : ', knapsack[2])

    
    finish_time = time.perf_counter()
    print('\nFinished in', str(finish_time-start_time), 'seconds')