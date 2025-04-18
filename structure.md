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

---

## ✅ Submission Checklist ✅

| ✅ Task | Status |
|--------|--------|
| `/src` with class diagram code | ✅ |
| `/creational_patterns` folder | ✅ |
| `/tests` with unit tests | ✅ |
| `README.md` with rationales | ✅ |
| `CHANGELOG.md` | ✅ |
| GitHub Issues / Project Board updated | ✅ |
| Mermaid diagram for overview | ✅ |

---
