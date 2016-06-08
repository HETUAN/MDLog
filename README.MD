
1. cmd下执行类似的命令：
``` bash
C:\Windows\Microsoft.Net\Framework\v4.0.30319\msbuild.exe hello.csproj
```
便可以生成exe程序

2. 生成exe文件之后复制到根目录，运行exe，便可以在Data目录下生成files.json (如果没有Data文件请自己创建不然会报错)

3. 打开index.html便可以查看

> 发布到IIS上时可能要添加允许请求的文件类型(ContentType)