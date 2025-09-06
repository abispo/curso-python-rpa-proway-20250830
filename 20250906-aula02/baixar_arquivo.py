import requests


if __name__ == "__main__":

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',  # Do Not Track
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}
    url = "https://www.ceasa.sc.gov.br/index.php/cotacao-de-precos/2025/01-janeiro-17/2734-31-01-2025/file"
    response = requests.get(url, headers=headers)

    content = response.content

    with open("arquivo_teste.pdf", 'wb') as _file:
        _file.write(content)