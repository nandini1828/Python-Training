def generate_coupons():

    print("\nGenerating Coupons")

    yield "SAVE10"

    yield "SAVE20"

    yield "FREESHIP"


def display_coupons():

    coupons = generate_coupons()

    for coupon in coupons:

        print(coupon)