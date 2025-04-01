from sys import *

intv, floatv, boolv, strv, listv, tupv, dictv, setv = [None] * 8

if __name__ == '__main__':
    intv = 0
    floatv = 0.0
    boolv = True
    strv = ""
    listv = []
    tupv = ()
    dictv = {}
    setv = set()

    print("int형 기본 크기-->", getsizeof(intv))
    print("float형 기본 크기-->", getsizeof(floatv))
    print("bool형 기본 크기-->", getsizeof(boolv))
    print("str형 기본 크기-->", getsizeof(strv))
    print("list형 기본 크기-->", getsizeof(listv))
    print("tuple형 기본 크기-->", getsizeof(tupv))
    print("dictionary형 기본 크기-->", getsizeof(dictv))
    print("set형 기본 크기-->", getsizeof(setv))
