
def printer(res):
    if type(res)==tuple:
        max_width = []
        limit_len = 40
        for index, elem  in enumerate(res[1]):
            max_width.append(max([len(str(x[index])) for x in res[0]]+[len(elem)]))
            if max_width[index]>limit_len:
                max_width[index] = limit_len
            print(elem.rjust(max_width[index])+ " | ", end='')
        print('')
        for item in res[0]:
            print(" | ".join(map(lambda x: str(x[1])[:min(max_width[x[0]],len(str(x[1])))].rjust(max_width[x[0]]) , enumerate(item)))+" | ")
    elif res == True:
        print("Without feedback")
    elif res == False:
        print("Error")

#select p.likes from Posts p join Walls w on w.id=p.id_walls where title='Birthday!' and id_user='+380679201293' and likes > 5