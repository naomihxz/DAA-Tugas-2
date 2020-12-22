# Jawaban soal no 2, algoritma brute force

def a_pow_n(a, n):
    res = 1
    for i in range(n):
        res *= a
    
    return res


if __name__ == "__main__":
    from time import perf_counter_ns
    import matplotlib.pyplot as plt

    list_n = []
    list_rt = []

    for x in range(10, 1000, 100):
        start_time = perf_counter_ns()
        r = a_pow_n(10, x)
        finish_time = perf_counter_ns()

        running_time = finish_time - start_time
        list_n.append(x)
        list_rt.append(running_time)

        print('pow(10,' + str(x) + ')\t\t time : ' + str(running_time))

    plt.scatter(list_n, list_rt)
    plt.plot(list_n, list_rt)
    plt.title('Brute Force')
    plt.xlabel('Jumlah n')
    plt.ylabel('Running time (ns)')
    plt.show()
