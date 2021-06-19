import datetime

def add_plan(date, start_time, end_time, lesson_name, lesson_form, teacher, room_num, lesson_time):
    with open('plan.dat', "a") as file:
        file.write(f"{date}|{start_time}|{end_time}|{lesson_name}|{lesson_form}|{teacher[0]} {teacher[1]} {teacher[2]}|{room_num}|{lesson_time} \n")
        file.close()

def get_plan():
    plan = []
    with open('plan.dat', 'r') as file:
        for line in file.readlines():
            plan.append(line)
    return plan

def get_plan_by_date(date):
    plan = get_plan()
    return [x.rstrip() for x in plan if x.split("|")[0] == date]

def get_list_by_przedmiot(przedmiot):
    plan = get_plan()
    list = [x.rstrip().split("|") for x in plan if x.split("|")[3] == przedmiot]
    return list

def get_plan_by_przedmiot(przedmiot):
    plan = get_plan()
    list = [x.rstrip().split("|") for x in plan if x.split("|")[3] == przedmiot]
    for x in list:
        x[0] = datetime.datetime.strptime(f"{x[0]} {x[2]}", "%d/%m/%Y %H:%M")
    return list

def how_much_lessons_done_today(lesson_name):
    current_date = datetime.datetime.today()
    plan = get_plan_by_przedmiot(lesson_name)
    plan = sorted(plan, key=lambda x: x[0])
    asd = len([x for x in plan if x[0] < current_date])
    return asd


# add_plan("26/01/2021", "12:00", "14:00", "Programowanie", "L", ["Doctor", "Name", "Surname"], 10, "2")
# add_plan("26/01/2021", "12:00", "14:00", "Programowanie", "L", ["Doctor", "Name", "Surname"], 10, "2")


print(get_plan_by_date("27/01/2021"))
print(get_list_by_przedmiot("Fizyka"))
print(how_much_lessons_done_today("Fizyka"))