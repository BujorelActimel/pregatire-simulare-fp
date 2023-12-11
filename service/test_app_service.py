from service import AppService
from repo import FurnitureRepo

def test_searchByType():
    repo = FurnitureRepo("service/test_data.csv")
    service = AppService(repo)

    assert service.searchByType("masa") == repo.furniture_list[0:2]
