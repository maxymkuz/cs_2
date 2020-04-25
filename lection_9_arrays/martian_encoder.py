from arrays import Array


def print_answer(arr, length):
    """
    Simply prints an answer
    """
    for i in range(length):
        print(arr[i], end=' ')


def main():
    """
    This function converts an input into an list of degrees, the camera on
    Mars has to move in positive or negative direction to convey a message.
    THIS FUNCTION RETURNS MOST EFFECTIVE SOLUTION, SO THAT THE CAMERA HAS
    TO MOVE MINIMUM AMOUNT OF DEGREES.
    return: None
    """
    text = input("Please, enter am ASCII sentence you wanna encode: ")
    arr = Array(len(text)*2)
    start = 0
    for i in range(len(text)):
        let = text[i]
        if ord(let) > 127:
            raise ValueError(f'Value has to be ascii, YOU ENRERED {let}')
        for j in range(2):
            char = hex(ord(let))[2:][j]
            if not char.isdigit():
                char = ord(char) - ord('a') + 10
            num = int(char) * 360 / 16
            if num > start:
                deg = num - start if num - start < 360 - num + start else \
                    -360 + num - start
            else:
                deg = num - start if start - num < 360 - start + num else \
                    -360 + start - num
            arr[i*2 + j] = deg
            start = num
    print_answer(arr, len(text*2))


if __name__ == '__main__':
    main()
