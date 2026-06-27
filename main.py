from src.perceptron import Perceptron
from src.dataset import training_data


def main():
    model = Perceptron()
    model.train(training_data)

    nuevo_cliente = [9, 1]
    resultado = model.predict(nuevo_cliente)

    estado = "APROBADO" if resultado == 1 else "RECHAZADO"
    print(f"Predicción para cliente {nuevo_cliente}: {resultado} ({estado})")


if __name__ == "__main__":
    main()
