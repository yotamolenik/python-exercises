from typing import List, Callable


def complicated_func(
    lst: List[int], hook_modify_element: Callable[[int], int], hook_if_negative=None
) -> int:
    res = sum(hook_modify_element(x) for x in lst)
    if res < 0 and hook_if_negative is not None:
        print("Returning negative hook")
        return hook_if_negative
    return res


def my_hook_func(x: int) -> int:
    return x


if __name__ == "__main__":
    res = complicated_func(
        lst=[1, 2, -10, 4],
        hook_modify_element=my_hook_func,
        hook_if_negative=0,
    )
    print(res)