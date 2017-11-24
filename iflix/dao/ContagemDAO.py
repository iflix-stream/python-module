from iflix.models.AssistindoFilme import AssistindoFilme
from iflix.models.AssistindoSerie import AssistindoSerie
from iflix.models.banco import bd


class ContagemDAO:
    def retreave(self, args):
        session = bd()
        a = session.query(AssistindoFilme).count()
        b = session.query(AssistindoSerie).count()
        return a+b
