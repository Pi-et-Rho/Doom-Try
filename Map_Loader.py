class MapLoader:

    @staticmethod

    def loader(file_path):
        with open (file_path, "r") as file:
            file.readline()
            width, height = map(int, file.readline().split(','))
            game_map = []
            for _ in range(height):
                row = list(map(int, file.readline().split(',')))
                game_map.append(row)
        return width, height, game_map