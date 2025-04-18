```mermaid
classDiagram
class DatabaseConnection {
    -instance: DatabaseConnection
    +__new__(): DatabaseConnection
}
DatabaseConnection <|-- Singleton

class PizzaBuilder {
    +add_cheese()
    +add_pepperoni()
    +add_veggies()
    +build()
}
PizzaBuilder --> Pizza

class GUIFactory
GUIFactory <|-- WindowsFactory
GUIFactory <|-- MacFactory
WindowsFactory --> WindowsButton
MacFactory --> MacOSButton


