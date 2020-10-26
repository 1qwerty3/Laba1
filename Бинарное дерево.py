class Node:
    def __init__(self, value):
        # Корень
        self.value = value
        # Левая ветвь
        self.left = None
        # Правая ветвь
        self.right = None

    def insert_after(self, value):
        """
        Функция вставки элемента в дерево
        :param value: значение для вставки
        """
        # Если элемент для вставки меньше корневого элемента
        if value < self.value:
            # Если левая ветвь не пуста, то рекурсивно вызываем для нее функцию вставки
            if self.left:
                self.left.insert_after(value)
            # Если левая ветвь пуста, вставляем элемент туда
            else:
                self.left = Node(value)
        # Если элемент для вставки больше корневого элемента
        elif value > self.value:
            # Если правая ветвь не пуста, то рекурсивно вызываем для нее функцию вставки
            if self.right:
                self.right.insert_after(value)
            # Если правая ветвь пуста, вставляем элемент туда
            else:
                self.right = Node(value)
        # Если элемент для вставки уже есть в дереве
        else:
            raise ValueError("Данное дерево не поддерживает дублирующиеся значения")

    def __repr__(self):
        """
         Функция вывода дерева в файл
        """
        # Массив будущих строк для вывода
        lines = []

        # Формируем правую ветвь
        if self.right:
            found = False
            for line in repr(self.right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line

                lines.append(line)

        # Корень
        lines.append(str(self.value))

        # Формируем левую ветвь
        if self.left:
            found = False
            for line in repr(self.left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line

                lines.append(line)

        # Выводим в файл
        f = open('output.txt', 'w', encoding='utf-8')
        for line in lines:
            f.write(str(line))
            f.write('\n')
        f.close()

        return "\n".join(lines)


class BinarySearchTree:
    def __init__(self):
        # Корень
        self.root = None

    def insert(self, data):
        """
        Функция обертка для вставки
        :param data: элемент для вставки
        """
        # Если корня нет
        if self.root is None:
            self.root = Node(data)
            return
        # Если корень есть
        self.root.insert_after(data)

    def __repr__(self):
        """
        Функция обертка для вывода
        """
        return repr(self.root)


if __name__ == '__main__':
    # Создаем экзмепляр класса Бинароное Дерево Поиска
    bst = BinarySearchTree()

    # Вставляем элементы в дерево
    bst.insert(4)
    bst.insert(2)
    bst.insert(8)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
    bst.insert(10)
    bst.insert(9)
    bst.insert(25)
    bst.insert(26)
    bst.insert(17)

    # Выводим дерево в файл
    print(bst)
