def hms(segundos):
    horas = segundos//3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60

    return (horas, minutos, segundos)

def main():
    total = 7600
    horas, minutos, segundos = hms(total)
    print("%d segundos equivale a %dh%dm%ds" % (total,horas, minutos, segundos))

if __name__ == "__main__":
    main()
