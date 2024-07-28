def calculate_can_chi_calendar(year):
    can = ['Canh', 'Tan', 'Nham', 'Quy', 'Giap',
           'At', 'Binh', 'Dinh', 'Mau', 'Ky']
    chi = ['Than', 'Dau', 'Tuat', 'Hoi', 'Ty', 'Suu',
           'Dan', 'Meo', 'Thin', 'Ty', 'Ngo', 'Mui']
    can_dict = {}
    chi_dict = {}
    for j in range(0, 10):
        can_dict[j] = can[j]
    for k in range(0, 12):
        chi_dict[k] = chi[k]

    result = can_dict.get(year % 10) + " " + chi_dict.get(year % 12)

    return result


print(calculate_can_chi_calendar(2020))
