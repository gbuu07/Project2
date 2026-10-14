# Gia Buu Luong
# Aymaan Changai Mangalote
# ECE 241 - Project 2: Preliminary

class Link:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)


class BigNumberLL:
    def __init__(self, number):
        self.first = None
        self.last = None
        self.size = 0
        self.positive = True

        if not isinstance(number, str):
            raise TypeError("BigNumberLL expects a string")

        if number.startswith("-"):
            self.positive = False
            number = number[1:]

        if not number or any(ch not in "0123456789" for ch in number):
            raise ValueError("Enter digits with an optional leading minus sign")

        for ch in number:
            self.insertLast(int(ch))

        self.trimFront()

    def insertLast(self, data):
        new_link = Link(data)

        if self.last is None:
            self.first = new_link
            self.last = new_link
        else:
            new_link.prev = self.last
            self.last.next = new_link
            self.last = new_link

        self.size += 1

    def insertFirst(self, data):
        new_link = Link(data)

        if self.first is None:
            self.first = new_link
            self.last = new_link
        else:
            new_link.next = self.first
            self.first.prev = new_link
            self.first = new_link

        self.size += 1

    def deleteFirst(self):
        if self.first is None:
            return None

        removed = self.first
        self.first = removed.next

        if self.first is None:
            self.last = None
        else:
            self.first.prev = None

        removed.next = None
        removed.prev = None
        self.size -= 1

        return removed.data

    def trimFront(self):
        while self.size > 1 and self.first.data == 0:
            self.deleteFirst()

        if self.size == 1 and self.first.data == 0:
            self.positive = True

    def __str__(self):
        parts = []
        current = self.first
        remaining = self.size

        while current is not None:
            parts.append(str(current.data))
            remaining -= 1

            if remaining > 0 and remaining % 3 == 0:
                parts.append(",")

            current = current.next

        sign = "" if self.positive else "-"
        return "[" + str(self.size) + "] " + sign + "".join(parts)

    def __gt__(self, other):
        if self.positive and not other.positive:
            return True
        if not self.positive and other.positive:
            return False

        if self.size != other.size:
            bigger_size_wins = self.size > other.size
            return bigger_size_wins if self.positive else not bigger_size_wins

        a = self.first
        b = other.first
        while a is not None:
            if a.data != b.data:
                bigger_digit_wins = a.data > b.data
                return bigger_digit_wins if self.positive else not bigger_digit_wins
            a = a.next
            b = b.next

        return False

    def __lt__(self, other):
        return other.__gt__(self)

    def __eq__(self, other):
        return not (self > other) and not (self < other)