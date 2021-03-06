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


# 请用Book类实例化一个python_book对象，并调用info()方法，输出信息
python_book = Book('Python Book', 'Amy Chen', '978-7-111-64598-6', 89.00)
python_book.info()