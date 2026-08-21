salary = 800
raise_ = 15.8

def new_salary(salary, raise_):
    nw_slry = 0
    nw_slry = salary + ((raise_ / 100) * salary)
    return nw_slry

print(new_salary(salary, raise_))