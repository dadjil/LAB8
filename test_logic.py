import pytest
from main import *


@pytest.xfail("Just by the conditions")
def test_equality():
    assert Truck() != Ship()

def test_truck_delivery():
    truck = Truck()
    assert truck.deliver() == "Доставка по суше (грузовиком)"

def test_ship_delivery():
    ship = Ship()
    assert ship.deliver() == "Доставка по морю (кораблем)"

def test_road_logistics_creates_truck():
    road_logistics = RoadLogistics()
    transport = road_logistics.create_transport()
    assert isinstance(transport, Truck)
    assert isinstance(transport, Transport)

def test_sea_logistics_creates_ship():
    sea_logistics = SeaLogistics()
    transport = sea_logistics.create_transport()
    assert isinstance(transport, Ship)
    assert isinstance(transport, Transport)

def test_logistics_is_abstract():
    with pytest.raises(TypeError):
        Logistics()

def test_transport_is_abstract():
    with pytest.raises(TypeError):
        Transport()


def test_road_logistics_delivery_plan(capsys):
    road_logistics = RoadLogistics()
    road_logistics.plan_delivery()
    captured = capsys.readouterr()
    assert "Планируем доставку: Доставка по суше (грузовиком)" in captured.out

def test_sea_logistics_delivery_plan(capsys):
    sea_logistics = SeaLogistics()
    sea_logistics.plan_delivery()
    captured = capsys.readouterr()
    assert "Планируем доставку: Доставка по морю (кораблем)" in captured.out


@pytest.mark.parametrize("logistics_class,expected_output", [
    (RoadLogistics, "Планируем доставку: Доставка по суше (грузовиком)"),
    (SeaLogistics, "Планируем доставку: Доставка по морю (кораблем)"),
])
def test_all_logistics_deliveries(logistics_class, expected_output, capsys):
    logistics = logistics_class()
    logistics.plan_delivery()
    captured = capsys.readouterr()
    assert expected_output in captured.out
