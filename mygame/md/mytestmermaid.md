#tolevel
```mermaid
stateDiagram
[*] --> Still
Still --> [*]
Still --> Moving
Moving --> Still
Moving --> Crash
Crash --> [*]

```
---
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |



---
```mermaid
gantt
section Section
Completed :done,    des1, 2014-01-06,2014-01-08
Active        :active,  des2, 2014-01-07, 3d
Parallel 1   :         des3, after des1, 1d
Parallel 2   :         des4, after des1, 1d
Parallel 3   :         des5, after des3, 1d
Parallel 4   :         des6, after des4, 1d
    
```

```mermaid
classDiagram
Class01 <|-- AveryLongClass : Cool
<<interface>> Class01
Class09 --> C2 : Where am i?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
    class Class10 {
    <<service>>
    int id
    size'(')
    }
```

```mermaid
classDiagram
Class01 <|-- AveryLongClass : Cool
Class03 *-- Class04
Class05 o-- Class06
Class07 .. Class08
Class09 --> C2 : Where am i?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
Class08 <--> C2: Cool label
```

```mermaid



graph LR
 
client1-->|read / write|SVN((SVN server))
client2-->|read only|SVN
client3-->|read / write|SVN
client4-->|read only|SVN
client5(...)-->SVN
SVN---|store the data|sharedrive

```

流程图
 
```flow
st=>start: 流程开始
e=>end: 流程结束
 
op1=>operation: 选手准备
op2=>operation: 开始循环
op3=>operation: 执行循环语句
op4=>operation: 循环结束 
 
cond1=>condition: 准备好了么
cond2=>condition: 判断循环条件
 
 
st->op1->cond1
cond1(yes, right)->op2(right)->cond2
cond1(no)->op1
cond2(yes)->op3->cond2
cond2(no)->op4->e

```
```flow
st=>start: 开始
e=>end: 结束
c1=>condition: A
c2=>condition: B
c3=>condition: C
io=>inputoutput: D
st->c1(no)->e
c2(no)->e
c3(no)->e
c1(yes,right)->c2(yes,right)->c3(yes,right)->io
io->e
```


code:
```plantumlcode
@startuml
title 类图
note "类图部分符合示意" as comment
@enduml
```