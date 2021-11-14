def binary_search(list, item):
  # Za pomoc low i high kontrolujemy, ktra cz listy jest przeszukiwana.
  low = 0
  high = len(list) - 1

  # Dopki obszar poszukiwa nie zosta zawony do jednego elementu...
  while low <= high:
    # ...wybieramy rodkowy element.
    mid = (low + high) // 2
    guess = list[mid]
    # Znaleziono element.
    if guess == item:
      return mid
    # Strzelono za du liczb.
    if guess > item:
      high = mid - 1
    # Strzelono za ma liczb.
    else:
      low = mid + 1

  # Element nie istnieje.
  return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1

# Warto None w Pythonie oznacza nic, czyli wskazuje, e elementu nie znaleziono.
print(binary_search(my_list, -1)) # => None
