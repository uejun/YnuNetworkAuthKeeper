# YnuNetworkAuthKeeper

YNUネットワーク認証を定期的に自動で行うスクリプト.  

YNUは12時間ごとに認証がリセットされる. したがって11時間ごとに
ブラウザを自動操作してログインをする.  

## 使用方法

### 起動  

```
python main.py
```  

スクリプトを実行すると, pythonプロセスが起動状態になります.  

### 終了  
Ctrl-Cで終了.

## 事前準備

### ChromeDriver
```
brew cask install chromedriver
```  

windowsの場合は適切にchromedriverをセットアップしてください.   

### Python

適当に仮想環境をセットアップしてください.

必要なpythonライブラリはrequirements.txtにまとめてあります.  

```
pip install -r requirements.txt
```

### 認証情報の記載
スクリプトのルートディレクトリにauth.jsonがあります.  
idとpasswordを上書きしてください.  
```
{
 "id": "xxxx",
 "password": "xxxx"
}


```
