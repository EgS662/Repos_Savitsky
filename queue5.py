def moves_to_stamp(stamp, target):
    def can_stamp(i):
        stamped = False
        for j in range(len(stamp)):
            if target[i + j] == '?' or target[i + j] == stamp[j]:
                stamped = True
            else:
                return False
        return stamped

    def do_stamp(i):
        nonlocal target
        new_target = list(target)
        for j in range(len(stamp)):
            new_target[i + j] = '?'
        target = ''.join(new_target)

    n, m = len(target), len(stamp)
    stamped_positions = set()
    result = []

    for _ in range(10 * n):
        stamped = False

        for i in range(n - m + 1):
            if i not in stamped_positions and can_stamp(i):
                do_stamp(i)
                stamped = True
                result.append(i)
                stamped_positions.update(set(range(i, i + m)))

        if stamped and len(stamped_positions) == n:
            return result[::-1]

    return []

stamp1 = "abc"
target1 = "ababc"
print(moves_to_stamp(stamp1, target1))  


