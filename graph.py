#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:55:10 2024

@author: rodolfodom
"""

linea_1 = {
    "Pantitlán-1": {
        "Zaragoza": 1320,
        "Pantitlán-9": 300,
        "Pantitlán-A": 300,
        "Pantitlán-5": 300,
    },
    "Zaragoza": {"Gómez Farías": 762, "Pantitlán-1": 1320},
    "Gómez Farías": {"Boulevard Puerto Aéreo": 595, "Zaragoza": 762},
    "Boulevard Puerto Aéreo": {"Balbuena": 595, "Gómez Farías": 595},
    "Balbuena": {"Moctezuma": 703, "Boulevard Puerto Aéreo": 595},
    "Moctezuma": {"San Lázaro-1": 478, "Balbuena": 703},
    "San Lázaro-1": {"Candelaria-1": 866, "San Lázaro-B": 300, "Moctezuma": 478},
    "Candelaria-1": {"Merced": 698, "Candelaria-4": 300, "San Lázaro-1": 866},
    "Merced": {"Pino Suárez-1": 745, "Candelaria-1": 698},
    "Pino Suárez-1": {"Isabel la Católica": 382, "Pino Suárez-2": 300, "Merced": 745},
    "Isabel la Católica": {"Salto del Agua-1": 445, "Pino Suárez-1": 382},
    "Salto del Agua-1": {"Balderas-1": 458, "Salto del Agua-8": 300, "Isabel la Católica": 445},
    "Balderas-1": {"Cuauhtémoc": 409, "Balderas-3": 300, "Salto del Agua-1": 458},
    "Cuauhtémoc": {"Insurgentes": 793, "Balderas-1": 409},
    "Insurgentes": {"Sevilla": 645, "Cuauhtémoc": 793},
    "Sevilla": {"Chapultepec": 501, "Insurgentes": 645},
    "Chapultepec": {"Juanacatlán": 973, "Sevilla": 501},
    "Juanacatlán": {"Tacubaya-1": 1158, "Chapultepec": 973},
    "Tacubaya-1": {"Observatorio": 1262, "Tacubaya-9": 300, "Tacubaya-7": 300, "Juanacatlán": 1158},
    "Observatorio": {"Tacubaya-1": 1262},
}


linea_2 = {
    "Cuatro Caminos": {"Panteones": 1639},
    "Panteones": {"Tacuba-2": 1416, "Cuatro Caminos": 1639},
    "Tacuba-2": {"Cuitláhuac": 637, "Tacuba-7": 300, "Panteones": 1416},
    "Cuitláhuac": {"Popotla": 620, "Tacuba-2": 637},
    "Popotla": {"Colegio Militar": 462, "Cuitláhuac": 620},
    "Colegio Militar": {"Normal": 516, "Popotla": 462},
    "Normal": {"San Cosme": 657, "Colegio Militar": 516},
    "San Cosme": {"Revolución": 537, "Normal": 657},
    "Revolución": {"Hidalgo-2": 587, "San Cosme": 537},
    "Hidalgo-2": {"Bellas Artes-2": 447, "Hidalgo-3": 300, "Revolución": 587},
    "Bellas Artes-2": {"Allende": 387, "Bellas Artes-8": 300, "Hidalgo-2": 447},
    "Allende": {"Zócalo/Tenochtitlan": 602, "Bellas Artes-2": 387},
    "Zócalo/Tenochtitlan": {"Pino Suárez-2": 745, "Allende": 602},
    "Pino Suárez-2": {"San Antonio Abad": 817, "Pino Suárez-1": 300, "Zócalo/Tenochtitlan": 745},
    "San Antonio Abad": {"Chabacano-2": 642, "Pino Suárez-2": 817},
    "Chabacano-2": {"Viaducto": 774, "Chabacano-8": 300, "Chabacano-9": 300, "San Antonio Abad": 642},
    "Viaducto": {"Xola": 490, "Chabacano-2": 774},
    "Xola": {"Villa de Cortés": 698, "Viaducto": 490},
    "Villa de Cortés": {"Nativitas": 750, "Xola": 698},
    "Nativitas": {"Portales": 924, "Villa de Cortés": 750},
    "Portales": {"Ermita-2": 748, "Nativitas": 924},
    "Ermita-2": {"General Anaya": 838, "Ermita-12": 300, "Portales": 748},
    "General Anaya": {"Tasqueña": 1330, "Ermita-2": 838},
    "Tasqueña": {"General Anaya": 1330},
}

linea_3 = {
    "Indios Verdes": {"Deportivo 18 de Marzo-3": 1166},
    "Deportivo 18 de Marzo-3": {"Potrero": 966, "Deportivo 18 de Marzo-6": 300, "Indios Verdes": 1166},
    "Potrero": {"La Raza-3": 1106, "Deportivo 18 de Marzo-3": 966},
    "La Raza-3": {"Tlatelolco": 1445, "La Raza-5": 300, "Potrero": 1106},
    "Tlatelolco": {"Guerrero-3": 1042, "La Raza-3": 1445},
    "Guerrero-3": {"Hidalgo-3": 702, "Guerrero-B": 300, "Tlatelolco": 1042},
    "Hidalgo-3": {"Juárez": 251, "Hidalgo-2": 300, "Guerrero-3": 702},
    "Juárez": {"Balderas-3": 659, "Hidalgo-3": 251},
    "Balderas-3": {"Niños Héroes": 665, "Balderas-1": 300, "Juárez": 659},
    "Niños Héroes": {"Hospital General": 559, "Balderas-3": 665},
    "Hospital General": {"Centro Médico-3": 653, "Niños Héroes": 559},
    "Centro Médico-3": {
        "Etiopía/Plaza de la Transparencia": 1119,
        "Centro Médico-9": 300,
        "Hospital General": 653,
    },
    "Etiopía/Plaza de la Transparencia": {"Eugenia": 950, "Centro Médico-3": 1119},
    "Eugenia": {"División del Norte": 715, "Etiopía/Plaza de la Transparencia": 950},
    "División del Norte": {"Zapata-3": 794, "Eugenia": 715},
    "Zapata-3": {"Coyoacán": 1153, "Zapata-12": 300, "División del Norte": 794},
    "Coyoacán": {"Viveros/Derechos Humanos": 908, "Zapata-3": 1153},
    "Viveros/Derechos Humanos": {"Miguel Ángel de Quevedo": 824, "Coyoacán": 908},
    "Miguel Ángel de Quevedo": {"Copilco": 1295, "Viveros/Derechos Humanos": 824},
    "Copilco": {"Universidad": 1306, "Miguel Ángel de Quevedo": 1295},
    "Universidad": {"Copilco": 1306},
}

linea_4 = {
    "Santa Anita-4": {"Jamaica-4": 758, "Santa Anita-8": 300},
    "Jamaica-4": {"Fray Servando": 1033, "Jamaica-9": 300, "Santa Anita-4": 758},
    "Fray Servando": {"Candelaria-4": 633, "Jamaica-4": 1033},
    "Candelaria-4": {"Morelos-4": 1062, "Candelaria-1": 300, "Fray Servando": 633},
    "Morelos-4": {"Canal del Norte": 910, "Morelos-B": 300, "Candelaria-4": 1062},
    "Canal del Norte": {"Consulado-4": 884, "Morelos-4": 910},
    "Consulado-4": {"Bondojito": 645, "Consulado-5": 300, "Canal del Norte": 884},
    "Bondojito": {"Talisman": 959, "Consulado-4": 645},
    "Talisman": {"Martín Carrera-4": 1129, "Martín Carrera-6": 300, "Bondojito": 959},
    "Martín Carrera-4": {"Talismán": 1129},
}

linea_5 = {
    "Politécnico": {"Instituto del Petróleo-5": 1188},
    "Instituto del Petróleo-5": {
        "Autobuses del Norte": 1067,
        "Instituto del Petróleo-6": 300,
        "Politécnico": 1188,
    },
    "Autobuses del Norte": {"La Raza-5": 975, "Instituto del Petróleo-5": 1067},
    "La Raza-5": {"Misterios": 892, "La Raza-3": 300, "Autobuses del Norte": 975},
    "Misterios": {"Valle Gómez": 969, "La Raza-5": 892},
    "Valle Gómez": {"Consulado-5": 679, "Misterios": 969},
    "Consulado-5": {"Eduardo Molina": 815, "Consulado-4": 300, "Valle Gómez": 679},
    "Eduardo Molina": {"Aragón": 860, "Consulado-5": 815},
    "Aragón": {"Oceanía-5": 1219, "Eduardo Molina": 860},
    "Oceanía-5": {"Terminal Aérea": 1174, "Oceanía-B": 300, "Aragón": 1219},
    "Terminal Aérea": {"Hangares": 1153, "Oceanía-5": 1174},
    "Hangares": {"Pantitlán-5": 1644, "Terminal Aérea": 1153},
    "Pantitlán-5": {"Pantitlán-1": 300, "Pantitlán-9": 300, "Pantitlán-A": 300, "Hangares": 1644},
}

linea_6 = {
    "El Rosario-6": {"Tezozómoc": 1257, "El Rosario-7": 300},
    "Tezozómoc": {"Azcapotzalco": 973, "El Rosario-6": 1257},
    "Azcapotzalco": {"Ferrería": 1173, "Tezozómoc": 973},
    "Ferrería": {"Norte 45": 1072, "Azcapotzalco": 1173},
    "Norte 45": {"Vallejo": 660, "Ferrería": 1072},
    "Vallejo": {"Instituto del Petróleo-6": 755, "Norte 45": 660},
    "Instituto del Petróleo-6": {"Lindavista": 1258, "Instituto del Petróleo-5": 300, "Vallejo": 755},
    "Lindavista": {"Deportivo 18 de Marzo-6": 1075, "Instituto del Petróleo-6": 1258},
    "Deportivo 18 de Marzo-6": {
        "La Villa/Basílica": 570,
        "Deportivo 18 de Marzo-3": 300,
        "Lindavista": 1075,
    },
    "La Villa/Basílica": {"Martín Carrera": 1141, "Deportivo 18 de Marzo-6": 570},
    "Martín Carrera-6": {"Martín Carrera-4": 300, "La Villa/Basílica": 1141},
}

linea_7 = {
    "El Rosario-7": {"Aquiles Serdán": 1615, "El Rosario-6": 300},
    "Aquiles Serdán": {"Camarones": 1402, "El Rosario-7": 1615},
    "Camarones": {"Refinería": 952, "Aquiles Serdán": 1402},
    "Refinería": {"Tacuba-7": 1295, "Camarones": 952},
    "Tacuba-7": {"San Joaquín": 1433, "Tacuba-2": 300, "Refinería": 1295},
    "San Joaquín": {"Polanco": 1163, "Tacuba-7": 1433},
    "Polanco": {"Auditorio": 812, "San Joaquín": 1163},
    "Auditorio": {"Constituyentes": 1430, "Polanco": 812},
    "Constituyentes": {"Tacubaya-7": 1005, "Auditorio": 1430},
    "Tacubaya-7": {
        "San Pedro de los Pinos": 1084,
        "Tacubaya-1": 300,
        "Tacubaya-9": 300,
        "Constituyentes": 1005,
    },
    "San Pedro de los Pinos": {"San Antonio": 606, "Tacubaya-7": 1084},
    "San Antonio": {"Mixcoac": 788, "San Pedro de los Pinos": 606},
    "Mixcoac-7": {"Barranca del Muerto": 1476, "Mixcoac-12": 300, "San Antonio": 788},
    "Barranca del Muerto": {"Mixcoac-7": 1476},
}

linea_8 = {
    "Garibaldi-8": {"Bellas Artes-8": 634, "Garibaldi-B": 300},
    "Bellas Artes-8": {"San Juan de Letrán": 456, "Bellas Artes-2": 300, "Garibaldi-8": 634},
    "San Juan de Letrán": {"Salto del Agua-8": 292, "Bellas Artes-8": 456},
    "Salto del Agua-8": {"Doctores": 564, "Salto del Agua-1": 300, "San Juan de Letrán": 292},
    "Doctores": {"Obrera": 761, "Salto del Agua-8": 564},
    "Obrera": {"Chabacano-8": 1143, "Doctores": 761},
    "Chabacano-8": {"La Viga": 843, "Chabacano-2": 300, "Chabacano-9": 300, "Obrera": 1143},
    "La Viga": {"Santa Anita-8": 633, "Chabacano-8": 843},
    "Santa Anita-8": {"Coyuya": 968, "Santa Anita-4": 300, "La Viga": 633},
    "Coyuya": {"Iztacalco": 993, "Santa Anita-8": 968},
    "Iztacalco": {"Apatlaco": 910, "Coyuya": 993},
    "Apatlaco": {"Aculco": 534, "Iztacalco": 910},
    "Aculco": {"Escuadrón 201": 789, "Apatlaco": 534},
    "Escuadrón 201": {"Atlalilco-8": 1738, "Aculco": 789},
    "Atlalilco-8": {"Iztapalapa": 732, "Atlalilco-12": 300, "Escuadrón 201": 1738},
    "Iztapalapa": {"Cerro de la Estrella": 717, "Atlalilco-8": 732},
    "Cerro de la Estrella": {"UAM I": 1135, "Iztapalapa": 717},
    "UAM I": {"Constitución de 1917": 1137, "Cerro de la Estrella": 1135},
    "Constitución de 1917": {"UAM I": 1137},
}

linea_9 = {
    "Pantitlán-9": {
        "Puebla": 1380,
        "Pantitlán-1": 300,
        "Pantitlán-5": 300,
        "Pantitlán-A": 300,
    },
    "Puebla": {"Ciudad Deportiva": 800, "Pantitlán-9": 1380},
    "Ciudad Deportiva": {"Velódromo": 1110, "Puebla": 800},
    "Velódromo": {"Mixiuhca": 821, "Ciudad Deportiva": 1110},
    "Mixiuhca": {"Jamaica-9": 942, "Velódromo": 821},
    "Jamaica-9": {"Chabacano-9": 1031, "Jamaica-4": 300, "Mixiuhca": 942},
    "Chabacano-9": {"Lázaro Cárdenas": 1000, "Chabacano-8": 300, "Chabacano-2": 300, "Jamaica-9": 1031},
    "Lázaro Cárdenas": {"Centro Médico-9": 1059, "Chabacano-9": 1000},
    "Centro Médico-9": {"Chilpancingo": 1152, "Centro Médico-3": 300, "Lázaro Cárdenas": 1059},
    "Chilpancingo": {"Patriotismo": 955, "Centro Médico-9": 1152},
    "Patriotismo": {"Tacubaya-9": 1133, "Chilpancingo": 955},
    "Tacubaya-9": {"Tacubaya-1": 300, "Tacubaya-7": 300, "Patriotismo": 1133},
}

linea_B = {
    "Ciudad Azteca": {"Plaza Aragón": 574},
    "Plaza Aragón": {"Olímpica": 709, "Ciudad Azteca": 574},
    "Olímpica": {"Ecatepec": 596, "Plaza Aragón": 709},
    "Ecatepec": {"Múzquiz": 1485, "Olímpica": 596},
    "Múzquiz": {"Río de los Remedios": 1155, "Ecatepec": 1485},
    "Río de los Remedios": {"Impulsora": 436, "Múzquiz": 1155},
    "Impulsora": {"Nezahualcóyotl": 1393, "Río de los Remedios": 436},
    "Nezahualcóyotl": {"Villa de Aragón": 1335, "Impulsora": 1393},
    "Villa de Aragón": {"Bosques de Aragón": 784, "Nezahualcóyotl": 1335},
    "Bosques de Aragón": {"Deportivo Oceanía": 1165, "Villa de Aragón": 784},
    "Deportivo Oceanía": {"Oceanía-B": 863, "Bosques de Aragón": 1165},
    "Oceanía-B": {"Romero Rubio": 809, "Oceanía-5": 300, "Deportivo Oceanía": 863},
    "Romero Rubio": {"Ricardo Flores Magón": 908, "Oceanía-B": 809},
    "Ricardo Flores Magón": {"San Lázaro-B": 907, "Romero Rubio": 908},
    "San Lázaro-B": {"Morelos-B": 1296, "San Lázaro-1": 300, "Ricardo Flores Magón": 907},
    "Morelos-B": {"Tepito": 498, "Morelos-4": 300, "San Lázaro-B": 1296},
    "Tepito": {"Lagunilla": 611, "Morelos-B": 498},
    "Lagunilla": {"Garibaldi-B": 474, "Tepito": 611},
    "Garibaldi-B": {"Guerrero-B": 757, "Garibaldi-8": 300, "Lagunilla": 474},
    "Guerrero-B": {"Buenavista": 521, "Guerrero-3": 300, "Garibaldi-B": 757},
    "Buenavista": {"Guerrero-B": 521},
}

linea_A = {
    "Pantitlán-A": {
        "Agrícola Oriental": 1409,
        "Pantitlán-1": 300,
        "Pantitlán-5": 300,
        "Pantitlán-9": 300,
    },
    "Agrícola Oriental": {"Canal de San Juan": 1093, "Pantitlán-A": 1409},
    "Canal de San Juan": {"Tepalcates": 1456, "Agrícola Oriental": 1093},
    "Tepalcates": {"Guelatao": 1161, "Canal de San Juan": 1456},
    "Guelatao": {"Peñón Viejo": 2206, "Tepalcates": 1161},
    "Peñón Viejo": {"Acatitla": 1379, "Guelatao": 2206},
    "Acatitla": {"Santa Marta": 1100, "Peñón Viejo": 1379},
    "Santa Marta": {"Los Reyes": 1783, "Acatitla": 1100},
    "Los Reyes": {"La Paz": 1956, "Santa Marta": 1783},
    "La Paz": {"Los Reyes": 1956},
}

linea_12 = {
    "Tláhuac": {"Tlaltenco": 1298},
    "Tlaltenco": {"Zapotitlán": 1115, "Tláhuac": 1298},
    "Zapotitlán": {"Nopalera": 1276, "Tlaltenco": 1115},
    "Nopalera": {"Olivos": 1360, "Zapotitlán": 1276},
    "Olivos": {"Tezonco": 490, "Nopalera": 1360},
    "Tezonco": {"Periférico Oriente": 1545, "Olivos": 490},
    "Periférico Oriente": {"Calle 11": 1111, "Tezonco": 1545},
    "Calle 11": {"Lomas Estrella": 906, "Periférico Oriente": 1111},
    "Lomas Estrella": {"San Andrés Tomatlán": 1060, "Calle 11": 906},
    "San Andrés Tomatlán": {"Culhuacán": 990, "Lomas Estrella": 1060},
    "Culhuacán": {"Atlalilco-12": 1671, "San Andrés Tomatlán": 990},
    "Atlalilco-12": {"Mexicaltzingo": 1922, "Atlalilco-8": 300, "Culhuacán": 1671},
    "Mexicaltzingo": {"Ermita-12": 1805, "Atlalilco-12": 1922},
    "Ermita-12": {"Eje Central": 895, "Ermita-2": 300, "Mexicaltzingo": 1805},
    "Eje Central": {"Parque de los Venados": 1280, "Ermita-12": 895},
    "Parque de los Venados": {"Zapata-12": 563, "Eje Central": 1280},
    "Zapata-12": {"Hospital 20 de Noviembre": 450, "Zapata-3": 300, "Parque de los Venados": 563},
    "Hospital 20 de Noviembre": {"Insurgentes Sur": 725, "Zapata-12": 450},
    "Insurgentes Sur": {"Mixcoac-12": 651, "Hospital 20 de Noviembre": 725},
    "Mixcoac-12": {"Mixcoac-7": 300, "Insurgentes Sur": 651},
}

metro_graph = {**linea_1, **linea_2, **linea_3, **linea_4, **linea_5, **linea_6, **linea_7, **linea_8, **linea_9,**linea_A, **linea_B, **linea_12}