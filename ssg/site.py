from pathlib import Path


class Site:
    def __init__(self, source,dest):
        self._source=Path()
        self._dest=Path()

    def create_dir(self,path):
        directory=self._dest+"/"+self._source.relative_to(self._dest)
        directory.mkdir(parents=True,exist_ok=True)


    def build(self):
        self._dest.mkdir(parents=True,exist_ok=True)

