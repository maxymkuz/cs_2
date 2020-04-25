def get_input():
    return list(map(int, input().split(' ')))


def print_arr(array):
    for row in array:
        print()
        for col in row:
            if col:
                print(col, end='  ')
            else:
                print(col, end=' ')


def recursive_jump(r_prev, c_prev, arr, num):
    # Maybe change for other if later
    # print()
    if all([all(row) for row in arr]):
        print_arr(arr)
        return True  # or print ansver

    for r_idx in range(r):
        for c_idx in range(c):
            if r_idx == r_prev or c_idx == c_prev or r_idx - c_idx == \
                    r_prev - c_prev or r_idx + c_idx == r_prev + c_prev:
                # print(r_idx, c_idx)
                continue
            if arr[r_idx][c_idx]:
                continue
            arr[r_idx][c_idx] = num+1
            if recursive_jump(r_idx, c_idx, arr, num+1):
                return True
            else:
                # num -= 1
                arr[r_idx][c_idx] = False
                continue
    return False


def even(r, c, arr):
    num = 0
    for two_row in range(r//2):
        start = two_row * 2
        print_arr(arr[two_row*2: two_row*2 + 2])
        recursive_jump(start, 0, arr[two_row*2: two_row*2 + 2], num)


if __name__ == '__main__':
    r, c = 4, 16
    arr = [[False for i in range(c)][:] for j in range(r)]
    num = 0
    if r % 2 == 0:
        even(r, c, arr)
