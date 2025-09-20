"""
Criar um robô que irá acessar a página do ceasa de santa catarina (https://www.ceasa.sc.gov.br/index.php/cotacao-de-precos). Esse robô irá acessar cada pasta e subpasta dessa página, e irá fazer o download dos arquivos PDF. Se possível, manter a mesma estrutura de pastas localmente. Como um bônus, ler o conteúdo dos arquivos e salvar no banco de dados. Para esse último item, pesquise a biblioteca markitdown, ou utilize outra de sua escolha.
"""

import asyncio
import aiohttp
import os
from urllib.parse import urljoin

from bs4 import BeautifulSoup

BASE_URL = "https://www.ceasa.sc.gov.br/index.php/cotacao-de-precos"
visited = set()
processed = set()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}
lock = asyncio.Lock()

def next_page(soup: BeautifulSoup):
    try:
        next_arrow = soup.find('a', string="»")
        if next_arrow and next_arrow.get("href"):
            full_url = urljoin(BASE_URL, next_arrow["href"])
            
            if full_url != BASE_URL:
                return full_url
            
        return None

    except Exception as e:
        print(f"Erro ao processar a próxima página: {e}")

def create_folder(url: str) -> str:
    url_items = url.split('/')[-5:][:-2]
    folder_path = os.path.join(*url_items)
    os.makedirs(folder_path, exist_ok=True)

    return folder_path

def extract_filename(url) -> str:
    return f"{url[:-5][-10:]}.pdf"

async def download_pdf(session: aiohttp.ClientSession, url: str):

    async with lock:
        if url in processed:
            return
        processed.add(url)

    try:
        async with session.get(url, headers=headers) as response:
            folder_path = create_folder(url=url)
            filename = extract_filename(url=url)
            filepath = os.path.join(folder_path, filename)
            content = await response.read()

            with open(file=filepath, mode='wb') as _file:
                _file.write(content)

            print(f"Arquivo '{filename}' processado.")

    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}.")

async def process_page(session: aiohttp.ClientSession, url: str):

    async with lock:
        if url in visited:
            return
        visited.add(url)

    print('='*30)
    print(f"=== PROCESSANDO PÁGINA '{url}' ===")

    try:
        async with session.get(url, headers=headers) as response:

            soup = BeautifulSoup(await response.text(), "html.parser")

            tasks = []

            for link in soup.find_all("a", class_="koowa_header__link"):
                href = link.get("href")
                full_url = urljoin(url, href)
                tasks.append(process_page(session=session, url=full_url))

            for link in soup.find_all("a", class_="koowa_header__image_link"):
                href = link.get("href")
                full_url = urljoin(url, href)
                tasks.append(download_pdf(session=session, url=full_url))

            next_page_url = next_page(soup=soup)
            if next_page_url and next_page_url not in visited:
                tasks.append(process_page(session, url=next_page_url))

            if tasks:
                await asyncio.gather(*tasks)
                print(f"{len(tasks)} arquivos processados")

    except Exception as e:
        print(f"Erro ao processar a requisição: {e}.")

async def main():
    async with aiohttp.ClientSession() as session:
        await process_page(session, url=BASE_URL)

if __name__ == "__main__":
    asyncio.run(main())