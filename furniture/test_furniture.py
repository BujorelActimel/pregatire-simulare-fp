from furniture import Furniture

def test_furniture_code():
    furn1 = Furniture("masa", "masa1", 100, 9.99)
    assert furn1.code == 0

    furn2 = Furniture("masa", "masa2", 100, 10.99)
    assert furn2.code == 1

    furn3 = Furniture("masa", "masa3", 100, 13.99, code=3)
    assert furn3.code == 3


def test_furniture_type():
    furn1 = Furniture("masa", "masa1", 100, 9.99)
    assert furn1.type_ == "masa"


def test_furniture_name():
    furn1 = Furniture("masa", "masa1", 100, 9.99)
    assert furn1.name == "masa1"


def test_furniture_stock():
    furn1 = Furniture("masa", "masa1", 100, 9.99)
    assert furn1.stock == 100


def test_furniture_price():
    furn1 = Furniture("masa", "masa1", 100, 9.99)
    assert furn1.price == 9.99
