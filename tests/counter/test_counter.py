from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "Python") == 1639


# pega o arquivo e procura qual palavra vai ser encontrada.
# laura dias me ajudou a entender e executar o teste corretamente
