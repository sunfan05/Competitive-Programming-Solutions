Limak, Bob = map(int, input().split())
count = 0
  
while Limak <= Bob:
    Limak = Limak * 3 
    Bob = Bob * 2
    count += 1
   
print(count)