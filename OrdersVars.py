from datetime import date
import random
from datetime import datetime, timedelta
import locale


class OrdersVars(object):
    Document = ""
    varsList = []
    numList = []
    my_date = date.today().strftime('%d.%m.%Y')
    my_time = datetime.now().strftime('%H:%M:%S')

    def __init__(self):
        self.str1 = "1CClientBankExchange" + "\r\n" + \
                    "ВерсияФормата=" + "1.01" + "\r\n" + \
                    "Кодировка=" + "Windows" + "\r\n" + \
                    "Отправитель=Альфа-Бизнес Онлайн" + "\r\n"
        '''
        ДатаСоздания=17.11.2020
        ВремяСоздания=11:45:54
        ДатаНачала=01.05.2020
        ДатаКонца=01.09.2020
        '''
        self.str2 = "Получатель=" + "\r\n" + "ДатаСоздания=" + self.gen_datetime(0) + "\r\n" + \
                    "ВремяСоздания=" + self.gen_datetime(1) + "\r\n" + \
                    "ДатаНачала=" + self.my_date + "\r\n" + \
                    "ДатаКонца=" + self.my_time + "\r\n"

        """
        РасчСчет=40702810102860003014
        СекцияРасчСчет
        РасчСчет=40702810102860003014
        КонецРасчСчет
        """
        self.str3 = "РасчСчет=" + self.gen_random_number(20) + "\r\n" \
                    + "СекцияРасчСчет" + "\r\n" + \
                    "РасчСчет=" + self.gen_random_number(20) + "\r\n" + \
                    "КонецРасчСчет" + "\r\n"

        """
        СекцияДокумент=Банковский ордер
        Номер=64
        Дата=01.09.2020
        Сумма=20000.00
        """
        self.str4 = "СекцияДокумент=" + "Банковский орде" + "\r\n" + \
                    "Номер=" + self.gen_random_number(2) + "\r\n" + \
                    "Дата=" + self.gen_datetime(0) + "\r\n" + \
                    "Сумма=" + self.gen_random_number(5) + "." + \
                    self.gen_random_number(2) + "\r\n" + \
                    "ПлательщикСчет=" + self.gen_random_number(20) + "\r\n"

        """
        ДатаСписано=02.09.2020
        Плательщик=Общество с ограниченной ответственностью "ЭлПроф"
        ПлательщикИНН=7727302470
        ПолучательСчет=40702810510000507837
        """
        self.str5 = "ДатаСписано=" + self.gen_datetime(0) + "\r\n" + \
                    "Плательщик=" + "Общество с ограниченной ответственностью \"ЭлПроф\"" + "\r\n" + \
                    "ПлательщикИНН=" + self.gen_random_number(10) + "\r\n" + \
                    "ПолучательСчет=" + self.gen_random_number(20) + "\r\n"

        """
        ДатаПоступило=
        Получатель=ООО "ЭЛЕКТРОТК"
        ПолучательИНН=7735180881
        НазначениеПлатежа=Комиссия
        КонецДокумента
        """
        self.str6 = "ДатаПоступило=" + "" + "\r\n" + \
                    "Получатель=" + "ООО \"ЭЛЕКТРОТК\"" + "\r\n" \
                                                          "ПолучательИНН=" + self.gen_random_number(10) + "\r\n" + \
                    "НазначениеПлатежа=" + "Комиссия" + "\r\n" + \
                    "КонецДокумента"

        """
        СекцияДокумент=Платежное поручение
        Номер=93
        Дата=03.10.2020
        Сумма=29000.00
        ПлательщикСчет=40702810102860003014
        """
        self.str7 = "СекцияДокумент=" + "Платежное поручение" + "\r\n" + \
                    "Номер=" + self.gen_random_number(3) + "\r\n" + \
                    "Дата=" + self.gen_datetime(0) + "\r\n" + \
                    "Сумма=" + self.gen_random_number(6) + "." + self.gen_random_number(2) + "\r\n" + \
                    "ПлательщикСчет=" + self.gen_datetime(20) + "\r\n"

        """
        ДатаСписано=02.09.2020
        Плательщик=Общество с ограниченной ответственностью "ЭлПроф"
        ПлательщикИНН=7727302470
        ПолучательСчет=40702810510000507837
        """
        self.str8 = "ДатаСписано=" + self.gen_datetime(0) + "\r\n" + \
                    "Плательщик=" + "Общество с ограниченной ответственностью \"ЭлПроф\"" + "\r\n" + \
                    "ПлательщикИНН=" + self.gen_random_number(10) + "\r\n" + \
                    "ПолучательСчет=" + self.gen_random_number(20) + "\r\n"

        """
        ДатаПоступило=
        Получатель=ООО "ЭЛЕКТРОТК"
        ПолучательИНН=7735180881
        НазначениеПлатежа=Оплата по  Договору
        """
        self.str9 = "ДатаПоступило=" + "" + "\r\n" + \
                    "Получатель=" + "ООО \"ЭЛЕКТРОТК\"" + "\r\n" + \
                    "ПолучательИНН=" + self.gen_random_number(10) + "\r\n" + \
                    "НазначениеПлатежа=" + "Оплата по  Договору" + "\r\n" + \
                    "КонецДокумента" + "\r\n"

        """
        СекцияДокумент=Платежное поручение
        Номер=29437
        Дата=02.10.2020
        Сумма=21000.00
        ПлательщикСчет=40702810510000507837
        """
        self.str10 = "СекцияДокумент=" + "Платежное поручение" + "\r\n" + \
                     "Номер=" + self.gen_random_number(6) + "\r\n" + "Дата=" + self.gen_datetime(0) + "\r\n" + \
                     "Сумма=" + self.gen_random_number(7) + "." + self.gen_random_number(2) + "\r\n" \
                     + "ПлательщикСчет=" + self.gen_random_number(20) + "\r\n"
        """
        ДатаСписано=
        Плательщик=ООО "ЭЛЕКТРОТК"
        ПлательщикИНН=7735180881
        ПолучательСчет=40702810102860003014
        """
        self.str11 = "ДатаСписано=" + "" + "\r\n" + \
                     "Плательщик=" + "ООО \"ЭЛЕКТРОТК\"" + "\r\n" + \
                     "ПлательщикИНН=" + self.gen_random_number(10) + "\r\n" + \
                     "ПолучательСчет=" + self.gen_random_number(20) + "\r\n"

        """
        ДатаПоступило=02.09.2020
        Получатель=ООО "ЭЛПРОФ"
        ПолучательИНН=7727302470
        НазначениеПлатежа=ОПЛ. ПО СЧ
        КонецДокумента
        КонецФайла
        """
        self.str12 = "ДатаПоступило=" + self.gen_datetime(0) + "\r\n" + \
                     "Получатель=" + "ООО \"ЭЛПРОФ\"" + "\r\n" + \
                     "ПолучательИНН=" + self.gen_random_number(10) + "\r\n" + \
                     "НазначениеПлатежа=" + "ОПЛ. ПО СЧ" + "\r\n" + \
                     "КонецДокумента" + "\r\n" + \
                     "КонецФайла" + "\r\n"
        self.Document = self.str1 + self.str2 + \
            self.str3 + self.str4 + \
            self.str5 + self.str6 + \
            self.str7 + self.str8 + \
            self.str9 + self.str10 + \
            self.str11 + self.str12

    def gen_random_number(self, dl):
        interval = ""
        if dl <= 0:
            print('error: digitsLen < or = null, try 9 - 999999999')
            return 0
        for x in range(dl):
            interval = interval + '9'
        f_ma = '{0:0' + str(dl) + '}'
        vlv = f_ma.format(random.randint(1, int(interval)))
        if len(self.numList) <= 0:
            self.numList.append(vlv)
        for item in self.numList:
            if item == vlv:
                self.gen_random_number(dl)
            else:
                self.numList.append(vlv)
                return vlv
        return vlv
    '''
    если присвоить:
    Время года месяцы день selector = 0
    часы минуты секунды selector = 1
    '''
    def gen_datetime(self, selector):
        min_year = 2019
        max_year = datetime.now().year
        lo = ['ru_RU']
        data_ff = ['%d.%m.%Y']
        if selector == 1:
            data_ff = ['%H:%M:%S']   # generate a datetime
        start = datetime(min_year, 1, 1)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        format_date = data_ff[random.randint(0, len(data_ff) - 1)]
        locale_date = lo[random.randint(0, len(lo) - 1)]
        try:
            locale.setlocale(locale.LC_ALL, locale_date)  # generate error if local are not available on your computer
        except ArithmeticError:
            locale.setlocale(locale.LC_ALL, '')
        bvr = (start + (end - start) * random.random()).strftime(format_date)
        if len(self.varsList) <= 0:
            self.varsList.append(bvr)
        for item in self.varsList:
            if item == bvr:
                self.gen_datetime(selector)
            else:
                self.varsList.append(bvr)
                return bvr
        return bvr

    def client_bank_doc_full(self):
        return self.Document


def make():
    doc = OrdersVars()
    return doc.Document
