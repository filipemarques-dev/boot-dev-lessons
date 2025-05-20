def args_logger(*args, **kwargs):
    count = 1
    for item in args:
        print(f"{count}. {item}")
        count += 1
    sorted_kwargs = sorted(kwargs.items())
    for item in sorted_kwargs:
        print(f"* {item[0]}: {item[1]}")