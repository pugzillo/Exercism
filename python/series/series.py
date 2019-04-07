def slices(series, length):
    # Check if length is positive and less than series length
    if len(series) < length:
        raise ValueError("Length is greater than series length")

    if length <= 0:
        raise ValueError("Length cannot be zero or negative")

    # Check if series is valid
    if len(series) == 0:
        raise ValueError("Series cannot be empty")
    
    result = list()
    
    num_loops = len(series) + 1 - length

    for start in range(num_loops):
        end = start + length
        value = series[start:end]
        result.append(value)
    
    return result

    

