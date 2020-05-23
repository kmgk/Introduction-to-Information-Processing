import csv
import random

prefecture = [
    "青森",
    "岩手",
    "宮城",
    "秋田",
    "山形",
    "福島",
    "茨城",
    "栃木",
    "群馬",
    "埼玉",
    "千葉",
    "神奈川",
    "新潟",
    "富山",
    "石川",
    "福井",
    "山梨",
    "長野",
    "岐阜",
    "静岡",
    "愛知",
    "三重",
    "滋賀",
    "兵庫",
    "奈良",
    "和歌山",
    "鳥取",
    "島根",
    "岡山",
    "広島",
    "山口",
    "徳島",
    "香川",
    "愛媛",
    "高知",
    "福岡",
    "佐賀",
    "長崎",
    "熊本",
    "大分",
    "宮崎",
    "鹿児島",
    "沖縄",
]
ken = ["県", ""]
shi = ["市", ""]
cho = ["町", ""]
kouza = ["-", ""]

array = [
    [
        random.choice(prefecture)[0] + random.choice(prefecture)[1],
        random.choice(prefecture)[0] + random.choice(prefecture)[1],
        random.choice(prefecture),
        random.choice(prefecture)[0] + random.choice(prefecture)[1],
        random.choice(prefecture)[0] + random.choice(prefecture)[1],
        str(random.randint(1000000, 9999999)),
    ]
    for i in range(10000)
]

info = [
    [
        array[i][0],
        array[i][1],
        array[i][2] + random.choice(ken),
        array[i][3] + random.choice(shi),
        array[i][4] + random.choice(cho),
        array[i][5][0:3] + random.choice(kouza) + array[i][5][3:],
    ]
    for i in range(len(array))
]

control = [
    [
        array[i][0],
        array[i][1],
        array[i][2] + "県" + array[i][3] + "市" + array[i][4] + "町",
        array[i][5],
    ]
    for i in range(len(array))
]


with open("./info.csv", "w", newline="", encoding="shift_jis") as f:
    writer = csv.writer(f)
    writer.writerow(["性", "名", "県名", "市名", "町名", "口座番号"])
    writer.writerows(info)

with open("./info_utf-8.csv", "w", newline="", encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(["性", "名", "県名", "市名", "町名", "口座番号"])
    writer.writerows(info)

with open("./control.csv", "w", newline="", encoding="shift_jis") as f:
    writer = csv.writer(f)
    writer.writerow(["性", "名", "住所", "口座番号"])
    writer.writerows(control)

with open("./control_utf-8.csv", "w", newline="", encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerow(["性", "名", "住所", "口座番号"])
    writer.writerows(control)
