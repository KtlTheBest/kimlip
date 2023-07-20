import kimlip

evaluate = kimlip.evaluate

def test1():
    e = ["+", 1, 2]
    res = evaluate(["do", e], {})
    assert(res == 3)

def test2():
    e = ["-", 2, 1]
    res = evaluate(["do", e], {})
    assert(res == 1)

def test3():
    e = ["+", ["-", 3, 1], 2]
    res = evaluate(["do", e], {})
    assert(res == 4)

def test4():
    e1 = ["def", "foo", 4]
    e2 = ["+", 3, "foo"]
    res = evaluate(["do", e1, e2], {})
    assert(res == 7)

def test5():
    e1 = ["def", "foo", 4]
    e2 = ["def", "bar", 5]
    e3 = ["+", "foo", "bar"]
    res = evaluate(["do", e1, e2, e3], {})
    assert(res == 9)

def test6():
    e1 = ["def", "printHelloWorldAnd1",
           ["fn", [], ["do", ["print", "Hello World!"], 1]]]
    e2 = ["printHelloWorldAnd1"]
    res = evaluate(["do", e1, e2], {})
    assert(res == 1)

def run_tests():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

run_tests()
