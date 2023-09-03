import requests, bs4, re

if __name__ == '__main__':
    URL = 'https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy83MTBiOTk4L3BvZGNhc3QvcnNz?hl=pt-br'
    pattern = r'Livros citados no episódio:(.*?)Nossas redes'
    file = open('livros_recomendados.txt', "w")
    try:
        res = requests.get(URL)
        res_html = bs4.BeautifulSoup(res.text, 'html.parser')
        episodes_html = res_html.select('a[role] .LrApYe[role="presentation"]')
        
        print('Scrapping...')

        for episode_html in episodes_html:
            matches = re.findall(pattern, episode_html.string, re.DOTALL)
            for match in matches:
                file.write('{}\n'.format(match.strip()))
            file.write('\n****************\n')
        file.close()
        print('done!')
    except Exception as exc:
        print('There was a problem: %s' % (exc))