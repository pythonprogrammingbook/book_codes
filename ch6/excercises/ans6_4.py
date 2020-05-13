# 定义一个Book类，属性：name、author、isbn、publisher和price
class Book():
    """Define a Book class

    """
    def __init__(self, name, author, isbn, price, publisher="ABC Press"):
        """Init the properties

        Args:
            name (string): [Book's name]
            author (string): [Book's author]
            isbn (string): [Book's isbn]
            price (float): [Book's price]
            publisher (str, optional): [description]. Defaults to "ABC Press".
        """
        self.name = name
        self.author = author
        self.isbn = isbn
        self.price = price
        self.publisher = publisher

    def info(self):
        print(f"The book's name:{self.name}; author:{self.author}; " \
              f"isbn:{self.isbn}; price:{self.price}; publisher:{self.publisher}")


# 请定义一个TextBook类，从Book类继承；教材类是普通书籍类的一个子类
# 拥有自己的属性：courseware(课件数，int)和exercise(练习题数: int)
# 重载info()方法，增加courseware和exercise信息输出


class TextBook(Book):  # 从Book类继承
    """TextBook(教材类)是普通书籍类的一个子类
       从Book类继承
    """
    def __init__(self,
                 name,
                 author,
                 isbn,
                 price,
                 publisher="ABC Press",
                 courseware=13,
                 exercise=200):
        super().__init__(name, author, isbn, price, publisher)
        self.courseware = courseware  # 教材会配套课件
        self.exercise = exercise  # 教材会配套习题

    def info(self):
        super().info()
        print(
            f"The book's courseware:{self.courseware}; exercise:{self.exercise}"
        )

    # set_courseware()方法，用于设置课件数量
    def set_courseware(self, nums):
        self.courseware = nums  # 设置课件数量

    # get_ courseware()方法，用于获得课件数量
    def get_courseware(self):
        return self.courseware  # 获得课件数量


# 实例化一个python_textbook对象，并调用info()方法，输出信息
python_textbook = TextBook('Python TextBook', 'Amy Chen', '978-7-111-64598-6',
                           89.00, "XYZ Press", 20, 300)
python_textbook.set_courseware(24)  # 课件数量设置为24
python_textbook.info()