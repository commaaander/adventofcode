""" https://adventofcode.com/2022/day/7 """

from adventofcode import LOG
from misc.Filesystem import Directory, File

questions = [
    "Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. "
    "What is the total size of that directory?",
    "Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?",
]


def part_one(**kwargs):
    LOG.debug(f"part_one({kwargs=})")

    root = execute_commands(kwargs["raw_data"])
    dirs = []
    root.get_all_dirs(dirs)
    # LOG.debug(f"Found {len(dirs)} dirs. {dirs=}")
    LOG.debug(f"Found {len(dirs)} dirs.")

    return questions[0], sum(dir.get_dir_size() for dir in dirs if dir.get_dir_size() < 100_000)


def part_two(**kwargs):
    LOG.debug(f"part_two({kwargs=})")

    root = execute_commands(kwargs["raw_data"])
    dirs = []
    root.get_all_dirs(dirs)
    # LOG.debug(f"Found {len(dirs)} dirs. {dirs=}")
    LOG.debug(f"Found {len(dirs)} dirs.")

    # total_diskspace = 70_000_000  # 35_227_764
    total_diskspace = root.get_dir_size()
    needed_space = 30_000_000

    dir_sizes = {}
    for dir in dirs:
        # if total_diskspace - dir.get_dir_size() >= needed_space:
        #     dir_sizes[dir.get_full_path()] = total_diskspace - dir.get_dir_size() - needed_space
        if dir.get_full_path() in dir_sizes:
            LOG.warn(f"double entry for {dir.get_full_path()}")
        dir_sizes[dir.get_full_path()] = total_diskspace - dir.get_dir_size() - needed_space

    answer = 0
    return questions[1], answer


def execute_commands(terminal_output) -> Directory:

    root = Directory(name="root", sub_dirs={}, files={})
    pwd = root

    for command_line in terminal_output.split("$"):

        command = command_line[:3].strip()
        args = list(arg for arg in command_line[4:].split("\n") if arg != "")
        # LOG.debug(f"{pwd.get_full_path()=}, {command=}, {args=}")
        if command == "cd":

            dir = args[0]
            if dir == "/":
                pwd = root
            elif dir == "..":
                pwd = pwd.parent_dir
            else:
                pwd = pwd.get_sub_dir(dir)

            # LOG.debug(f"Changed into dir {pwd.get_full_path}")

        elif command == "ls":
            for obj in args:
                meta, name = obj.split(" ")
                if meta == "dir":
                    pwd.add_sub_dir(sub_dir_name=name)
                    pass
                else:
                    pwd.add_file(File(name=name, size=meta))
            # LOG.debug(f"ls: {dir_content=}")
            pass
        else:
            LOG.warn(f" Unknown command >{command}<")

    return root
