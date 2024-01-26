i = 0
for _ in range(2):
    print("layer0 - " + str(i))
    i += 10
    for _ in range(5):
        print("layer1 - " + str(i))
        i += 1