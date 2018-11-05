import os


BASE_DIRS = os.path.dirname(__file__)

print(BASE_DIRS)
# 参数
options = {
    'port': 8001
}

#MysSql
mysql = {
    'host': '10.0.111.230',
    'user': 'root',
    'passwd': 'www5522522ni',
    'dbName': 'dushustore'
}

# 配置
setting = {
    'debug': True,
    'template_path':os.path.join(BASE_DIRS, 'template'),
    'static': os.path.join(BASE_DIRS, 'static'),
    "cookie_secret": "t63VyFj+T4uz+OwspKnQv50hXM9+skLTh1s1Tbaqa5Q=",

}

