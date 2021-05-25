def run():
    mults = [i for i in range(0, 100001) if i %
             4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(mults)


if __name__ == '__main__':
    run()
