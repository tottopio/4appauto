
## Android アプリを PC で動かすためのエミュレーターを使用前提のプログラムです。
## 環境構築

### 実行コマンド一覧

#### 使用環境
```
エミュレータ：NoxPlayer
OS:Windows10
CPU:ryzen7 7700x
グラボ：MSI GeForce RTX 2060 SUPER
```

#### エミュレータ設定
```
1.Android7(32bit)端末を起動。
※Android5を起動した場合うまく作動しないことがありました。
2.起動後、パフォーマンスのタブを選択して下記の設定に変更する。
　機能設定：高←できるだけPCの許すスペック最大限のほうがいいです。
　あまりにもスペックが低いと処理に時間がかかり、エラーが起きました。
　起動設定：カスタム　幅：800　高さ：600　DPI：160
```
#### 仮想環境の構築
```
conda create -n GameAutoEnv python=3.7.5
```

#### 仮想環境に入る
```
conda activate GameAutoEnv
```

#### パッケージのアップデート
```
python -m pip install --upgrade pip
```

#### 必要パッケージのインストール
```
pip install pyautogui
pip install tqdm
pip install opencv_python
```

