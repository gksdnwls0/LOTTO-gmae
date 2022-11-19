import random
emptyarr = []
countarr = []
while True:
    n = int(input("원하시는 숫자 범위의 최댓값을 입력해주세요. "))
    if n < 6:
        print("6 이상의 숫자를 입력해주세요.")
    else:
        break
while True:
    playerarr = list(map(int, input("원하시는 숫자 6개를 입력해주세요. ").split(" ")))
    if len(playerarr) != 6:
        print("숫자가 6개가 되도록 다시 입력해주세요.")
    else:
        break
for i in range(5):
    count = 0
    emptyarr = []
    while True:
        rand_num = random.randint(1, n)
        if rand_num not in emptyarr:
            emptyarr.append(rand_num)
        if len(emptyarr) == 6:
            break
    print(emptyarr)
    for i in range(6):
        if playerarr[i] in emptyarr:
            count += 1
    countarr.append(count)
for i in range(5):
    print("{0}번째 줄에서는 {1}개를 맞추었습니다.".format(i + 1,countarr[i]))