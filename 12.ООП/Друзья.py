class Friends:
    def __init__(self, connections):
        self.connections = set(frozenset(c) for c in connections)

    def add(self, connection):
        """Метод add добавляет новую связь во множество связей, если связь уникальна."""
        connection = frozenset(connection)
        if connection not in self.connections:
            self.connections.add(connection)
            return True
        return False

    def remove(self, connection):
        """Метод remove удаляет связь из множества связей, если она существует."""
        connection = frozenset(connection)
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        return False

    def names(self):
        """Метод names возвращает множество имен, которые участвуют в связях."""
        names = set()
        for connection in self.connections:
            names.update(connection)
        return names

    def connected(self, name):
        """Метод connected возвращает множество имен, связанных с заданным именем."""
        connected_names = set()
        for connection in self.connections:
            if name in connection:
                connected_names.update(connection - {name})
        return connected_names
