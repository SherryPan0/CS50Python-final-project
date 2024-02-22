from project import name_validate, get_authorID, get_papers

def main():
    test_name_validate()


def test_name_validate():
    assert name_validate("123") == False
    assert name_validate("Victor de Boer!") == False
    assert name_validate("Victor de Boer") == "victor+de+boer"


if __name__=="__main__":
    main()
