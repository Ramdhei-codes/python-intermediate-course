def read(route):
    names = []
    with open(route, "r", encoding="utf-8") as f:
        for line in f:
            line = line.replace('\n', '')
            names.append(line)

    print(names)


def write(route):
    brands = ['Moyu', 'Qiyi', 'ShengShou', 'Dayan', 'X-man', 'GAN']
    with open(route, "w", encoding='utf-8') as f:
        for brand in brands:
            f.write('{}\n'.format(brand))



def run():
    # read("./files/example.txt")
    write('./files/cube_brands.txt')


if __name__ == '__main__':
    run()
