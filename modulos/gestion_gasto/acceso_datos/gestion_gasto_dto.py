class GastoDTO:
    def __init__(self, transaccion_id=None, usuario_id=None, categoria=None,
                 descripcion=None, monto=None, fecha=None):
        self.transaccion_id = transaccion_id
        self.usuario_id     = usuario_id
        self.categoria      = categoria
        self.descripcion    = descripcion
        self.monto          = monto
        self.fecha          = fecha

    def to_dict(self):
        return {
            "transaccion_id": self.transaccion_id,
            "usuario_id":     self.usuario_id,
            "categoria":      self.categoria,
            "descripcion":    self.descripcion,
            "monto":          float(self.monto),
            "fecha":          self.fecha.isoformat() if self.fecha else None
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            transaccion_id=d.get("transaccion_id"),
            usuario_id   =d.get("usuario_id"),
            categoria    =d.get("categoria"),
            descripcion  =d.get("descripcion"),
            monto        =d.get("monto"),
            fecha        =d.get("fecha")
        )
