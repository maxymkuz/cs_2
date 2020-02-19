def check_input(ipt):
    """
    str -> bool
    True if input is ok ip address
    >>> check_input("еуіе")
    False
    """
    if ipt.count('.') != 3:
        return False
    try:
        lst = ipt.split('/')[0].split('.')
        for i in lst:
            if not 0 <= int(i) <= 255:
                return False
        return True
    except ValueError:
        return False


def get_ip_from_raw_address(raw_address):
    """
    (str) -> str
    returns an ip adress without last 3 symbols
    >>> get_ip_from_raw_address('v/b')
    'v'
    >>> get_ip_from_raw_address('123.456.788.0/30')
    '123.456.788.0'
    >>> get_ip_from_raw_address('0.0.0.0/0')
    '0.0.0.0'
    """
    if not check_input(raw_address) or raw_address.count('/') != 1:
        return None
    return raw_address.split('/')[0]


def binary_to_int(n):
    """
    str -> int
    Converts string with 0 and 1 without 0b at the beginning to int
    >>> binary_to_int("1010")
    10
    """
    res = 0
    for i in range(len(n) - 1, -1, -1):
        if n[i] == '1':
            res += 2 ** (len(n) - 1 - i)
    return res


def get_network_address_from_raw_address(raw_address):
    """
    (str)-> str
    Returns the network address using raw_address
    # >>> "91.124.230.205/30"
    # '91.124.230.204'
    >>> get_network_address_from_raw_address('191.168.1.15/24')
    '191.168.1.0'
    >>> get_network_address_from_raw_address('91.124.230.205/30')
    '91.124.230.204'
    """
    if not check_input(raw_address) or raw_address.count('/') != 1:
        return None
    num = int(raw_address.split('/')[1])
    ip = [int(i) for i in raw_address[:-3].split('.')]
    mask, network_address, temp = [], [], ''

    for i in range(32):
        temp += '1' if i < num else '0'
        if (i + 1) % 8 == 0:
            mask.append(binary_to_int(temp))
            temp = ''

    for i in range(len(ip)):
        network_address.append(str(mask[i] & ip[i]))

    return ".".join(network_address)


def get_broadcast_address_from_raw_address(raw_address):
    """
    str -> str
    Returns broadcast address
    >>> get_broadcast_address_from_raw_address('191.150.1.15/24')
    '191.150.1.255'
    >>> get_broadcast_address_from_raw_address('91.124.230.205/30')
    '91.124.230.207'
    """
    if not check_input(raw_address) or raw_address.count('/') != 1:
        return None
    mask = get_binary_mask_from_raw_address(raw_address).split('.')
    for i in range(len(mask)):
        mask[i] = 255 - binary_to_int(mask[i])

    net_adr = get_network_address_from_raw_address(raw_address).split('.')
    res = ".".join([str(mask[i] | int(net_adr[i])) for i in range(len(mask))])
    return res


def get_binary_mask_from_raw_address(raw_address):
    """
    str -> str
    Returns a binary mask
    >>> get_binary_mask_from_raw_address('192.168.0.7/25')
    '11111111.11111111.11111111.10000000'
    >>> get_binary_mask_from_raw_address('192.168.1.15/24')
    '11111111.11111111.11111111.00000000'
    >>> get_binary_mask_from_raw_address('91.124.230.205/30')
    '11111111.11111111.11111111.11111100'
    """
    if not check_input(raw_address) or raw_address.count('/') != 1:
        return None
    mask = int(raw_address[-2:]) * "1" + (32 - int(raw_address[-2:])) * "0"
    new_mask, temp = [], ''
    for i in range(len(mask)):
        temp += mask[i]
        if (i + 1) % 8 == 0:
            new_mask.append(temp)
            temp = ''
    return ".".join(new_mask)


def get_first_usable_ip_address_from_raw_address(raw_address):
    """
    str -> str
    Returns first usable ip address
    >>> get_first_usable_ip_address_from_raw_address('172.44.0.7/30')
    '172.44.0.5'
    >>> get_first_usable_ip_address_from_raw_address('91.124.230.205/30')
    '91.124.230.205'
    """
    if not check_input(raw_address) or raw_address.count('/') != 1:
        return None
    net_adr = get_network_address_from_raw_address(raw_address).split(".")
    broadcast = get_broadcast_address_from_raw_address(raw_address).split(".")
    lower_bound = int("".join(net_adr))
    upper_bound = int("".join(broadcast))
    if upper_bound - lower_bound >= 2:
        for i in range(len(net_adr) - 1, -1, -1):
            if net_adr[i] == 255:
                net_adr[i] = 0
                continue
            net_adr[i] = str(int(net_adr[i]) + 1)
            return '.'.join(net_adr)
    return None


