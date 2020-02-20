
i = 0
c_day = 0
lib = []
numb = 1


def ebashyshohuyaru_listi(num_library, lib):
    list_bibl = []
    count = 0

    for i in range(1,num_library+2,2):
        list_bibl.append(sum(int(item) for item in lib[i]))
        


with open('a_example.txt', "r") as f:
    line1 = f.readline()
    num_book = int(line1.split()[0])
    num_library = int(line1.split()[1])
    num_day = int(line1.split()[2])
    all_book = f.readline().split()
    for i in range(num_library*2):
        lib.append(f.readline().split())

ebashyshohuyaru_listi(num_library, lib)
        




# print(lib[1][0])