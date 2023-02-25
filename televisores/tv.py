class TV:
  _numTV = 0

  def __init__(self, marca, estado):
    self._marca = marca
    self._canal = 1
    self._precio = 500
    self._estado = estado
    self._volumen = 1
    self._control = None
    TV._numTV += 1

  def setMarca(self, marca):
    self._marca = marca

  def getMarca(self):
    return self._marca

  def setControl(self, control):
    self._control = control

  def getControl(self):
    return self._control

  def setPrecio(self, precio):
    self._precio = precio

  def getPrecio(self):
    return self._precio

  def setVolumen(self, volumen):
    if (not self._estado): return
    if (volumen < 0 or volumen > 7): return
    self._volumen = volumen

  def getVolumen(self):
    return self._volumen

  def setCanal(self, canal):
    if (not self._estado): return
    if ( canal < 1 or canal > 120): return
    self._canal = canal

  def getCanal(self):
    return self._canal

  @staticmethod
  def getNumTV():
    return TV._numTV
  
  @classmethod
  def setNumTV(cls, numTV):
    cls._numTV = numTV

  def turnOff(self):
    self._estado = False

  def turnOn(self):
    self._estado = True

  def getEstado(self):
    return self._estado

  def canalUp(self):
    if (not self._estado): return
    if (self._canal == 120): return
    self._canal += 1

  def canalDown(self):
    if (not self._estado): return
    if (self._canal == 1): return
    self._canal -= 1

  def volumenUp(self):
    if (not self._estado): return
    if (self._volumen == 7): return
    self._volumen += 1

  def volumenDown(self):
    if (not self._estado): return
    if (self._volumen == 0): return
    self._volumen -= 1