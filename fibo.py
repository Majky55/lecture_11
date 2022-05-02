def recursive_th_fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return recursive_th_fibo(n - 1) + recursive_th_fibo(n - 2)


def main():
    print(recursive_th_fibo(27))


if __name__ == "__main__":
    main()
