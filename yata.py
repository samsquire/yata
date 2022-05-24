from collections import defaultdict
from functools import cmp_to_key

def conflict_sorter(left, right):
  sequence_left = [left]
  current_left = left
  while current_left.left != None:
    sequence_left.insert(0, current_left.left)
    current_left = current_left.left
  sequence_right = [right]
  current_right = right
 
  
  while current_right.left != None:
    sequence_right.insert(0, current_right.left)
    current_right = current_right.left
  print(sequence_left)
  print(sequence_right)
  if left in sequence_right:
    return sequence_right.index(left) - sequence_right.index(right)

  if right in sequence_left:
    return sequence_right.index(right) - sequence_right.index(right)
  
  return left.user - right.user
  return 0

class Edit():
  def __init__(self, user, identifier, origin, right, characters):
    self.user = user
    self.identifier = identifier
    self.origin = origin
    self.left = None
    self.right = right
    self.characters = characters
    self.origin_left = None

  def rollback(self):
    if self.origin_left:
      self.left = self.origin_left
      self.origin.right = self.original_origin_right 
      self.right = self.original_right
    
  def serialize(self):
    data = ""
    current = self
    
    while current.right != None:
      
      data += current.characters
      current = current.right
    data += current.characters
    return data
  def __repr__(self):
    return self.characters
  def insert(self, inserts):
    seen = defaultdict(list)
    previous = self
    for insert in inserts:
      if insert.origin.identifier in seen:
        for conflict in seen[insert.origin.identifier]:
          conflict.rollback()
        
        seen[insert.origin.identifier].append(insert)
        

        
        
        seen[insert.origin.identifier].append(insert)
    character_conflict = defaultdict(list)
    for key, conflicts in seen.items():
      for conflict in conflicts:
        character_conflict[conflict.characters].append(conflict)
 
    unsorted_conflicts = []
    for key, conflicts in seen.items():
      
        for conflict in conflicts:
          unsorted_conflicts.append(conflict)

    for conflict in unsorted_conflicts:
      conflict.left = conflict.origin
    print("unsorted conflicts")
    print(unsorted_conflicts)
    sorted_conflicts = sorted(unsorted_conflicts, key=cmp_to_key(conflict_sorter))
    sorted_conflicts[0].left = sorted_conflicts[0].origin
    sorted_conflicts[0].origin.right = sorted_conflicts[0]
    original_end = sorted_conflicts[-1].right
    print("original end")
    print(original_end)
    print("sorted conflicts")
    print(sorted_conflicts)
    previous = sorted_conflicts[0]
    
    for conflict in sorted_conflicts[1:]:
      conflict.left = previous
      print(conflict)
      previous.right = conflict
      previous = conflict
    previous.right = original_end
    print(original_end.right)
        

beginning = Edit(0, 0, None, None, "")
end = Edit(0, -1, None, None, "")
beginning.right = end
end.left = beginning

y = Edit(0, 1, beginning, end, "Y")

a = Edit(0, 2, y, end, "A")



beginning.insert([
  y,
  a
      ])
conflicts = [
Edit(0, 3, a, end, "T"),
Edit(1, 4, a, end, "T")
            ]

A = Edit(0, 3, a, end, "A")
B = Edit(0, 3, A, end, "B")
C = Edit(0, 4, B, end, "C")

X = Edit(1, 4, a, end, "X")
Y = Edit(1, 4, X, end, "Y")
Z = Edit(1, 4, Y, end, "Z")

conflicts = [

C, A, B, Z, Y, X
            ]
a.insert(conflicts)
print(beginning.serialize())
