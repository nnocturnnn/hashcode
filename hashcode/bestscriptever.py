
i = 0
c_day = 0
lib = []
numb = 1




def ebashyshohuyaru_listi(num_library, lib):
    list_bibl = []
    count = 0


    for i in range(1,num_library,2)
        list_bibl.append(sum(lib[i]))
        list_bibl.sort




if __name__ == '__main__':
    filenames = ['a_example.txt','b_read_on.txt','c_incunabula.txt','d_tough_choices.txt','e_so_many_books.txt','f_libraries_of_the_world.txt']
    fileprint = ['1a_example.txt','1b_read_on.txt','1c_incunabula.txt','1d_tough_choices.txt','1e_so_many_books.txt','1f_libraries_of_the_world.txt']

    for i in filenames:
        with open(i,"r") as f:
            line1 = f.readline()
            num_book = int(line1.split()[0])
            num_library = int(line1.split()[1])
            num_day = int(line1.split()[2])
            for i in range(num_library):
                lib.append(f.readline().split())
            
            # while c_day < num_day:
            #     c_day += lib[numb][1]
            #     numb += 2
            #     how_i_have_day_to_scan = num_day - lib[numb][1] # 5
            # for w in fileprint:
            #     with open(w, "w") as pf:
            #         pf.write(str(num_library) + "\n")
            #         pf.write()
            #         pf.write(listbok[i])
                    
