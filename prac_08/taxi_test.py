from prac_08.taxi import Taxi


def main():
    prius_taxi = Taxi("Prius 1", 100)
    prius_taxi.start_fare()
    prius_taxi.drive(40)
    prius_taxi.get_fare()
    print(prius_taxi)

    prius_taxi.start_fare()
    prius_taxi.drive(100)
    prius_taxi.get_fare()
    print(prius_taxi)


main()
