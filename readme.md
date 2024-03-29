# pyverify
![PyPI](https://img.shields.io/pypi/v/pyverify-xnz233)

## 简介

pyverify包是一个基于`tkinter`和`pyotp`库实现的GUI身份验证库
### 主要功能
- 为您的`py`文件能够快速使用TOTP认证的功能
- 提供一个简易的二维码生成器，可生成手机app可用的二维码

![](img/utils.jpg "生成器")

Tips:秘钥存储在运行目录下的`secdata.pass`文件中  
删除该文件会导致无法验证

## 使用教程

### 安装
你可以在终端执行pip来安装：  
`pip install pyverify-xnz233`

### 生成器


- 生成秘钥
```python
python -m pyverify.utils.py
```

- 读取秘钥
  - 方法一：各种2FA手机APP扫码
  - 方法二：查看运行目录下`secdata.pass`文件

### 验证程序
- 在任意py文件中的头部调用包中的`gui_verify()`:
```python
import pyverify
pyverify.gui_verify()

# Your code...
```
