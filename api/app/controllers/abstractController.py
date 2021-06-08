class AbstractController:
    def get(self, id):
        raise NotImplementedError()

    def create(self, data):
        raise NotImplementedError()

    def update(self, id, data):
        raise NotImplementedError()

    def delete(self, id):
        raise NotImplementedError()
