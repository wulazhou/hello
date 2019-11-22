```mermaid
graph TD
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
```mermaid
	graph TB
	A[Apple]-->B{Boy}
	A---C(Cat)
	B.->D((Dog))
	C==喵==>D
	style A fill:#2ff,fill-opacity:0.1,stroke:#faa,stroke-width:4px
	style D stroke:#000,stroke-width:8px;
```
```mermaid
sequenceDiagram
	A-->B: works!
	B-->C: help!
```

::: warning
*here be dragons*
:::

```mermaid
	pie
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 15 
```



```mermaid
 classDiagram
      Animal <|-- Duck
      Animal <|-- Fish
      Animal <|-- Zebra
      Animal : +int age
      Animal : +String gender
      Animal: +isMammal()
      Animal: +mate()
      class Duck{
          +String beakColor
          +swim()
          +quack()
      }
      class Fish{
          -int sizeInFeet
          -canEat()
      }
      class Zebra{
          +bool is_wild
          +run()
      }
```



```mermaid
flow
	st=>start: 开始
	e=>end: 结束
	op1=>operation: 操作1 | past
	op2=>operation: 操作2 | current
	op3=>operation: 操作3 | future
	pa=>parallel: 多输出操作4 | approved
	cond=>condition: 确认？ | rejected
	
	st->op1->cond
	cond(true)->e	
	cond(no)->op2(right)->op3->pa(path1,right)->op1
	pa(path2,left) ->e
	st@>op1({"stroke":"Blue"})@>cond({"stroke":"Green"})@>e({"stroke":"Red","stroke-width":6,"arrow-end":"classic-wide-long"})
```


