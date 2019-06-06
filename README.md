# YnuNetworkAuthKeeper

YNUネットワーク認証を定期的に自動で行うシステム

## PreRequirements

### ChromeDriver
```
brew cask install chromedriver
```

### Python

適当に仮想環境を設定してください.

```
pip install -r requirements.txt
```

### 認証情報の記載
auth.json  
```
{
 "id": "xxxx",
 "password": "xxxx"
}


```

## 実行

```
$ python main.py
```