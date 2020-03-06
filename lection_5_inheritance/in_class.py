class WebSite:
    def __init__(self):
        self.info = "info"

    def retrieve_info(self):
        print("INFO accessed")

    def get_info_api(self):
        print(self.info)
    # def __correct_code(self, code):
    #     if code == 123:
    #         return "INFO"
    #     else:
    #         return "Wrong password"


class SecurityWebSite():
    def __init__(self):
        self.__site = WebSite()

    def retrieve_info(self, login, password):
        if login == 1 and password == 2:
            self.__site.retrieve_info()


# class Flyable:
#     def fly(self):
#         print("flying")
#
#
# class Movable:
#     def move(self):
#         print("moves")
#
#
# class Dambo(Flyable, Movable):
#     d = Dambo()
#     d.move()

if __name__ == '__main__':
    w = SecurityWebSite()
    w.retrieve_info(1, 2)