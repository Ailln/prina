# prina: print python variable with the variable name.

🦥 打印 Python 变量时，带着变量名称。

## 缘起

不知道你有没有这样的烦恼，在没有 IDE 的情况下做调试时，都会写一堆打印信息来查看数据是否准确。

比如：
```python
a = "1"
b = 2
c = True
print(a, b, c)
# 1 2 True
```

如果直接这样打印，在控制台的输出中就很难区分不同变量的值。

因此需要安装下面的方式来书写，其中就**有很多变量名需要写两遍。**

```python
a = "1"
b = 2
c = True
print("a: {} b: {} c: {}".format(a, b, c))
# or (Python3.6+ 支持的语法)
print(f"a: {a} b: {b} c: {c}")
# a: 1 b: 2 c: True
```

那么有没有一种方法**可以打印 Python 变量时，带着变量名称呢？**

我找了半天 Python 的内置函数，发现都无法完成这一功能，于是就有了 `prina` 这个库。

> prina = print + name

## 使用方法

```python
from prina import prina

a = "1"
b = 2
c = True

prina(a, b, c)
# a: 1 b: 2 c: True
```

## 其他

在 `Python 3.8` 中，你可以使用 `f-string` 来调试文档：

```python
a = "1"
b = 2
c = True

print(f"{a=} {b=} {c=}")
# a=1 b=2 c=True
```

## 许可

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
