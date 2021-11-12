# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
                object_type = line.split()[0].lower()
            elif object_type == "planet": 
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
                object_type = line.split()[0].lower()
            
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    Data = line.split()
    star.R = float(Data[1])
    star.m = float(Data[3])
    star.color = Data[2]
    star.x = float(Data[4])
    star.y = float(Data[5])
    star.Vx = float(Data[6])
    star.Vy = float(Data[7])  
    


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    Data = line.split()
    planet.R = float(Data[1])
    planet.color = Data[2]
    planet.m = float(Data[3])
    planet.x = float(Data[4])
    planet.y = float(Data[5])
    planet.Vx = float(Data[6])
    planet.Vy = float(Data[7])
    


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    i=0
    vobjects=['Солнечная система','Меркурий', 'Венера','Земля','Марс','Юпитер','Сатурн','Уран','Нептун']
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write('# '+ vobjects[i]+'\n')
            
            out_file.write(str(obj.type)+' '+str(obj.R)+' '+str(obj.color)+' '+str(obj.m)
                           +' '+str(obj.x)+' '+str(obj.y)+' '+str(obj.Vx)+' '+str(obj.Vy)+'\n')
            out_file.write('\n')
            i+=1
            '''out_file.write(str(space_objects)+' '+ str(space_objects.R)+' '+str(space_objects.color)+' '+
                  str(space_objects.m)+' '+str(space_objects.x)+' '+str(space_objects.y)+' '+
                  str(space_objects.Vx)+' '+str(space_objects.Vy)+'\n')'''
            

if __name__ == "__main__":
    print("This module is not for direct call!")
