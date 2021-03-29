from .douban import author_clear

def test_author_clear():

    assert author_clear("张三[美]") == "张三"
    assert author_clear("李四【中】") == "李四"
    assert author_clear("(美)李四[意]蛋【韩】") == "李四蛋"