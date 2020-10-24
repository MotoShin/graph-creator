# graph-creator
## 2軸のグラフの作成 (x-y)
### 実行方法
以下のように実行する
```
# 対象のcsvのパスを指定する
python main.py [csv_file_path]

# 対象のcsvのパスを指定して画像名も指定する
python main.py [csv_file_path] [output_file_name]

# 軸の名前を指定
python main.py [csv_file_name] [x_axis_name] [y_axis_name]

# 全部盛り
python main.py [csv_file_name] [x_axis_name] [y_axis_name] [output_file_name]
```

### csvファイル形式
以下のようなcsvの形式ならばOK
```
x_axis,y_axis_1,y_axis_2,y_axis_3
0,1,2,3
0,1,2,3
```
詳しくは[example.csv](https://github.com/MotoShin/graph-creator/blob/master/example/example.csv)を参照
