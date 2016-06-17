{
    "title":"百度前端学院Task14",
    "time":"2016-06-29 15:26"
}
------

## 14. 
### 题目：
``` html
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>IFE JavaScript Task 01</title>
      </head>
    <body>
    
      <h3>污染城市列表</h3>
      <ul id="aqi-list">
    <!--   
        <li>第一名：福州（样例），10</li>
        <li>第二名：福州（样例），10</li> -->
      </ul>
    
    <script type="text/javascript">
    
    var aqiData = [
      ["北京", 90],
      ["上海", 50],
      ["福州", 10],
      ["广州", 50],
      ["成都", 90],
      ["西安", 100]
    ];
    
    (function () {
    
      /*
      在注释下方编写代码
      遍历读取aqiData中各个城市的数据
      将空气质量指数大于60的城市显示到aqi-list的列表中
      */
    
    })();
    
    </script>
    </body>
    </html>
```
说明：参考示例代码，页面加载后，将提供的空气质量数据数组，按照某种逻辑（比如空气质量大于60）进行过滤筛选，最后将符合条件的数据按照一定的格式要求显示在网页上
### 分析:
本题目我想到的三个地方有：数组的排序，数组的过滤和DOM操作。
1. 数组排序
方式1. 遍历数组通过各种排序算法进行排序
方式2. Js的数组对象已有排序方法 sort()，可以直接使用
``` javascript
    var aqiData = [
      ["北京", 90],
      ["上海", 50],
      ["福州", 10],
      ["广州", 50],
      ["成都", 90],
      ["西安", 100]
    ];
    //points.sort(function(a,b){return a-b});
    aqiData.scort(function(a,b){return a[1]-b[1];})
    // 从大到小还是从小到大取决于委托函数中的比较方法
    //此外还有下面两种方法，分别是正序和逆序
    aqiData.sort();
    aqiData.reverse();
```
2. 数组的过滤
方式1. 数组的过滤同样可以自己使用循环遍历来解决
方式2. 数组对象依然有方法的实现filter()
``` javascript
    var aqiData = [
      ["北京", 90],
      ["上海", 50],
      ["福州", 10],
      ["广州", 50],
      ["成都", 90],
      ["西安", 100]
    ];
    //points.sort(function(a,b){return a-b});
    aqiData.filter(function(item){return item[1]>60;}) 
```
3. DOM 操作
方式1. 创建DOM节点，然后附加到父节点
``` javascript
  var oLi = document.createElement("li");
  oLi.innerHTML = '第'+arr[i]+'名：'+aqiData[i][0]+','+aqiData[i][1];
  oList.appendChild(oLi);
```
方式2. 直接拼接html，然后设置父节点的innerHTML属性

综合来看通过上面的方式可以拼凑出很多的方法：

``` javascript
var aqiData = [
      ["北京", 90],
      ["上海", 50],
      ["福州", 10],
      ["广州", 50],
      ["成都", 90],
      ["西安", 100]
    ];
    
// test 1 先筛选再过滤再绑定
 //先选出空气质量指数大于60的城市（减少排序的次数）
var sortCount = aqiData.filter(function(item){
    return (item[1] > 60);
});
//对大于60的城市进行排序
sortCount.sort(function(a, b){
    return b[1] - a[1];
});
var aqiList = document.getElementById('aqi-list');
//将结果显示
for(var i = 0; i < sortCount.length; i++){
    aqiList.innerHTML += '<li>第' + (i + 1) + '名：' + sortCount[i][0] + '(样例) , ' + sortCount[i][1] + '</li>';
}

// test 2 先从大到小排序然后再遍历绑定是判断
 //sort 从大到小
aqiData.sort(function(a,b){
  return b[1]-a[1];
});
oList.innerHTML = "";
for(var i=0;i<aqiData.length;i++){
  if(aqiData[i][1]>60){
    var oLi = document.createElement("li");
    oLi.innerHTML = '第'+arr[i]+'名：'+aqiData[i][0]+','+aqiData[i][1];
    oList.appendChild(oLi);
  }
}
// test 3 这个链式操作简洁，而且能防止过多的操作DOM
var chineseNumbers = ["一","二","三","四","五","六","七","八","九","十"];
  
  var contentStr = "";
  aqiData.filter(function(element){return element[1] > 60;})
         .sort(function (d1,d2){ return d2[1] - d1[1]; })
         .forEach(function (element,index){
    contentStr += "<li>第" + chineseNumbers[index] + "名：" + element[0] + "，" + element[1] + "</li>";    
  });
  
  document.getElementById("aqi-list").innerHTML = contentStr;
// test 4 
 
var chineseNumbers = ["一","二","三","四","五","六","七","八","九","十"];
  
  var contentStr = "";
  aqiData.sort(function (d1,d2){ return d2[1] - d1[1]; })
         .forEach(function (element,index){
         if(element[1]>=60)
         {
         contentStr += "<li>第" + chineseNumbers[index] + "名：" + element[0] + "，" + element[1] + "</li>";  
         }else
         {
         break;
         }  
  });
  
  document.getElementById("aqi-list").innerHTML = contentStr;

```

 

