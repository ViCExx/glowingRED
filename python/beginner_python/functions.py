def do_nothing(pos1, pos2, pos3, /, either1, either2, *, keyword1, keyword2, keyword3):
    print("pos1",pos1)
    print("pos2,",pos2)
    print("pos3,",pos3)
    print("either1,",either1)
    print("either2,",either1)
    print("keyword1,",keyword1)
    print("keyword2,",keyword2)
    print("keyword3,",keyword3)

do_nothing(1, 2, 3, 4, either2=-5, keyword3=6, keyword1=7, keyword2=8)