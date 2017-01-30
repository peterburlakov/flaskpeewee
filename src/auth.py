class NoAuth:
    @staticmethod
    def authorize():
        return True


auth = NoAuth()
