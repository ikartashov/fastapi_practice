from routers.users import add_user

class Test:
    pass

class TestRouter:
    def test_add_user_short_name_error(self, client):
        response = client.post('/users/post_new_user',
                               json={'name': 'A'})
        assert response.status_code == 422
        assert response.json()['detail'] == 'Длина имени не соответствует'




    def test_get_users(self,client):
        response = client.get('/users/get_users')
        assert response is not None
        assert response.status_code == 200
