{
    "title":"10个C#特性",
    "time":"2015-05-07 18:26"
}
------
#10个C#特性

### 1. async/awqit
使用 async / await 模式，可以在执行代码块操作的时候不会阻塞 UI 或者当前的线程。即使该操作被某些执行动作延迟了（比如一个 web 请求），async / await 模式也会继续执行后续的代码。(可以在响应web请求和桌面操作时使用防止卡顿)
[更多关于 async / await 模式的内容](https://msdn.microsoft.com/zh-cn/library/hh191443.aspx) 

### 2. 对象 / 数组 / 集合的初始值设定项（initializers）
通过使用对象、数组、集合的初始值设定项，可以很容易地创建类、数组和集合的实例：
``` cs
// 示例类
public class Employee {
    public string Name {get; set;}
    public DateTime StartDate {get; set;}
}

// 使用初始值设定项创建员工实例
Employee emp = new Employee {Name="John Smith", StartDate=DateTime.Now()};
```
上述示例中的代码在单元测试中可能非常有帮助，不过在有些情况下也应该避免使用它，比如应该通过构造函数来进行类的实例化的时候。[更多关于初始值设定项的内容](https://msdn.microsoft.com/zh-cn/library/bb384062.aspx)

### 3. Lambda 表达式、谓词委托（predicates）、委托（delegates）和闭包（closures）
这些特性在很多情况下都是非常必要的（比如使用 Linq 的时候），请务必学习在何时以及如何使用它们。(在使用时可以将其作为参数传入函数进行使用)
[更多关于 Lambda 表达式、谓词委托、委托和闭包的内容](http://www.codeaddiction.net/articles/13/lambda-expressions-delegates-predicates-and-closures-in-c ) 

### 4. ?? – null 合并运算符（Null coalescing operator）
当表达式左侧不为 null 的时候，?? 运算符返回其左侧的值，否则返回其右侧的值：
``` cs
// 可能是 null
var someValue = service.GetValue();
var defaultValue = 23
 
// 如果 someValue 是 null 的话，result 为 23
var result = someValue ?? defaultValue;
```
?? 运算符可以用于链式操作：
``` cs
string anybody = parm1 ?? localDefault ?? globalDefault;
```
它也可以将可空类型转换为非可空类型：
``` cs
var totalPurchased = PurchaseQuantities.Sum(kvp => kvp.Value ?? 0);
```
[更多关于 ?? 运算符的内容](https://msdn.microsoft.com/zh-cn/library/ms173224.aspx)

### 5. $”{x}” – 内插字符串（String Interpolation）- C# 6
C# 6 的一个新特性，可以通过更加高效和优雅的方式来进行字符串拼接：
``` cs
// 传统方式
var someString = String.Format("Some data: {0}, some more data: {1}", someVariable, someOtherVariable);

// 新的方式
var someString = $"Some data: {someVariable}, some more data: {someOtherVariable}";
```
也可以在大括号中写 C# 表达式，这让它变得非常强大。

### 6. ?. – null 条件运算符（Null-conditional operator） – C# 6

null 条件运算符使用起来如下所示：
``` cs
// 如果 customer 或 customer.profile 或 customer.profile.age 为 null 的话，结果都是 null
var currentAge = customer?.profile?.age;
```
不再会发生 NullReferenceExceptions 了！
[更多关于 ?. 运算符的内容](https://msdn.microsoft.com/zh-cn/library/dn986595.aspx)

### 7. nameof 表达式 – C# 6

新的 nameof 表达式可能看上去没那么重要，不过它确实也有其用武之地。在使用自动重构工具（比如 Resharper）时，你可能会需要通过参数的名字来表示它：
``` cs
public void PrintUserName(User currentUser)
{
    // 在重命名 currentUser 的时候，重构工具可能会遗漏在文本中的这个变量名
    if(currentUser == null)
        _logger.Error("Argument currentUser is not provided");

    //...
}
```
现在你可以这样来写：
``` cs
public void PrintUserName(User currentUser)
{
    // 重构工具不会漏掉这个
    if(currentUser == null)
        _logger.Error($"Argument {nameof(currentUser)} is not provided");

    //...
}
```
[更多关于 nameof 表达式的内容](https://msdn.microsoft.com/zh-cn/library/dn986596.aspx)

### 8. 属性初始值设定项 – C# 6
你可以通过属性初始值设定项，在声明一个属性的时候指定一个初始值：
``` cs
public class User
{ 
    public Guid Id { get; } = Guid.NewGuid();  
    // ...
}
```
使用属性初始值设定项的一个好处，就是你不必声明一个 setter 方法，从而使得该属性成为不可变的（immutable）。属性初始值设定项可以和 C# 6 的主构造函数（Primary Constructor）语法配合使用。（译者注：Primary Constructor 语法可以让你在定义一个类的同时，在类名之后立即指定一个带参数的构造函数）

### 9. as / is 运算符
is 运算符用来判断一个实例是否是特定类型的，比如你想看一下类型转换是否是可行的：
``` cs
if (Person is Adult)
{
    //do stuff
}
```
as 运算符会试图将某个对象转换为某个特定类的实例。如果无法转换的话会返回 null：
``` cs
SomeType y = x as SomeType;
if (y != null)
{
    //do stuff
}
```

### 10. yield 关键字

你可以通过 yield 关键字来返回 IEnumerable 接口的数据项。下面的示例会返回 2 的次方（比如直到 8 次方：2、4、8、16、32、64、128、256）：
``` cs
public static IEnumerable<int> Power(int number, int exponent)
{
    int result = 1;
    for (int i = 0; i < exponent; i++)
    {
      result = result * number;
      yield return result;
    }
}
```
如果使用得当的话，yield 会变得非常强大。它使得你延迟生成序列中的对象，比如当系统不需要枚举整个集合的时候，可以按需停止。
> ref => http://blog.jobbole.com/99599/

