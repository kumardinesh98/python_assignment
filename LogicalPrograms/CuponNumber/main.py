from LogicalPrograms.CuponNumber.CuponCode import CuponCode


class Main:
    cupon_code = []

    def user(self):
        while True:
            try:
                total = int(input("enter total number of cupon code needed"))
                self.add_cupon(total)
                break
            except ValueError:
                print("please enter a valid number")

    def add_cupon(self, total):
        random_code = CuponCode();
        while len(self.cupon_code) != total:
            code = random_code.random_cupon()

            if code not in self.cupon_code:
                self.cupon_code.append(code)
        print(self.cupon_code)


main = Main()
main.user()