from app import run_app
from model.costs import save_costs
from model.parameters import save_parameters

def main():
    """
    Entry point for the application
    """
    
    print("DAIMO: Dashboard para el Análisis de Intervenciones en Movilidad")
    print("1. Construir el grafo")
    print("2. Calcular los costos")
    print("3. Ejecutar la aplicación")
    print()
    print("> ")

    choice = input("Ingresa una opción (1/2/3): ")

    if choice == '1':
        save_parameters()
    elif choice == '2':
        save_costs()
    elif choice == '3':
        run_app()
    else:
        print("Opción incorrecta")


if __name__ == "__main__":
    main()
