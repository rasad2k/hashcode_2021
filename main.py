#!/bin/python3
import sys


def read_files(file):

    file1 = open(file, 'r')
    lines = file1.readlines()
    intro = lines[0].split()
    streets = {}

    for tmp in lines[1:int(intro[2])+1]:
        line = tmp.split()
        streets[line[2]] = {
            "start": line[0],
            "end": line[1],
            "time": int(line[3])
        }

    cars = []

    for tmp in lines[int(intro[2])+1:]:
        line = tmp.split()
        car = {
            "path": line[1:int(line[0])+1],
            "duration": 0
        }
        cars.append(car)

    return intro, streets, cars


if __name__ == "__main__":
    intro, streets, cars = read_files(sys.argv[1])
    intersections = {}

    for street in streets:

        if streets[street]["end"] not in intersections:
            intersections[streets[street]["end"]] = {
                "out_str": "",
                street: 0,
                'street_count': 0
            }
        else:
            intersections[streets[street]["end"]][street] = 0

    for car in cars:

        for street in car["path"]:
            car["duration"] += streets[street]["time"]

    cars = sorted(cars, key=lambda x: x["duration"])

    for car in cars:
        time = 0
        tmp_intersections = intersections

        for street in car["path"]:
            time += streets[street]["time"]

            if intersections[streets[street]["end"]][street] == 0:
                intersections[streets[street]["end"]
                              ][street] = 1
                intersections[streets[street]["end"]
                              ]["out_str"] += f"{street} 1\n"
                intersections[streets[street]["end"]]["street_count"] += 1
            else:
                continue

    c = 0
    res = ""

    for key, value in intersections.items():

        if value["out_str"] == "":
            continue
        else:
            res += f"{key}\n{value['street_count']}\n{value['out_str']}"
            c += 1

    res = "\n".join([s for s in res.split("\n") if s])
    print(f"{c}\n{res}")
