#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:55:10 2024

@author: rodolfodom
"""

linea_1 = {
    "Pantitlán-1": {"Zaragoza": 1320, "Pantitlán-9": 469, "Pantitlán-A": 602, "Pantitlán-5": 300},
    "Zaragoza": {"Gómez Farías": 762},
    "Gómez Farías": {"Boulevard Puerto Aéreo": 595},
    "Boulevard Puerto Aéreo": {"Balbuena": 595},
    "Balbuena": {"Moctezuma": 703},
    "Moctezuma": {"San Lázaro-1": 478},
    "San Lázaro-1": {"Candelaria-1": 866, "San Lázaro-B": 300},
    "Candelaria-1": {"Merced": 698, "Candelaria-4": 300},
    "Merced": {"Pino Suárez-1": 745},
    "Pino Suárez-1": {"Isabel la Católica": 382, "Pino Suárez-2": 300},
    "Isabel la Católica": {"Salto del Agua-1": 445},
    "Salto del Agua-1": {"Balderas-1": 458, "Salto del Agua-8":300},
    "Balderas-1": {"Cuauhtémoc": 409, "Balderas-3":300},
    "Cuauhtémoc": {"Insurgentes": 793},
    "Insurgentes": {"Sevilla": 645},
    "Sevilla": {"Chapultepec": 501},
    "Chapultepec": {"Juanacatlán": 973},
    "Juanacatlán": {"Tacubaya-1": 1158},
    "Tacubaya-1": {"Observatorio": 1262, "Tacubaya-9": 300, "Tacubaya-7": 300},
    "Observatorio": {}
    }


linea_2 = {
    "Cuatro Caminos": {"Panteones": 1639},
    "Panteones": {"Tacuba-2": 1416},
    "Tacuba-2": {"Cuitláhuac": 637, "Tacuba-7": 300},
    "Cuitláhuac": {"Popotla": 620},
    "Popotla": {"Colegio Militar": 462},
    "Colegio Militar": {"Normal": 516},
    "Normal": {"San Cosme": 657},
    "San Cosme": {"Revolución": 537},
    "Revolución": {"Hidalgo-2": 587},
    "Hidalgo-2": {"Bellas Artes-2": 447, "Hidalgo-3": 300},
    "Bellas Artes-2": {"Allende": 387, "Bellas Artes-8": 300},
    "Allende": {"Zócalo/Tenochtitlan": 602},
    "Zócalo/Tenochtitlan": {"Pino Suárez-2": 745},
    "Pino Suárez-2": {"San Antonio Abad": 817, "Pino Suárez-1": 300},
    "San Antonio Abad": {"Chabacano-2": 642},
    "Chabacano-2": {"Viaducto": 774, "Chabacano-8": 300, "Chabacano-9": 300},
    "Viaducto": {"Xola": 490},
    "Xola": {"Villa de Cortés": 698},
    "Villa de Cortés": {"Nativitas": 750},
    "Nativitas": {"Portales": 924},
    "Portales": {"Ermita-2": 748},
    "Ermita-2": {"General Anaya": 838, "Ermita-12": 300},
    "General Anaya": {"Tasqueña": 1330},
    "Tasqueña": {}
}

linea_3 = {
    "Indios Verdes": {"Deportivo 18 de Marzo-3": 1166},
    "Deportivo 18 de Marzo-3": {"Potrero": 966, "Deportivo 18 de Marzo-6": 300},
    "Potrero": {"La Raza-3": 1106},
    "La Raza-3": {"Tlatelolco": 1445, "La Raza-5": 300},
    "Tlatelolco": {"Guerrero-3": 1042},
    "Guerrero-3": {"Hidalgo-3": 702, "Guerrero-B": 300},
    "Hidalgo-3": {"Juárez": 251, "Hidalgo-2": 300},
    "Juárez": {"Balderas-3": 659},
    "Balderas-3": {"Niños Héroes": 665, "Balderas-1": 300},
    "Niños Héroes": {"Hospital General": 559},
    "Hospital General": {"Centro Médico-3": 653},
    "Centro Médico-3": {"Etiopía/Plaza de la Transparencia": 1119, "Centro Médico-9": 300},
    "Etiopía/Plaza de la Transparencia": {"Eugenia": 950},
    "Eugenia": {"División del Norte": 715},
    "División del Norte": {"Zapata-3": 794},
    "Zapata-3": {"Coyoacán": 1153, "Zapata-12": 300},
    "Coyoacán": {"Viveros/Derechos Humanos": 908},
    "Viveros/Derechos Humanos": {"Miguel Ángel de Quevedo": 824},
    "Miguel Ángel de Quevedo": {"Copilco": 1295},
    "Copilco": {"Universidad": 1306}
    "Universidad": {}
}

linea_4 = {
    "Santa Anita-4": {"Jamaica-4": 758, "Santa Anita-8": 300},
    "Jamaica-4": {"Fray Servando": 1033, "Jamaica-9": 300},
    "Fray Servando": {"Candelaria-4": 633},
    "Candelaria-4": {"Morelos-4": 1062, "Candelaria-1": 300},
    "Morelos-4": {"Canal del Norte": 910, "Morelos-B": 300},
    "Canal del Norte": {"Consulado-4": 884},
    "Consulado-4": {"Bondojito": 645, "Consulado-5": 300},
    "Bondojito": {"Talisman": 959},
    "Talisman": {"Martín Carrera-4": 1129, "Martín Carrera-6": 300},
    "Martín Carrera-4": {}
}

linea_5 = {
    "Politécnico": {"Instituto del Petróleo-5": 1188},
    "Instituto del Petróleo-5": {"Autobuses del Norte": 1067, "Instituto del Petróleo-6": 300},
    "Autobuses del Norte": {"La Raza-5": 975},
    "La Raza-5": {"Misterios": 892, "La Raza-3": 300},
    "Misterios": {"Valle Gómez": 969},
    "Valle Gómez": {"Consulado-5": 679},
    "Consulado-5": {"Eduardo Molina": 815, "Consulado-4": 300},
    "Eduardo Molina": {"Aragón": 860},
    "Aragón": {"Oceanía-5": 1219},
    "Oceanía-5": {"Terminal Aérea": 1174, "Oceanía-B": 300},
    "Terminal Aérea": {"Hangares": 1153},
    "Hangares": {"Pantitlán-5": 1644},
    "Pantitlán-5": {"Pantitlán-1": 300, "Pantitlán-9": 300, "Pantitlán-A": 300}
}

linea_6 = {
    "El Rosario-6": {"Tezozómoc": 1257, "El Rosario-7": 300},
    "Tezozómoc": {"Azcapotzalco": 973},
    "Azcapotzalco": {"Ferrería": 1173},
    "Ferrería": {"Norte 45": 1072},
    "Norte 45": {"Vallejo": 660},
    "Vallejo": {"Instituto del Petróleo-6": 755},
    "Instituto del Petróleo-6": {"Lindavista": 1258, "Instituto del Petróleo-5": 300},
    "Lindavista": {"Deportivo 18 de Marzo-6": 1075},
    "Deportivo 18 de Marzo-6": {"La Villa/Basílica": 570, "Deportivo 18 de Marzo-3": 300},
    "La Villa/Basílica": {"Martín Carrera": 1141},
    "Martín Carrera-6": {"Martín Carrera-4": 300}
}

linea_7 = {
    "El Rosario-7": {"Aquiles Serdán": 1615, "El Rosario-6": 300},
    "Aquiles Serdán": {"Camarones": 1402},
    "Camarones": {"Refinería": 952},
    "Refinería": {"Tacuba-7": 1295},
    "Tacuba-7": {"San Joaquín": 1433, "Tacuba-2": 300},
    "San Joaquín": {"Polanco": 1163},
    "Polanco": {"Auditorio": 812},
    "Auditorio": {"Constituyentes": 1430},
    "Constituyentes": {"Tacubaya-7": 1005},
    "Tacubaya-7": {"San Pedro de los Pinos": 1084, "Tacubaya-1": 300, "Tacubaya-9": 300},
    "San Pedro de los Pinos": {"San Antonio": 606},
    "San Antonio": {"Mixcoac": 788},
    "Mixcoac-7": {"Barranca del Muerto": 1476, "Mixcoac-12": 300}
    "Barranca del Muerto": {}
}

linea_8 = {
    "Garibaldi-8": {"Bellas Artes-8": 634, "Garibaldi-B": 300},
    "Bellas Artes-8": {"San Juan de Letrán": 456, "Bellas Artes-2": 300},
    "San Juan de Letrán": {"Salto del Agua-8": 292},
    "Salto del Agua-8": {"Doctores": 564, "Salto del Agua-1": 300},
    "Doctores": {"Obrera": 761},
    "Obrera": {"Chabacano-8": 1143},
    "Chabacano-8": {"La Viga": 843, "Chabacano-2": 300, "Chabacano-9": 300},
    "La Viga": {"Santa Anita-8": 633},
    "Santa Anita-8": {"Coyuya": 968, "Santa Anita-4": 300},
    "Coyuya": {"Iztacalco": 993},
    "Iztacalco": {"Apatlaco": 910},
    "Apatlaco": {"Aculco": 534},
    "Aculco": {"Escuadrón 201": 789},
    "Escuadrón 201": {"Atlalilco-8": 1738},
    "Atlalilco-8": {"Iztapalapa": 732, "Atlalilco-12": 300},
    "Iztapalapa": {"Cerro de la Estrella": 717},
    "Cerro de la Estrella": {"UAM I": 1135},
    "UAM I": {"Constitución de 1917": 1137}
    "Constitución de 1917": {}
}

linea_9 = {
    "Pantitlán-9": {"Puebla": 1380, "Pantitlán-1": 300, "Pantitlán-5": 300, "Pantitlán-A": 300},
    "Puebla": {"Ciudad Deportiva": 800},
    "Ciudad Deportiva": {"Velódromo": 1110},
    "Velódromo": {"Mixiuhca": 821},
    "Mixiuhca": {"Jamaica-9": 942},
    "Jamaica-9": {"Chabacano-9": 1031, "Jamaica-4": 300},
    "Chabacano-9": {"Lázaro Cárdenas": 1000, "Chabacano-8": 300, "Chabacano-2": 300},
    "Lázaro Cárdenas": {"Centro Médico-9": 1059},
    "Centro Médico-9": {"Chilpancingo": 1152, "Centro Médico-3": 300},
    "Chilpancingo": {"Patriotismo": 955},
    "Patriotismo": {"Tacubaya-9": 1133}
    "Tacubaya-9": {"Tacubaya-1": 300, "Tacubaya-7": 300}
}



linea_B = {
    "Ciudad Azteca": {"Plaza Aragón": 574},
    "Plaza Aragón": {"Olímpica": 709},
    "Olímpica": {"Ecatepec": 596},
    "Ecatepec": {"Múzquiz": 1485},
    "Múzquiz": {"Río de los Remedios": 1155},
    "Río de los Remedios": {"Impulsora": 436},
    "Impulsora": {"Nezahualcóyotl": 1393},
    "Nezahualcóyotl": {"Villa de Aragón": 1335},
    "Villa de Aragón": {"Bosques de Aragón": 784},
    "Bosques de Aragón": {"Deportivo Oceanía": 1165},
    "Deportivo Oceanía": {"Oceanía-B": 863},
    "Oceanía-B": {"Romero Rubio": 809, "Oceanía-5": 300},
    "Romero Rubio": {"Ricardo Flores Magón": 908},
    "Ricardo Flores Magón": {"San Lázaro-B": 907},
    "San Lázaro-B": {"Morelos-B": 1296, "San Lázaro-1": 300},
    "Morelos-B": {"Tepito": 498, "Morelos-4": 300},
    "Tepito": {"Lagunilla": 611},
    "Lagunilla": {"Garibaldi-B": 474},
    "Garibaldi-B": {"Guerrero-B": 757, "Garibaldi-8": 300},
    "Guerrero-B": {"Buenavista": 521, "Guerrero-3": 300},
    "Buenavista": {}
}

linea_A = {
    "Pantitlán-A": {"Agrícola Oriental": 1409, "Pantitlán-1": 300, "Pantitlán-5": 300, "Pantitlán-9": 300},
    "Agrícola Oriental": {"Canal de San Juan": 1093},
    "Canal de San Juan": {"Tepalcates": 1456},
    "Tepalcates": {"Guelatao": 1161},
    "Guelatao": {"Peñón Viejo": 2206},
    "Peñón Viejo": {"Acatitla": 1379},
    "Acatitla": {"Santa Marta": 1100},
    "Santa Marta": {"Los Reyes": 1783},
    "Los Reyes": {"La Paz": 1956}
}

linea_12 = {
    "Tláhuac": {"Tlaltenco": 1298},
    "Tlaltenco": {"Zapotitlán": 1115},
    "Zapotitlán": {"Nopalera": 1276},
    "Nopalera": {"Olivos": 1360},
    "Olivos": {"Tezonco": 490},
    "Tezonco": {"Periférico Oriente": 1545},
    "Periférico Oriente": {"Calle 11": 1111},
    "Calle 11": {"Lomas Estrella": 906},
    "Lomas Estrella": {"San Andrés Tomatlán": 1060},
    "San Andrés Tomatlán": {"Culhuacán": 990},
    "Culhuacán": {"Atlalilco-12": 1671},
    "Atlalilco-12": {"Mexicaltzingo": 1922, "Atlalilco-8": 300},
    "Mexicaltzingo": {"Ermita-12": 1805},
    "Ermita-12": {"Eje Central": 895, "Ermita-2": 300},
    "Eje Central": {"Parque de los Venados": 1280},
    "Parque de los Venados": {"Zapata-12": 563},
    "Zapata-12": {"Hospital 20 de Noviembre": 450, "Zapata-3": 300},
    "Hospital 20 de Noviembre": {"Insurgentes Sur": 725},
    "Insurgentes Sur": {"Mixcoac-12": 651},
    "Mixcoac-12": {"Mixcoac-7": 300}
}

















