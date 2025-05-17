from extentions import db

class Feira(db.Model):
    __tablename__ = 'feiras'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    data_inicio = db.Column(db.String(20))
    data_termino = db.Column(db.String(20))
    local = db.Column(db.String(100))
    cidade = db.Column(db.String(50))
    estado = db.Column(db.String(2))

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "data_inicio": self.data_inicio,
            "data_termino": self.data_termino,
            "local": self.local,
            "cidade": self.cidade,
            "estado": self.estado,
        }

    @classmethod
    def criar_feira(cls, data):
        if "nome" not in data or not data["nome"]:
            raise ValueError("Campo 'nome' é obrigatório")

        feira = cls(
            nome=data['nome'],
            descricao=data.get('descricao'),
            data_inicio=data.get('data_inicio'),
            data_termino=data.get('data_termino'),
            local=data.get('local'),
            cidade=data.get('cidade'),
            estado=data.get('estado')
        )
        db.session.add(feira)
        db.session.commit()
        return feira
