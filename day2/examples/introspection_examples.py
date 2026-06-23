from day1.utils.introspection_utils import (
    IntrospectionUtility
)


def main():

    employee_name = "Karthik"

    print(
        IntrospectionUtility.get_type(
            employee_name
        )
    )

    print(
        IntrospectionUtility.get_id(
            employee_name
        )
    )

    print(
        IntrospectionUtility.get_attributes(
            employee_name
        )
    )


if __name__ == "__main__":
    main()