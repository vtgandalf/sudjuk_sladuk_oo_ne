from car import Car
from path import Path
from street import Street
from intersection import Intersection
from traffic_light import TrafficLight

def read_input(path):
  file = open(path, "r")
  duration, num_intersections, num_streets, num_cars, points_per_car = map(lambda x: int(x), file.readline().replace("\n", "").split(" "))
  streets = []
  cars = []

  for i in range(num_streets):
    curr_line = file.readline().replace("\n", "").split(" ")
    start_intersection = int(curr_line[0])
    end_intersection = int(curr_line[1])
    street_name = curr_line[2]
    street_time = int(curr_line[3])

    streets.append({
      "id": i,
      "start_intersection": start_intersection,
      "end_intersection": end_intersection,
      "street_name": street_name,
      "street_time": street_time
    })
  
  for j in range(num_cars):
    curr_line = file.readline().replace("\n", "").split(" ")
    car_streets = []

    for _ in range(len(curr_line)):
      car_streets.append(curr_line[j + 1])

    cars.append({
      "id": j,
      "car_streets": car_streets
    })

  return {
    "duration": duration,
    "num_intersections": num_intersections,
    "num_streets": num_streets,
    "num_cars": num_cars,
    "points_per_car": points_per_car,
    "streets": streets,
    "cars": cars
  }


def main():
  input = read_input("a.txt")
  streets = []
  intersections = []
  cars = []
  points_per_car = []
  for street in input["streets"]:
    streets.append(Street(street["id"], street["street_name"], street["street_time"], [street["start_intersection"], street["end_intersection"]]))

  for id in range(input["num_intersections"]):
    intersections.append(Intersection(id, [], []))

  for car in input["cars"]:
    cars.append(Car(car["id"], car["car_streets"], []))



  # print(input)

if __name__ == "__main__":
    main()
