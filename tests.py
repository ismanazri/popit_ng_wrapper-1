import popit_ng


def test_baseentity_fetch_person():
    entity = popit_ng.BaseEntity("persons", language="en", id="55b4c72c98f2c81a501e11f4")
    assert entity.data

def test_base_data():
    entity = popit_ng.BaseEntity("persons", language="en", id="55b4c72c98f2c81a501e11f4")

    assert type(entity.data) == dict

def tests_persons_name():
    person = popit_ng.Person(language="en", id="55b4c72c98f2c81a501e11f4")
    assert person.name == "Ng Eng Tee"
