while True:
    print("請計算圓面積");
    r = input("請輸入半徑:");
    if r == "R":
        break;
    floatR = float(r);
    area = 3.1415926 * floatR ** 2;
    print("圓面積為:" + str(area));
    print("\n\n\n");
    print("=========================================");

print("bye bye")
