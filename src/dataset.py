"""
Dataset de entrenamiento para el perceptrón.

Cada tupla contiene:
    ([ingreso_mensual_normalizado, historial_crediticio], etiqueta)

- ingreso_mensual_normalizado: escala simplificada (1 a 9)
- historial_crediticio: 1 = bueno, 0 = malo
- etiqueta: 1 = aprobado, 0 = rechazado
"""

training_data = [
    ([8, 1], 1),
    ([7, 1], 1),
    ([6, 1], 1),
    ([3, 0], 0),
    ([2, 0], 0),
    ([1, 0], 0)
]
