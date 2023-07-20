# kimlip
Know It Means Lisp In Python

# Why?
Because I forgot that Hy existed. But then again, I thought that it was interesting, that one can embed Lisp into Python just by treating the code as data.

# How?
```python
import kimlip

evaluate = kimlip.evaluate

evaluate(["do", ["print", "Hello World!]], {})
```

# I want more!

There are some examples in the `tests.py` file. I plan to add more capabilities soon. But I just wanted to get it out there.

# What about Kim Lip?
Who knows 👀.
