import requests

def test_products_json():
    response = requests.get('http://127.0.0.1:5000/products?source=json')
    assert response.status_code == 200, "Failed: JSON source did not return status code 200"
    print("Success: JSON source returned status code 200")

if __name__ == "__main__":
    test_products_json()
