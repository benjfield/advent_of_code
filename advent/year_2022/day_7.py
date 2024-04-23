from advent.runner import register
import math
import re

def get_and_update_folder_sizes(folder_sizes, folder_name, folder):
    total_size = 0
    for name, underlying in folder.items():
        if name == "parent":
            pass
        elif isinstance(underlying, dict):
            total_size += get_and_update_folder_sizes(folder_sizes, name, underlying)
        else:
            total_size += underlying
    
    folder_sizes.append(total_size)
    return total_size

def build_filesystem(split_text):    
    filesystem = {}

    for line in split_text:
        split_by_space = line.split(" ")
        if split_by_space[0] == "$":
            if split_by_space[1] == "cd":
                if split_by_space[2] == "/":
                    current_directory = filesystem
                elif split_by_space[2] == "..":
                    current_directory = current_directory["parent"]
                else:
                    old_directory = current_directory
                    current_directory = current_directory[split_by_space[2]]
                    current_directory["parent"] = old_directory
        else:
            if split_by_space[0] == "dir":
                if split_by_space[1] not in current_directory:
                    current_directory[split_by_space[1]] = {}
                else:
                    raise Exception
            else:
                if split_by_space[1] not in current_directory:
                    current_directory[split_by_space[1]] = int(split_by_space[0])
                else:
                    raise Exception

    return filesystem

@register(7, 2022, 1, True)
def no_space_left_1(split_text):
    filesystem = build_filesystem(split_text)
    
    folder_sizes = []
    get_and_update_folder_sizes(folder_sizes, "/", filesystem)

    small_folders_size = 0

    for size in folder_sizes:
        if size <= 100000:
            small_folders_size += size

    return small_folders_size


@register(7, 2022, 2, True)
def no_space_left_2(split_text):
    filesystem = build_filesystem(split_text)
    
    folder_sizes = []
    root_size = get_and_update_folder_sizes(folder_sizes, "/", filesystem)

    folder_sizes.sort()

    free_space = 70000000 - root_size

    needed = 30000000 - free_space

    for folder_size in folder_sizes:
        if folder_size > needed:
            return folder_size

    return small_folders_size