class LNode():
  def __init__(self, data, next_node = None) -> None:
    self.data = data
    self.next = next_node

class TNode():
  def __init__(self, data, left, right) -> None:
    self.data = data
    self.left = left
    self.right = right

class Directorio():
  def __init__(self, name, parent = None) -> None:
    self.name = name
    self.files = []
    self.parent = parent

class File():
  def __init__(self, name, weight) -> None:
    self.name = name
    self.weight = weight
