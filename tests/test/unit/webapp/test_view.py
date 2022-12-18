from __init__ import client
import io


"""
Test the landing page
"""
def test_landing(client):
    rv = client.get('/')
    html = rv.data.decode()

    assert client.get('/home').data == rv.data
    assert rv.status_code == 200

"""
Test file upload
"""
def test_file_upload(client):
    filename = 'test_data/test_data.las'
    data = {'las_file': (io.BytesIO(b"some initial text data"), filename)}
    response = client.post('/home', data=data, follow_redirects=True)

    assert response.status_code == 200

"""
Test stop visualization
"""
def test_stop_visualization(client):
    response = client.post('/stop_visualization', follow_redirects=True)

    assert response.status_code == 200

"""
Test stop visualization
"""
def test_visualization(client):
    # test visualize button while no file uploaded
    filename = ''
    data = {'las_file': (io.BytesIO(b"some initial text data"), filename)}
    response = client.post('/visualize', data=data, follow_redirects=True)
    assert response.status_code == 200

    # test visualize button with a file uploaded
    filename = 'test_data/test_data.las'
    data = {'las_file': (io.BytesIO(b"some initial text data"), filename)}
    response = client.post('/visualize', data=data, follow_redirects=True)
    assert response.status_code == 200







