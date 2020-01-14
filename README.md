# python-swagger-docker
基于Docker的swagger API 管理框架


## 1. 构建镜像
`
docker build -t aturx/api-swagger .
`

## 2. 启动实例

`
docker run -d -p 5000:5000 aturx/api-swagger
`

## 3. 访问API 页面
 `
访问API 接口在线地址 ：  http://localhost:5000/apidocs/
 `

## 4. 参考文档地址
`
https://github.com/flasgger/flasgger
`

## 5. 目录结构
`
src  业务逻辑代码
v1   API在线接口 V1 版本
main.py 主运行函数
`

## 6. 开发完成 导出 requirements.txt
`
pipreqs . --encoding=utf8
`

### 7. Docker hub 地址
下载并启动
`
docker pull 167006261/api-swagger
docker run -d -p 5000:5000 167006261/api-swagger
`

然后访问
`
http://localhost:5000/apidocs/
`