def get_penultimate_usable_ip_address_from_raw_address(raw_address):
    """
    str -> str
    Returns last usable ip address
    >>> get_penultimate_usable_ip_address_from_raw_address('192.123.0.7/11')
    '192.127.255.253'
    >>> get_penultimate_usable_ip_address_from_raw_address('91.124.230.205/30')
    '91.124.230.205'
    """
    if not check_input(raw_address) or raw_address.count('/') != 1:
        return None
    net_adr = get_network_address_from_raw_address(raw_address).split(".")
    broadcast = get_broadcast_address_from_raw_address(raw_address).split(".")
    lower_bound = int("".join(net_adr))
    upper_bound = int("".join(broadcast))
    if upper_bound - lower_bound >= 2:
        for i in range(len(broadcast) - 1, -1, -1):
            if 1 == broadcast[i]:
                broadcast[i] = 254
                continue
            if broadcast[i] == 0:
                broadcast[i] = 255
                continue
            broadcast[i] = str(int(broadcast[i]) - 2)
            return '.'.join(broadcast)
    return None


def get_number_of_usable_hosts_from_raw_address(raw_address):
    """
    str -> int
    >>> get_number_of_usable_hosts_from_raw_address('192.168.144.1/21')
    1784
    >>> get_number_of_usable_hosts_from_raw_address('91.124.230.205/30')
    2
    """
    if not check_input(raw_address) or raw_address.count('/') != 1:
        return None
    res = 0
    net_adr = get_network_address_from_raw_address(raw_address).split(".")
    broadcast = get_broadcast_address_from_raw_address(raw_address).split(".")
    lower_bound = int("".join(net_adr))
    upper_bound = int("".join(broadcast))
    if lower_bound < upper_bound:
        for i in range(len(broadcast) - 1, -1, -1):
            difference = int(broadcast[i]) - int(net_adr[i]) - 1

            if difference <= 0:
                continue
            res += difference * (255 ** (len(broadcast) - i - 1))
    return res


def get_ip_class_from_raw_address(raw_address):
    """
    str -> str
    Returns a class of this address
    [1,126]-A
    [128, 191] - B
    [192, 223] - C
    Numbers larger than 223 correspond - D and E,
    >>> get_ip_class_from_raw_address('111.134.83.111/8')
    'A'
    >>> get_ip_class_from_raw_address('10.0.0.0/11')
    'A'
    >>> get_ip_class_from_raw_address('128.111.111.0/11')
    'B'
    """
    if not check_input(raw_address) or raw_address.count('/') != 1:
        return None
    num = int(raw_address.split('.')[0])
    if 1 <= num <= 126:
        return 'A'
    elif 128 <= num <= 191:
        return 'B'
    elif 192 <= num <= 223:
        return 'C'


def check_private_ip_address_from_raw_address(raw_address):
    """
    str -> bool
    Returns True if this ip address is private else False
    >>> check_private_ip_address_from_raw_address('192.111.813.111/11')
    False
    >>> check_private_ip_address_from_raw_address('10.11.11.11/8')
    True
    """
    if not check_input(raw_address) or raw_address.count('/') != 1:
        return None
    address = raw_address.split('/')[0].split('.')
    mask = int(raw_address.split('/')[1])
    if address[0] == '10' and mask == 8:
        return True
    elif address[0] == '172' and 16 <= int(address[1]) <= 31 and mask == 12:
        return True
    elif address[0] == '192' and address[1] == '168' and mask == 16:
        return True
    return False


if __name__ == "__main__":
    ipt = input("Enter the raw address: ")
    if check_input(ipt):
        if ipt.count('/') != 1:
            print("Missing prefix")
        else:
            print('IP address: ' + get_ip_from_raw_address(ipt))
            print('Network Address: ' +
                  get_network_address_from_raw_address(ipt))
            print('Broadcast Address: ' +
                  get_broadcast_address_from_raw_address(ipt))
            print('Binary Subnet Mask: ' +
                  get_binary_mask_from_raw_address(ipt))
            print('First usable host IP: ' +
                  get_first_usable_ip_address_from_raw_address(ipt))
            print('Penultimate usable host IP: ' +
                  get_penultimate_usable_ip_address_from_raw_address(ipt))
            print('Number of usable Hosts:',
                  get_number_of_usable_hosts_from_raw_address(ipt))
            print('IP class: ' + get_ip_class_from_raw_address(ipt))
            print('IP type private:',
                  check_private_ip_address_from_raw_address(ipt))
    else:
        print("Error")
