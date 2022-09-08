from core.repositories import TheatreRepository

class TestTheatreRepository(TheatreRepository):
    def __init__(self):
        self.theatres: dict = []
        self._init()

    def faker(self):
        result = {}
        result["Avengers 5"] = {
            "2022-05-01": {
                "2PM": [[False, False, False],
                        [False, True, True],
                        [False, False, False]]
            }
        }
        result["Avengers 4"] = {
            "2022-02-02": {
                "2PM": [[False, True, False],
                        [False, False, False],
                        [False, False, False]]
            }
        }
        return result

    def _init(self):
        self.theatres = self.faker()

    def _save(self):
        pass

TestTheatreRepository.__test__ = False