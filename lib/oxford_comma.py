def oxford_comma(items):
    new_list = []

    if len(items) > 1:
        if len(items) == 2:
            return " and ".join(items)
        for item in items:
            if items[len(items) - 1] == item:
                new_list.append(f"and {item}")
            else:
                new_list.append(f"{item}, ")
    else:
        print("".join(items))
        return "".join(items)
    return "".join(new_list)
