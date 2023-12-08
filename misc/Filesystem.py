from adventofcode import LOG


class Directory:
    def __init__(self, name, sub_dirs, files, parent_dir=None):
        self.name = name
        self.sub_dirs = sub_dirs
        self.parent_dir = self if parent_dir is None else parent_dir
        self.files = files
        pass

    def __str__(self) -> str:
        return f"Directory {self.get_full_path()}"

    def __repr__(self) -> str:
        return f"Dir[{self.get_full_path()}]({self.get_dir_size()})"

    def add_sub_dir(self, sub_dir_name):
        self.sub_dirs[sub_dir_name] = Directory(name=sub_dir_name, sub_dirs={}, files={}, parent_dir=self)

    def add_file(self, file):
        self.files[file.name] = file

    def get_sub_dir(self, sub_dir_name):
        ret_val = None
        try:
            ret_val = self.sub_dirs[sub_dir_name]
        except KeyError:
            LOG.warn(f"Subdir {sub_dir_name} not exists.")
            self.add_sub_dir(sub_dir_name)
            ret_val = self.sub_dirs[sub_dir_name]
        return ret_val

    def get_full_path(self) -> str:
        full_path = [self.name]
        parent_dir = self.parent_dir
        dir_name = self.name
        while parent_dir.name != dir_name:
            full_path.insert(0, parent_dir.name)
            dir_name = parent_dir.name
            parent_dir = parent_dir.parent_dir
        return "/".join(full_path)

    def get_dir_size(self) -> int:
        dir_size = 0
        for dir_name in self.sub_dirs:
            dir_size += self.sub_dirs[dir_name].get_dir_size()
        for file_name in self.files:
            x = self.files[file_name].get_size()
            dir_size += x
        return dir_size

    def get_all_dirs(self, dirs):

        for dir in self.sub_dirs.values():
            dirs.append(dir)
            dir.get_all_dirs(dirs)

        return


class File:
    def __init__(self, name, size=0):
        self.name = name
        self.size = int(size)

    def __str__(self) -> str:
        return f"File {self.name} with size {self.size}"

    def __repr__(self) -> str:
        return f"File[{self.name}](s={self.size})"

    def get_size(self) -> int:
        return self.size
