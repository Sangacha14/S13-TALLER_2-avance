class Opciones:
    iva=0.12
    def __init__(self):
        pass
    def genero(self):
        GENERO= (('M', 'Masculino'),('F', 'Femenino'),)
        return GENERO

    def estado_civil(self):
        ESTADO_CIVIL = (('S','Soltero(a)'),('C','Casado(a)'),('D','Divorciado(a)'),
            ('V', 'Viudo(a)'),('U','Union Libre'),
        )
        return ESTADO_CIVIL
    def forma_pago(self):
        FORMA_PAGO = (('E', 'Efectivo'),('C', 'Credito'),('V', 'Paypal'),)
        return FORMA_PAGO

    def motivo_permiso(self):
        MOTIVO_PERMISO=(('P','Personal'),('M','Medico'))
        return MOTIVO_PERMISO