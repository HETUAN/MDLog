# C#

1. cmd下执行类似的命令便可以生成exe程序：
``` bash
C:\Windows\Microsoft.Net\Framework\v4.0.30319\msbuild.exe hello.csproj
```

2. 生成exe文件之后复制到根目录，运行exe，便可以在Data目录下生成files.json (如果没有Data文件请自己创建不然会报错)

3. 打开index.html便可以查看

> 发布到IIS上时可能要添加允许请求的文件类型(ContentType)

# python

直接运行即可
``` bash
cd 项目根目录\Program\py
python MDLog.py
```

# node.js

待写

# BUG
1. 还未考虑更深层的目录的情况
2. 分类，标签等实现应当在浏览器端实现
3. 可参考的样式及页面设计 ->http://kuanghy.github.io/