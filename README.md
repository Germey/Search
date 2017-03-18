## 百度必应搜索接口

### 测试接口

#### 百度

##### 接口

http://211.159.152.173:5000/baidu

##### 请求方式

POST

##### 参数Form Data

* keyword：关键字，任意类型
* total: 要获取的数量 

#### 必应

##### 接口

http://211.159.152.173:5000/bing

##### 请求方式

POST

##### 参数Form Data

- keyword：关键字，任意类型
- total: 要获取的数量 

### 返回结果

#### 类型

json

#### 字段

* length: 结果长度
* content: 搜索结果列表
* content.title: 搜索结果标题
* content.href: 搜索结果标题链接
* content.abstract: 搜索结果摘要
* content.url: 搜索结果下方短链接
* content.snapshot: 搜索结果快照链接，仅百度接口提供

### 部署

#### 安装Python3

##### Ubuntu

```
sudo apt-get install build-essential python3-dev libssl-dev libffi-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev
sudo apt-get install python3
sudo apt-get install python3-pip
```

##### CentOS

```
sudo yum groupinstall development tools
sudo yum install python34-devel epel-release libxslt-devel libxml2-devel openssl-devel
sudo yum install python34
sudo yum install python34-setuptools
sudo easy_install-3.4 pip
```

#### 安装库

```
pip3 install requests flask pyquery
```

#### 下载并运行

```
git clone https://github.com/Germey/Search.git
ce Search
python3 web.py
# 下方命令为服务器进程守护运行
nohup python3 web.py &
```

