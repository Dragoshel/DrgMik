class Result:
    def __init__(self, suc, err) -> None:
        self.suc = suc
        self.err = err

    def is_error(self) -> bool:
        return self.err is not None


def succed(suc) -> Result:
    return Result(suc, None)


def fail(err: Exception) -> Result:
    return Result(None, err)
