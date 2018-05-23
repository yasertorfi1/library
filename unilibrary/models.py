from django.db import models


class Person(models.Model):
    student_number = models.BigIntegerField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=120)


class BookType(models.Model):
    name = models.CharField(max_length=128)
    stock_no = models.IntegerField()


class Book(models.Model):
    issn = models.BigIntegerField()
    print_year = models.IntegerField()
    author = models.CharField(max_length=120)
    translator = models.CharField(max_length=120)
    book_title = models.ForeignKey(BookType, on_delete=models.CASCADE)


class Reservation(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Person, on_delete=models.CASCADE)


class Borrow(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()


class Donate(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Person, on_delete=models.CASCADE)
