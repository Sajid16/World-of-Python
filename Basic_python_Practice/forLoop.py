foods = ["bacon","cheese","sausage","burger","pizza","pasta"]

# for f in foods:
for f in foods[1:5]:
    print(f)
    # print(len(f))
    if f == 'bacon':
        print("it can be an ingredients of burger")
    elif f == 'cheese':
        print("it can be ingredients of burger or pizza or pasta")
    elif f == 'sausage':
        print("it can be added to pizza or pasta or burger")
    else:
        print(f + " is a food that i wanna eat now")
