def flatten_office():

    print("\nFlatten Office Floors")

    office = [

        ["John","Alice"],

        ["David","Emma"],

        ["Mike","Sophia"]

    ]

    employees = [

        person

        for floor in office

        for person in floor

    ]

    print(employees)


def seating_layout():

    print("\nOffice Seating Layout")

    layout = [

        [

            "Empty"

            for seat in range(4)

        ]

        for row in range(3)

    ]

    for row in layout:

        print(row)