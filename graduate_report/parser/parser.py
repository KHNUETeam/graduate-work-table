import requests
import re
from bs4 import BeautifulSoup


class Parser:

    def __init__(self, search_str, year_start=None, year_stop=None):
        self.__search_str = search_str
        self.__count_on_page = 20
        self.__page = 1
        self.__count = None
        self.__year_start = year_start
        self.__year_stop = year_stop
        self.__session = requests.Session()
        self.__url = 'http://irbis-nbuv.gov.ua/cgi-bin/irbis64r_81/cgiirbis_64.exe'

        self.__get_count()
        self.collection = self.__collect_topicthesis()


    def __send_form(self, with_get=False):
        if with_get:
            responce = self.__session.get(
                'http://irbis-nbuv.gov.ua/cgi-bin/irbis64r_81/cgiirbis_64.exe?C21COM=F&I21DBN=ARD_EX&P21DBN=ARD&S21FMT=&S21ALL=&Z21ID='
            )

        data = {
            'I21DBN': 'ARD',
            'P21DBN': 'ARD',
            'S21REF': 10,
            'S21CNR': int(self.__count_on_page),
            'S21STN': int(self.__page),
            '2_S21P02': 1,
            '2_S21P03': 'K=',
            '2_S21P05': 'Ключевые слова',
            '2_S21STR': self.__search_str,
            '2_S21LOG': 0,
            '2_S21P01': 3,
            '1_S21P01': 2,
            '1_S21P03': 'RZN=',
            '1_S21P05': 'Тематика поиска',
            '1_S21STR': '',
            '4_S21P01': 2,
            '4_S21P03': 'KNS=',
            '4_S21P05': 'Спеціальність ВАК',
            '4_S21STR': '',
            '3_S21P01': 0,
            '3_S21P02': 1,
            '3_S21P03': 'A=',
            '3_S21P05': 'Автор',
            '3_S21STR': '',
            '5_S21P01': 2,
            '5_S21P03': 'G=',
            '5_S21P05': 'Год издания',
            '5_S21LOG': 5,
            '5_S21P06': 2000,
            '5_S21P07': 2002,
            'S21FMT': 'fullw',
            'C21COM': 'S',
            'C21COM1': 'Пошук'
        }

        responce = self.__session.post(self.__url, data=data)

        return responce.text


    def __get_count(self):
        prs = BeautifulSoup(self.__send_form(with_get=True), 'html.parser')
        self.__count = int(prs.find(
            'table',
            {
                'class': 'advanced',
                'bgcolor': 'WHITE',
                'border': 0
            }
        ).find_all(
            'td',
            {
                'align': 'left',
                'colspan': 4
            }
        )[1].find('b').text)

    def __collect_topicthesis(self):
        collection = [[]]
        coll_page = 0

        if self.__count:
            while self.__page < self.__count:
                print(self.__page)
                html = BeautifulSoup(self.__send_form(), 'html.parser')
                results = re.findall(
                    r'<tr width="100%">\s*<td valign="top" with="5%">\s*<b>\s*\d+\.\s*</b>\s*</td>\s*<td colspan="2" width="95%">\s*<hr noshade="" size="1"/>\s*<br[/]?>\s*<a href=".+" title="Пошук за автором">\s*([\w\s.]+)\s*</a>\s*<br/>\s*(<b>\s*([\w\d\s\'-:;,()-_]*\s*<b>\s*<font color="red">\s*\w+\s*</font>\s*</b>\s*[\w\d\s\'-:;,()-_]*)+\s*</b>).*\s*</td>\s*</tr>',
                    str(html)
                )

                print(results)

                for result in results:
                    if len(collection[coll_page]) < self.__count_on_page - 1:
                        collection[coll_page].append(
                            {
                                'fullname': result[0],
                                'theme': result[1]
                            }
                        )
                    else:
                        collection.append([])
                        coll_page += 1
                        collection[coll_page].append(
                            {
                                'fullname': result[0],
                                'theme': result[1]
                            }
                        )

                if self.__count - self.__page >= self.__count_on_page:
                    self.__page += self.__count_on_page
                else:
                    self.__page += self.__count - self.__page

        return collection