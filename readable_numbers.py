long_unreadable_number = 1000000000000
long_readable_number = 1_000_000_000_000
answer = long_unreadable_number + long_readable_number

# printing the answer in an unreadable way
print(answer)

# printing the answer in a readable way
print(f"{answer:,}")

# you can do the same with the underscore in the middle of the number
print(f"{answer:_}")
