# Py-Peeper
A very simple (and tricky) observer pattern in Python.

## Installation
```python
pip install pypeeper
```


### Usage
#### Implementing an Observable class
Every class can be converted to observable just by subclassing it from
Observer. If class attribute "pattern" is overwritten with a valid regex
expression, only matching attributes defined within the class constructor will
be observed. Otherwise, all attributes will be observed.
```python
from pypeeper import Observable, Observer

class AnyClass(Observable):

    def __init__(self):
        self.attribute_a = False
        self.whatever_attr = 0

    def set_attribute(self, value):
        self.attribute_a = value
```
#### Implementing an Observer class
Any class can be Observer of all Observable classes defined as shown above. To
define how the class should react on Observable's changes, just override
"notify" method from Observer class.
```python
class ObserverClass(Observer):

    def notify(self, class_name, object_id, attribute_name, old, new):
        print(class_name, object_id, attribute_name, old, new)

```
#### Instantiate and play
```python
my_observable = AnyClass()
my_observer = ObserverClass()

my_observable.set_attribute(True)
my_observable.attribute_a = 10
my_observable.whatever_attr = None
```
#### Console output
```
>>> AnyClass 2448221506696 attribute_a False True
>>> AnyClass 2448221506696 attribute_a True 10
>>> AnyClass 2448221506696 whatever_attr 0 None
```
