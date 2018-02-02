old = {
    "#1": 2,
    "#2": 4,
    "#3": 8
}
new = {
    "#1": 3,
    "#2": 6,
    "#4": 12
}
# old s2的key集合
old_key_set = set(old.keys())
new_key_set = set(new.keys())

remove_key_set = old_key_set.difference(new_key_set)
add_key_set = new_key_set.difference(old_key_set)
update_key_set = old_key_set.intersection(new)