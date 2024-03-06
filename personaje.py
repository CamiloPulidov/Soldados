class IAttackBehavior():
    def Attack(self):
        pass

class AttEspada(IAttackBehavior):
    
    def Attack(self):
        print("ataque de espada")


class AttArco(IAttackBehavior):
    def Attack(self):
        print("ataque de arco")

class IMoveBehavior():
    def Move(self):
        pass

class MoveRapido(IMoveBehavior): 
    def Move(self):
        print("movimiento rapido")

class MoveLento(IMoveBehavior): 
    def Move(self):
        print("movimiento lento")

class Personaje():

    def __init__(self,att_behavior:IAttackBehavior,move_behavior:IMoveBehavior):
        self.att=att_behavior
        self.move=move_behavior
       
    def perform_att(self):
        self.att.Attack()

    def perform_move(self):
        self.move.Move()

   

class Arquero(Personaje):
    def __init__(self):
        super().__init__(AttArco(),MoveRapido())
   

    
class Guerrero(Personaje):
    def __init__(self):
        super().__init__(AttEspada(),MoveLento())

if __name__=="__main__":
    arquero=Arquero()
    arquero.perform_att()
    arquero.perform_move()

    espadachin=Guerrero()
    espadachin.perform_att()
    espadachin.perform_move()

  

