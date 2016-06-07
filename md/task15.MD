{
    "title":"Task15",
    "time":"2016-06-07 15:26"
}
------

## 15. 
### 题目：
``` html
<!DOCTYPE>
<html>
  <head>
    <meta charset="utf-8">
    <title>IFE JavaScript Task 01</title>
  </head>
<body>

  <ul id="source">
    <li>北京空气质量：<b>90</b></li>
    <li>上海空气质量：<b>70</b></li>
    <li>天津空气质量：<b>80</b></li>
    <li>广州空气质量：<b>50</b></li>
    <li>深圳空气质量：<b>40</b></li>
    <li>福州空气质量：<b>32</b></li>
    <li>成都空气质量：<b>90</b></li>
  </ul>

  <ul id="resort">
    <!-- 
    <li>第一名：北京空气质量：<b>90</b></li>
    <li>第二名：北京空气质量：<b>90</b></li>
    <li>第三名：北京空气质量：<b>90</b></li>
     -->

  </ul>

  <button id="sort-btn">排序</button>

<script type="text/javascript">

/**
 * getData方法
 * 读取id为source的列表，获取其中城市名字及城市对应的空气质量
 * 返回一个数组，格式见函数中示例
 */
function getData() {
  /*
  coding here
  */

  /*
  data = [
    ["北京", 90],
    ["北京", 90]
    ……
  ]
  */

  return data;

}

/**
 * sortAqiData
 * 按空气质量对data进行从小到大的排序
 * 返回一个排序后的数组
 */
function sortAqiData(data) {

}

/**
 * render
 * 将排好序的城市及空气质量指数，输出显示到id位resort的列表中
 * 格式见ul中的注释的部分
 */
function render(data) {

}

function btnHandle() {
  var aqiData = getData();
  aqiData = sortAqiData(aqiData);
  render(aqiData);
}


function init() {

  // 在这下面给sort-btn绑定一个点击事件，点击时触发btnHandle函数

}

init();

</script>
</body>
</html>

``` 
参考以下示例代码，读取页面上已有的source列表，从中提取出城市以及对应的空气质量
将数据按照某种顺序排序后，在resort列表中按照顺序显示出来

分析：
``` javascript

/**
     * getData方法
     * 读取id为source的列表，获取其中城市名字及城市对应的空气质量
     * 返回一个数组，格式见函数中示例
     */
    function getData() {
        var source = document.getElementById("source");
        var arrLi = source.getElementsByTagName("li");
        var data = [];
        var str = "";
        for (var i = 0, len = arrLi.length; i < len; i++) {
            data[i] = [];
            str = arrLi[i].innerHTML;
            data[i][0] = str.substring(0, 2);
            data[i].push(parseInt(arrLi[i].getElementsByTagName("b")[0].innerHTML));
        }
        console.log(data);
        return data;
    }
    /**
     * sortAqiData
     * 按空气质量对data进行从小到大的排序
     * 返回一个排序后的数组
     */
    function sortAqiData(data) {
        function compare(value1, value2) {//二维数组排序
            return value1[1] - value2[1];
        }
        data.sort(compare);
        console.log(data);
        return data;
    }
    /**
     * render
     * 将排好序的城市及空气质量指数，输出显示到id位resort的列表中
     * 格式见ul中的注释的部分
     */
    function render(data) {
        var resort = document.getElementById("resort");
        var str = "";
        for (var i = 0, len = data.length; i < len; i++) {
            str += "<li>第"+ transfer((i + 1).toString()) + "名：" + data[i][0] + "空气质量：" + "<b>" + data[i][1] + "</b></li>";
        }
        resort.innerHTML = str;
    }
    function transfer(num) {
        var input = String(num);
        var unit = ["", "十", "百", "千", "万", "十", "百", "千", "亿"];
        var chineseNum = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"];
        var l = input.length;
        var a = [];
        var b = [];
        var result = "";
        for (var i = 0; i < l; i++) {
            a[i] = input.substr(i, 1);
            b[i] = chineseNum[a[i]];
            result += b[i] + unit[l - i - 1];
        }
        return result;
    }
    function btnHandle() {
        var aqiData = getData();
        aqiData = sortAqiData(aqiData);
        render(aqiData);
    }
    function init() {
        var btn = document.getElementById("sort-btn");
        addEvent(btn, "click", function () {
            btnHandle();
        });
    }
    function addEvent(element, type, handler) {
        if (element.addEventListener) {
            element.addEventListener(type, handler, false);
        } else if (element.attachEvent) {
            element.attachEvent("on" + type, handler);
        } else {
            element["on" + type] = handler;
        }
    }
    init();

```
