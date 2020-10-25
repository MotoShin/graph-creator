# graph-creator
[Science Plots](https://pypi.org/project/SciencePlots/)を簡単に使えるようにしたやつ。（自分用）

## 2軸のグラフの作成 (x-y)
### 実行方法
以下のように実行すると対話モードでアプリケーションが立ち上がるので指示通り入力していってください。
```
python main.py
```
全ての入力に対して入力無しにするとdefault値が全て入ります。
デファルト値は以下の通り。
```
Please select a mode (1: 2-axis graph): 1
Input a csv file path: example/example.csv
Input a x axis name: x
Input a y axis name: y
Input a output image file name: img.png
```

### csvファイル形式
以下のようなcsvの形式ならばOK
```
x_axis,y_axis_1,y_axis_2,y_axis_3
0,1,2,3
0,1,2,3
```
詳しくは[example.csv](https://github.com/MotoShin/graph-creator/blob/master/example/example.csv)を参照
