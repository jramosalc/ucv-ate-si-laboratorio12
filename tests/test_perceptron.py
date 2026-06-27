from src.perceptron import Perceptron
from src.dataset import training_data


def test_prediction():
    """Un cliente con buen ingreso e historial debe ser aprobado."""
    model = Perceptron()
    model.train(training_data)
    assert model.predict([8, 1]) == 1


def test_rejection():
    """Un cliente con bajo ingreso y mal historial debe ser rechazado."""
    model = Perceptron()
    model.train(training_data)
    assert model.predict([1, 0]) == 0


def test_new_unseen_case():
    """El perceptrón debe generalizar a un caso no visto en el entrenamiento."""
    model = Perceptron()
    model.train(training_data)
    assert model.predict([9, 1]) == 1


def test_weights_are_updated_after_training():
    """Tras entrenar, los pesos ya no deben ser los valores iniciales (0.0)."""
    model = Perceptron()
    model.train(training_data)
    assert model.weights != [0.0, 0.0]
