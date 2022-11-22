from __init__ import client
import io

def test_landing(client):
    """
    Test the landing page
    """
    rv = client.get('/')
    html = rv.data.decode()

    assert client.get('/home').data == rv.data
    assert rv.status_code == 200

def test_file_upload(client):
    """
    Test file upload
    """
    filename = 'test_data/test_data.las'
    data = {'las_file': (io.BytesIO(b"some initial text data"), filename)}
    response = client.post('/home', data=data, follow_redirects=True)

    assert response.status_code == 200

def test_stop_visualization(client):
    """
    Test stop visualization
    """
    response = client.post('/stop_visualization', follow_redirects=True)

    assert response.status_code == 200
