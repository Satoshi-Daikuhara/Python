import csv
import pandas as pd

csv_file = open("./Book1.csv", "r", encoding="ms932", errors="", newline="" )

#リスト形式
l = csv.reader(csv_file,  delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

#辞書形式
d = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

# header = next(l)
#
# print(header)
# for row in l:
#     # rowはList
#     # row[0]で必要な項目を取得することができる
#     print(row)
#
# for r in d:
#     #rowはdictionary
#     #row["column_name"] or row.get("column_name")で必要な項目を取得することができる
#     print(r)

csv_input = pd.read_csv(filepath_or_buffer="C:\\Users\\tie306098\PycharmProjects\Progrece\Book1.csv", encoding="ms932", sep=",")
# # インプットの項目数（行数 * カラム数）を返却します。
# print(csv_input.size)
# # 指定したカラムだけ抽出したDataFrameオブジェクトを返却します。
# print(csv_input[["商品名", "販売単価"]])

# #値を二次元配列形式?で返却します。
# #返却される型は、numpy.ndarray
# print(csv_input.values)
# #行インデックス、カラムインデックスの順番で指定して項目の値を取得できます。
# print(csv_input.values[0, 1])

# #頭から指定行数分取得
# #返却される型は、pandas.core.frame.DataFrame
# print(csv_input.head(3))
#
# #後ろから指定行数分取得
# #返却される型は、pandas.core.frame.DataFrame
# print(csv_input.tail(3))

# #行数を確認
# print(len(csv_input))
#
# #カラム数を確認
# print(len(csv_input.columns))
#
# #次元の確認
# print(csv_input.shape)

# #カラム情報
# print(csv_input.columns)
# print(csv_input.columns[3])

# #データアクセスの方法いろいろ
# #loc[rows, columns]
# #全行選択の場合、rowsは「:」を指定
# print(csv_input.loc[:,["商品名", "販売単価"]])
# print(csv_input.loc[1:2,["商品名", "販売単価"]]) #2行目3行目
#
# #iloc[rows番号, columns番号]
# #全行選択の場合、rowsは「:」を指定
# #インデックスの指定方法に注意
# print(csv_input.iloc[:, 3])#3カラム目を全行
# print(csv_input.iloc[0:3, 3:5]) #3,4カラム目だけを1行～3行目まで抽出
#
# #ix
# #カラム名、カラム番号のどちらでも使用可能
# print(csv_input.ix[0:3, ["商品名", "販売単価", "仕入単価"]]) #1行目～4行目
# print(csv_input.ix[0:3, 3:6]) #1行目～3行目

# # 指定した条件で抽出
# print(csv_input[csv_input["販売単価"] > 1500])
# # 複数条件の組み合わせの場合
# # and条件は「&」を使用
# print(csv_input[(csv_input["販売単価"] > 1500) & (csv_input["販売個数"] > 3)])
# # orr条件は「|」を使用
# print(csv_input[(csv_input["販売単価"] > 1500) | (csv_input["販売個数"] > 3)])
# # 抽出条件には、以下のような指定方法もあります
# print(csv_input.query("販売単価 > 1500"))
# # 複数の値を指定する
# print(csv_input[(csv_input["商品名"].isin(["ロロ", "へアップX5"]))])

csv_input["追加カラム"] = ["test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9", ]

print(csv_input)


