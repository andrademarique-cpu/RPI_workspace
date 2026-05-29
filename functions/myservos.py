# mi_robotica/servos.py
import time
from gpiozero import AngularServo, Device
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero.exc import GPIOPinInUse

# Forzar a gpiozero a usar el driver nativo de la Raspberry Pi 5
Device.pin_factory = LGPIOFactory()

class ControladorServo:
    def __init__(self, pin_gpio, angulo_min=0, angulo_max=180, min_pulso=0.5/1000, max_pulso=2.5/1000):
        """
        Clase generalizada para controlar cualquier servo en Raspberry Pi 5.
        
        :param pin_gpio: Número de pin GPIO (ej. 12, 18)
        :param angulo_min: Ángulo físico mínimo del servo (habitualmente 0)
        :param angulo_max: Ángulo físico máximo del servo (habitualmente 180)
        :param min_pulso: Ancho de pulso mínimo en segundos (0.5ms = 0.5/1000)
        :param max_pulso: Ancho de pulso máximo en segundos (2.5ms = 2.5/1000)
        """
        self.pin = pin_gpio
        
        try:
            # Inicializamos el servo angular con los parámetros calibrados
            self.servo = AngularServo(
                pin=self.pin,
                initial_angle=None, # Evita el "latigazo" inicial al encender
                min_angle=angulo_min,
                max_angle=angulo_max,
                min_pulse_width=min_pulso,
                max_pulse_width=max_pulso
            )
            print(f"✅ Servo inicializado correctamente en el GPIO {self.pin}")
        except GPIOPinInUse:
            print(f"❌ Error: El GPIO {self.pin} ya está siendo usado por otro proceso.")
            raise

    def mover_a(self, angulo):
        """
        Mueve el servo a un ángulo específico de forma segura.
        """
        # Validamos los límites para no forzar los engranajes del motor
        if angulo < self.servo.min_angle:
            angulo = self.servo.min_angle
        elif angulo > self.servo.max_angle:
            angulo = self.servo.max_angle
            
        self.servo.angle = angulo
        print(f"Servo [GPIO {self.pin}] -> Movido a {angulo}°")

    def apagar(self):
        """
        Libera el pulso del servo (evita que gaste batería y que vibre en reposo).
        """
        self.servo.detach()
        print(f"💤 Servo [GPIO {self.pin}] en reposo (pulso desactivado).")