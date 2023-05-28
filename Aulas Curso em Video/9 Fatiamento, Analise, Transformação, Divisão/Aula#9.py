frase = 'Algudão Doce'
print('Frase completa:', frase)
# O modelos de armazenamento abaixo é chamado Json.
# Foi feito, neste codigo, somente para organizar.
Fatiamento = {
    print(''),
    print('Tipos de Fatiamentos:'),
    print('----------------------'),
    # Fatiamento simples:
    print('Caracter 5 da frase:', frase[5]),

    # Fatiamento composto:
    print('Caracteres de 0 a 6', frase[0:7]),
    # o ultimo valor não entra na contagem

    # Fatiamento fracionado:
    print('fatiamento fracionado:', frase[0:12:2]),
    # A frase será colocada da memoria X até memoria Y
    # Pulando a quantidade de memoria C.
    # Veja que coloquei um número de memoria a mais na reprodução
    # esse é o pior jeito de se colocar até a ultima memoria.

    # Fatiamento com quantidade Omitida:
    print('Frase com quantidade Omitida 1:', frase[:7]),
    print('Frase com quantidade Omitida 2:', frase[8:]),
    # Omitindo o inicio ou o final desejado ele pegará o extremo da memoria
    # Ou seja, se omitir o inicio pegar a memoria 0
    # Se omitir o final pegará a ultima memoria.

    # Brincando com oq ja temos podemos fazer uma seleção mais complexa, como:
    print('Seleção complexa:', frase[0::2])
    # Aqui estamos iniciando na memoria 0 e omitindo a ultima memoria
    # e ainda estamos querendo que pule em 2 em 2 as memorias.
}

Analise = {
    print(''),
    print('Tipos de Analise:'),
    print('----------------------'),

    # Len serve para saber a quantidade de memoria na variavel.
    print('Quantidade de memoria:', len(frase)),

    # .count foi feito para mostra a quantidade de memorias com o mesmo codigo.
    print('Quantidade de vezes que aparece a letra "o"', frase.count('o')),

    # conseguese fazer fatiamentos com ".count" com esse modelo:
    frase.count('o', 0, 7),
    # a frase completa tem 2 'o' mas assim tiramos 1 'o' da contagem
    # limitando a contagem até a memoria 6

    # .find serve para achar a posição inicial de uma sequencia de codigos
    print('.find:', frase.find('gudão')),
    # Se a função retornar o valor -1 significa que não achou a sequencia.
    # Esse é uma função boleano que serve para indenficar frase na memoria.
    print('in frase:', 'Doce' in frase)
}
frase2 = '   Dunga    '
Transformação = {
    print(''),
    print('Tipos de Transformação:'),
    print('----------------------'),
    # replace substitui uma sequencia de codigos por outra
    print('replace:', frase.replace('Doce', 'Fino')),
    # Upper deixa todas as letras maiusculas.
    print('upper:', frase.upper()),
    # Lower deixa todas as letras minusculas.
    print('lower:', frase.lower()),
    # Capitalize deixa as letras iniciais maiusculas e demais minusculas
    print('Captalize:', frase.capitalize()),
    # Title vai identificar palavras atraves de espaços
    # e fazer Capitalize em todas individualmente.
    print('title:', frase.title()),
    # algumas memorias podem esta cheias de espaços vazios em suas estremidades
    # para resolver isso usamos .strip para tirar esses espaços.
    print("""A frase "{}" tem {} caracteres, mas utilizando .strip podemos tirar espaços indesejados e essa frase ficará com {} caracteres"""
          .format(frase2, len(frase2), len(frase2.strip()))),
    # .Strip tem suas variações: .rStrip e .lStrip que faças o mesmo processo
    # Mas somente de um lado referente, R right, L left
}
frase3 = 'Curso em Video Python'
Divisão = {
    # split faz com que a frase armazenada se transforme em uma lista
    print(frase3.split()),
    # join podemos juntar os elementos de uma lista
    # com uma String para um modificador entre caracteres
    print(' '.join(frase3))

}
