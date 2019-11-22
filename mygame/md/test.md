# d

## d

 - [ ] 1定义节点
名称=>类型：内容
类型有：start
        end
        operation 
        subroutine （循环）
        condition
        inputoutput （输入输出）
        parallel 允许多个流同时发生
        eg： st=>start: 注册
              e=>end: 结束
op1=>operation: 登陆
op2=>operation: 购买并登陆
cond=>condition: 是否已登陆购买
 - [ ] 2节点关系
  ->   eg：st->op1->cond
 - [ ] 3判断型节点
  根据yes 和no 指向 不同节点
cond(yes)->e
cond(no)->op2->e
##判断型节点 根据yes 和no 指向 不同节点

```flow
st=>start: 注册
e=>end: 结束
op1=>operation: 登陆
op2=>operation: 购买并登陆
cond=>condition: 是否已登陆购买
st->op1->cond
cond(yes)->e
cond(no)->op2->e
``` 
```mermaid
  graph LR
st[注册印象笔记]-->a
a{是否已经购买马克飞象}
a-->|是|b1(您已购买马克飞象可以使用markdown语法)
a-->|否|b2(您还未能成功购买马克飞象但你可以免费试用10天)
b1-->c[欢迎使用马克飞象]
b2-->d{是否要购买马克飞象}
d-->|是|e1(您已成功购买马克飞象欢迎使用)
e1-->c
d-->|否|e2(试用10天后将会到期欢迎购买)
```

```mermaid
graph LR
    id1(Start)-->id2(Stop)
    style id1 fill:#f9f,stroke:#500,stroke-width:4px
    style id2 fill:#ccf,stroke:#f66,stroke-width:2px,stroke-dasharray: 5, 5
```



​```sequence
Title: Here is title
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
​```


[](http://github.com)

### d
![](/mygame/yudi.jpg)

colspan `>` or `empty cell`:

| a | b |
|---|---|
| > | 1 |

rowspan `^`:

#dd

:smile:
:fa-car:

30^th^

H~~0
''' if TRUE: 
        run()
    else if:
        play()
'''
```mermaid
graph TD
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

$f(x) =sin(x) +12$
<img src='https://g.gravizo.com/svg?
 digraph G {
   main -> parse -> execute;
   main -> init;
   main -> cleanup;
   execute -> make_string;
   execute -> printf
   init -> make_string;
   main -> printf;
   execute -> compare;
 }
'/>

![Alt text](https://g.gravizo.com/source/custom_mark10?https%3A%2F%2Fraw.githubusercontent.com%2FTLmaK0%2Fgravizo%2Fmaster%2FREADME.md)
<details> 
<summary></summary>
custom_mark10
  digraph G {
    size ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf};
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }
custom_mark10
</details>

---------------------------------
![Alt text](https://g.gravizo.com/source/svg/custom_mark12?https%3A%2F%2Fraw.githubusercontent.com%2FTLmaK0%2Fgravizo%2Fmaster%2FREADME.md)
<details> 
<summary></summary>
custom_mark12
/**
*Structural Things
*@opt commentname
*@note Notes can
*be extended to
*span multiple lines
*/
class Structural{}

/**
*@opt all
*@note Class
*/
class Counter extends Structural {
        static public int counter;
        public int getCounter();
}

/**
*@opt shape activeclass
*@opt all
*@note Active Class
*/
class RunningCounter extends Counter{}
custom_mark12
</details>
---
***


![Alt text](https://g.gravizo.com/source/svg/thiisthemark?http%3A%2F%2Fwww.gravizo.com)
![Alt text](http://www.gravizo.com/img/1x1.png#

thiisthemark        
@startuml
object Object01
object Object02
object Object03
object Object04
object Object05
object Object06
object Object07
object Object08

Object01 <|-- Object02
Object03 *-- Object04
Object05 o-- "4" Object06
Object07 .. Object08 : some labels
@enduml
thiisthemark        
        



