import json

with open('data.txt') as data_file:
    data = json.load(data_file)


# print (data)
storedPopularHours = []

for i in data['popularHours']:
  storedPopularHours.append(i['popularity'])

frameSize = 3




print(storedPopularHours)

start = 0
end = start + frameSize

start_final = 0
end_final = 0
avg_final = 0


print(len(storedPopularHours))
while end != len(storedPopularHours) + 1:
  total= sum(storedPopularHours[start:end])/3  

  if total > avg_final:
    end_final = end
    start_final = start
    avg_final = total

  start += 1
  end += 1

print(start_final)
print(avg_final)
print(end_final)