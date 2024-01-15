from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

BASEMODEL = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Or(Not(And(AKnight, AKnave))),
    Or(Not(And(BKnight, BKnave))),
    Or(Not(And(CKnight, CKnave)))
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    BASEMODEL,
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # if A is a knight then he implies the both knaves statement
    # if A is a knave then he implies not of the both knaves statement
    BASEMODEL,
    Implication(AKnight, And(BKnave, AKnave)),
    Implication(AKnave, BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # if A is a knight then he implies that both A and B are knights.
    # if A is knave then he implies B is a knight
    # if B is knight then he implies that A is knave
    # if B is knave then he implies A is a Knave
    BASEMODEL,
    Implication(AKnight, BKnight),
    Implication(BKnight, AKnave),
    Implication(AKnave, BKnight),
    Implication(BKnave, AKnave)

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    BASEMODEL,
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    Implication(AKnight, BKnave),
    Implication(AKnave, BKnight),
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
