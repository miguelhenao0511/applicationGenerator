from django.http import HttpResponse
import xml.dom.minidom
import os


class Token:
    def __init__(self, id):
        self.id = id


class Task_Token(Token):
    def __init__(self, id, name, DOR):
        super().__init__(id)
        self.name = name
        self.DOR = DOR


class DOR_Token(Token):
    def __init__(self, id, name):
        super().__init__(id)
        self.campos = list(name)


class startEvent_Token(Token):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name


class sequenceFlow_Token(Token):
    def __init__(self, id, entrada, salida, name=None):
        super().__init__(id)
        self.entrada = entrada
        self.salida = salida
        self.name = name


class endEvent_Token(Token):
    def __init__(self, id, name=None):
        super().__init__(id)
        self.name = name


class gateway_Token(Token):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name


class atributo:
    def __init__(self, nombre, tipo, operation=None):
        self.nombre = nombre
        self.tipo = tipo
        self.operation = operation


class Dato:
    def __init__(self, nombre, atributos):
        self.nombre = nombre
        self.atributos = atributos


def generate_json_structure(file):
    domtree = xml.dom.minidom.parse(file)
    definitions = domtree.documentElement
    colab = definitions.getElementsByTagName('bpmn:collaboration')
    participantes = []
    processes = definitions.getElementsByTagName('bpmn:process')
    # Lista que contiene los elementos de cada proceso en sublistas
    EleNodes = []

    # hace listas de objetos de cada tipo de token
    tasks = []
    starts = []
    DORs = []
    flows = []
    ends = []
    gateways = []
    json = []

    Datos = []

    def getElement(nodeList):
        rc = []
        for node in nodeList:
            if node.nodeType == node.ELEMENT_NODE:
                rc.append(node)
        return rc

    def conectar_salida(lista):
        for el in lista:
            el.salida = []
            for f in flows:
                if el.id == f.entrada:
                    el.salida.append(f)
                    f.entrada = el
            if not el.salida:
                el.salida = None

    def conectar_entrada(lista):
        for f in flows:
            for el in lista:
                if f.salida == el.id:
                    f.salida = el
                    el.entrada = f

    print("generate json structure")
    for e in colab:
        p = e.childNodes
        participantes.append(getElement(p))

    # Definir los procesos dentro del XML
    for process in processes:
        print("---Process---")
        print(process)
        print(process.childNodes)
        if process.hasAttribute('id'):
            print("ID: {}".format(process.getAttribute('id')))

    for process in processes:
        nodes = process.childNodes
        EleNodes.append(getElement(nodes))

    for node in EleNodes:
        for element in node:
            if 'task' in element.tagName:
                if element.childNodes:
                    hijos = getElement(element.childNodes)
                    for hijo in hijos:
                        if 'dataOutputAssociation' in hijo.tagName:
                            nodes = getElement(hijo.childNodes)
                            for node in nodes:
                                if 'targetRef' in node.tagName:
                                    DOR = node.firstChild.nodeValue
                                    tasks.append(
                                        Task_Token(element.getAttribute('id'), element.getAttribute('name'), DOR))
                else:
                    tasks.append(Task_Token(element.getAttribute('id'), element.getAttribute('name')))
            elif 'startEvent' in element.tagName:
                starts.append(startEvent_Token(element.getAttribute('id'), element.getAttribute('name')))
            elif 'dataObjectReference' in element.tagName:
                DORs.append(DOR_Token(element.getAttribute('id'), element.getAttribute('name').split('\n')))
            elif 'sequenceFlow' in element.tagName:
                entrada = element.getAttribute('sourceRef')
                salida = element.getAttribute('targetRef')
                if element.hasAttribute('name'):
                    flows.append(
                        sequenceFlow_Token(element.getAttribute('id'), entrada, salida, element.getAttribute('name')))
                else:
                    flows.append(sequenceFlow_Token(element.getAttribute('id'), entrada, salida))
            elif 'endEvent' in element.tagName:
                if element.hasAttribute('name'):
                    ends.append(endEvent_Token(element.getAttribute('id'), element.getAttribute('name')))
                else:
                    ends.append(endEvent_Token(element.getAttribute('id')))
            elif 'exclusiveGateway' in element.tagName:
                gateways.append(gateway_Token(element.getAttribute('id'), element.getAttribute('name')))

    for dor in DORs:
        print(dor.campos)

    # Función para obtener todos los elementos/Nodos hijo de los procesos

    conectar_salida(tasks)
    conectar_salida(starts)
    conectar_salida(gateways)

    conectar_entrada(tasks)
    conectar_entrada(DORs)
    conectar_entrada(ends)
    conectar_entrada(gateways)

    for task in tasks:
        if task.DOR:
            for DOR in DORs:
                if DOR.id == task.DOR:
                    task.DOR = DOR
                    atributos = []
                    for campo in DOR.campos:
                        attrs = campo.split(":")
                        if len(attrs) > 2:
                            atributos.append(atributo(attrs[1], attrs[0], attrs[2]))
                        else:
                            atributos.append(atributo(attrs[1], attrs[0]))
                    Datos.append(Dato(task.name, atributos))

    for dato in Datos:
        dic = {}
        # print("nombre", dato.nombre)
        att = []
        for attr in dato.atributos:
            dic1 = {}
            # print(" atributo: nombre:", attr.nombre, "tipo: ", attr.tipo)
            dic1.setdefault('name', attr.nombre)
            dic1.setdefault('attribute_type', attr.tipo)
            if attr.operation is not None:
                dic1.setdefault('operation', attr.operation)
            att.append(dic1)
        dic.setdefault('name', dato.nombre)
        dic.setdefault('attributes', att)
        json.append(dic)

    return json
