import json
import numpy as np
import pandas as pd
from datetime import datetime


class TimeConverter:
    __column = ['invoice', 'sp2d', 'jenis', 'tgl_upload', 'jam_upload', 'tgl_selesai', 'jam_selesai', 'durasi']
    __toSecond = []
    lazySpm = []

    def __init__(self, datas):
        self.__datas = datas

    def durations(self):
        npa = np.array(self.__datas)
        df = pd.DataFrame(npa, columns=self.__column)
        return self.__convertDurationToSecond(df.durasi.tolist())

    def __convertDurationToSecond(self, datas):
        for data in datas:
            split = data.split(':')
            self.__converter(split)
        return self.__toSecond

    def __converter(self, time):
        durationsInSecond = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
        if durationsInSecond > 3600:
            self.lazySpm.append(durationsInSecond)
        self.__toSecond.append(durationsInSecond)


class GetParameter:
    def __init__(self, times, lateSpm, date):
        self.__times = times
        self.__lazySpm = lateSpm
        self.__date = date

    def __average(self):
        return np.mean(self.__times)

    def __toHour(self, number):
        return round(number/3600, 2)

    def __dateFormat(self, date):
        informated = datetime.strptime(self.__date, '%d-%m-%Y')
        return informated.strftime('%Y-%m-%d')

    def __lazySpmTotal(self):
        return len(self.__lazySpm)

    def __capaianPercentage(self):
        patuh = len(self.__times) - self.__lazySpmTotal()
        return round(patuh / len(self.__times), 2)

    def toJson(self):
        getJson = {'date': self.__dateFormat(self.__date), 'total': len(self.__times),
                   'average': self.__toHour(self.__average()), 'max': self.__toHour(max(self.__times)),
                   'min': self.__toHour(min(self.__times)), 'late': self.__lazySpmTotal(),
                   'capaian': self.__capaianPercentage()}
        return json.dumps(getJson)
