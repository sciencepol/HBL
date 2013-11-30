

def binary_search(elements, target, low, high):
  mid = (low + high) // 2
  if low > high: 
    return high + 1
  elif elements[mid][1] == target:
    return mid + 1
  elif target < elements[mid][1]: 
    return binary_search(elements, target, low, mid-1)
  else: 
    return binary_search(elements, target, mid+1, high)

players.insert(binary_search(players,new_player[1],0,len(players)-1),new_player)
