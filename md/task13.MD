{
    "title":"百度前端学院Task13",
    "time":"2016-06-30 15:26"
}
------

#### 13. 
题目: 
要求:
    用户可以在输入框中输入任何内容，点击“确认填写”按钮后，用户输入的内容会显示在“您输入的值是”文字的右边。
``` html
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>IFE JavaScript Task 01</title>
      </head>
    <body>
    
      <label>请输入北京今天空气质量：<input id="aqi-input" type="text"></label>
      <button id="button">确认填写</button>
    
      <div>您输入的值是：<span id="aqi-display">尚无录入</span></div>
    
    <script type="text/javascript">
    
    (function() {
      /*    
      在注释下方写下代码
      给按钮button绑定一个点击事件
      在事件处理函数中
      获取aqi-input输入的值，并显示在aqi-display中
      */
    
    })();
    
    </script>
    </body>
    </html> 
```
分析：
``` javascript
test 1
(function() {
    var node_in=document.getElementById("aqi-input");
    var node_btn=document.getElementById("button");
    var node_display=document.getElementById("aqi-display");
    if(node_btn.attachEvent){
        node_btn.attachEvent("onclick",click);//IE Compatibility
    }else{
        node_btn.addEventListener("click",click,false);
    }
    function click(){
        var val=node_in.value.replace( /^(\s|\u00A0)+|(\s|\u00A0)+$/g, "" );//strip blank
        if(val.length>0){
            if(node_display.textContent != null){
                node_display.textContent=val;
            }else{
                node_display.innerHTML=val.replace(/[<>]/ig,"");//avoid XSS
            }
        }else{
            alert("Please complete the form!");
        }
    }
})();

test 2
 var button = document.getElementById("button");
  var dis = document.getElementById("aqi-display");
  var input = document.getElementById("aqi-input");
  function updateDisplay() {
    dis.innerText = parseFloat(input.value);
  }
  button.onclick = updateDisplay;
  input.onkeyup = function(evt) {
    if (evt.keyCode == 13) {
      updateDisplay();
    }
  }


```