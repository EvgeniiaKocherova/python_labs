m = int(input("Минуты: "))

days = m // 1440
hours = int(((m / 1440) - days)*24)

minutes = m % 60

print(f"{days}:{hours}:{minutes:02d}")

