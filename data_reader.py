import random
def get_data():
    """
    ИМИТАЦИЯ получения данных!!!!!
    в случае наличия ардуино код таков:
    import serial
    try:
        arduino = serial.Serial("COM4", 9600, timeout=1)
        line = arduino.readline().decode("utf-8").strip()
        arduino.close()
        return line.split(",")
    except Exception:
        return ["0", "0", "0"]
    """
    # тестовые значения ГЕНЕРИРУЮТСЯ
    temp = round(random.uniform(20.0, 30.0), 1)
    hum = round(random.uniform(50.0, 80.0), 1)
    light = random.randint(200, 900)
    return [str(temp), str(hum), str(light)]
