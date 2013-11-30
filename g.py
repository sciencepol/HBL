player_score=1234

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

number = binary_search(players,player_score,0,len(players)-1)

for i in range(number-5, number):
    print players[i]

for i in range(number+1, number+6):
    print players[i]

