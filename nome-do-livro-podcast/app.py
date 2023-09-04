import requests, bs4, re

if __name__ == '__main__':
    URL = 'https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy83MTBiOTk4L3BvZGNhc3QvcnNz?hl=pt-br'
    pattern = r'(?:Livros citados no episódio:|citados:|citadas:)(.*?)(?=Nossas redes|$)'
    file = open('livros_recomendados.txt', "w")
    try:
        res = requests.get(URL)
        res_html = bs4.BeautifulSoup(res.text, 'html.parser')
        episodes_html = res_html.select('a[role="listitem"]')
        
        print('Scrapping...')

        for episode_html in episodes_html:
            episode_title_html = episode_html.select('.e3ZUqe')[0]
            book_recommendations_html = episode_html.select('.LrApYe[role="presentation"]')[0]
            book_matches = re.findall(pattern, book_recommendations_html.string, re.DOTALL)

            file.write('Episódio: {}\n\n'.format(episode_title_html.string))
            for match in book_matches:
                file.write('{}\n'.format(match.strip()))

            file.write('\n****************\n')

        file.close()
        print('done!')
    except Exception as exc:
        print('There was a problem: %s' % (exc))