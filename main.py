import requests

def check_error_404(url):
    try:
        response = requests.get(url)
        return response.status_code == 404
    except requests.exceptions.RequestException:
        return True

def main():
    print("Pega los enlaces (uno por línea). Presiona Enter y luego ingresa 'q' para continuar:")
    enlaces = []
    while True:
        entrada = input()
        if entrada.lower() == 'q':
            break
        enlaces.append(entrada.strip())

    for enlace in enlaces:
        if check_error_404(enlace):
            print(f"Error 404 en: {enlace}")
        else:
            print(f"Enlace válido: {enlace}")

if __name__ == "__main__":
    main()
