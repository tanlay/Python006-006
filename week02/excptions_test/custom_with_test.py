class Open():
    def __enter__(self):
        print("open")

    def __exit(self, type, value, trace):
        print("close")

    def __call__(self):
        pass


with Open('test.test') as f:
    pass
