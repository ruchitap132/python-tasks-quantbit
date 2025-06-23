def compare_versions(v1, v2):
    parts1 = list(map(int, v1.split('.')))
    parts2 = list(map(int, v2.split('.')))
    
    max_len = max(len(parts1), len(parts2))
    

    parts1 += [0] * (max_len - len(parts1))
    parts2 += [0] * (max_len - len(parts2))
    
    for a, b in zip(parts1, parts2):
        if a < b:
            return -1
        elif a > b:
            return 1
    return 0


print(compare_versions('1.01', '1.001'))  
