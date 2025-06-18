from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        return "Доставка по суше (грузовиком)"


class Ship(Transport):
    def deliver(self):
        return "Доставка по морю (кораблем)"


class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        result = transport.deliver()
        print(f"Планируем доставку: {result}")


class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


def client_code(logistics: Logistics):
    logistics.plan_delivery()


if __name__ == "__main__":
    print("Доставка по суше:")
    client_code(RoadLogistics())

    print("\nДоставка по морю:")
    client_code(SeaLogistics())