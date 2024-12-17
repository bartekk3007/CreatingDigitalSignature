from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generowanie pary kluczy
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

def createSignature(dataStrng):
    data = dataStrng.encode('utf-8')
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

data_string = '[{"date": "2024/11/21, 10:45:59", "ip": "192.168.0.103", "message": "-----BEGIN ENCRYPTED KEY-----\nj2TtUtBEAco83qsixsIliKB1Y1Mm16XDQl+G+tTx/6S9wVu0dE9C83nCaeMah1wejNXgpeRANDNWcIzZbMcDt7o4yPHVbHzfoUXmfrrk6IrEYW95pfDDAOznPpm0c4Ms4FN0QIjn3rbvSuC6TF/B+SFkbnEbnEEKe86jBNv2Ou2K4lfS5ramelbirk/aU3YUnjG0MdZxFuNL2kdqAr6iUtC/9jgYui7YtwAVa2qFvn2ytjn3xZp4lRhtViVtHpTdLskQP+l6bn7b/mQaXB9Memif13HBlW3NmfgIGu71cX2ocjIJxv4MaSWHqV4LM1NskxztjI6+b4Vy1NSII8cIpg==\n", "port": 56860, "user": "192.168.0.103:56860"}, {"date": "2024/11/21, 10:45:59", "ip": "192.168.0.103", "message": "-----BEGIN ENCRYPTED KEY-----\nj2TtUtBEAco83qsixsIliKB1Y1Mm16XDQl+G+tTx/6S9wVu0dE9C83nCaeMah1wejNXgpeRANDNWcIzZbMcDt7o4yPHVbHzfoUXmfrrk6IrEYW95pfDDAOznPpm0c4Ms4FN0QIjn3rbvSuC6TF/B+SFkbnEbnEEKe86jBNv2Ou2K4lfS5ramelbirk/aU3YUnjG0MdZxFuNL2kdqAr6iUtC/9jgYui7YtwAVa2qFvn2ytjn3xZp4lRhtViVtHpTdLskQP+l6bn7b/mQaXB9Memif13HBlW3NmfgIGu71cX2ocjIJxv4MaSWHqV4LM1NskxztjI6+b4Vy1NSII8cIpg==\n", "port": 56860, "user": "192.168.0.103:56860"}, {"date": "2024/11/21, 10:46:13", "ip": "192.168.0.103", "message": "BlUPbPgV5d6kDrv1pbaHcw==", "port": 56860, "user": "192.168.0.103:14101"}, {"date": "2024/11/21, 10:46:15", "ip": "192.168.0.103", "message": "ZNufnKa2p9R57vYWxHOVDQ==", "port": 14101, "user": "192.168.0.103:56860"}]'
digitalSignature = createSignature(data_string)
print("type")