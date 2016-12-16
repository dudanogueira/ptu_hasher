# -*- coding: utf-8 -*-
#!/usr/bin/env python
import hashlib
import os, sys, codecs

pasta_alvo = None

print("Checando plataforma...")
if hashlib.md5(str("Unimed").encode('utf-8')).hexdigest() == str('2dad3b15a3abcb29f82e1d5547e8cd1a'):
    print("OK! Biblioteca Hash Funciona!")

try:
    pasta_alvo = sys.argv[1]
except:
    pasta_alvo = os.path.join(os.getcwd(), 'PTUs')

print("Checando Pasta....")

if os.path.isdir(pasta_alvo):
    print("OK! Pasta alvo definida e válida: %s" % pasta_alvo)
else:
    print("ERRO! Pasta alvo inválida: %s" % pasta_alvo)

# exclui arquivos ocultos e pythonicos
arquivos = [f for f in os.listdir(pasta_alvo) if not f.startswith('.') and not f.endswith('.py')]


for arquivo in arquivos:
    caminho = os.path.join(pasta_alvo, arquivo)
    with codecs.open(caminho, encoding='utf-8') as f:
        print ('----------------%s---------------' % caminho)
        # remove quebras de linha
        linhas_originais = f.readlines()
        linhas = [l.replace('\r', '').replace('\n', '') for l in linhas_originais]
        # hash encontrado no arquivo
        md5_arquivo = linhas[-1][-32:]
        # conteudo sem ultima linhas
        conteudo = u"".join(linhas[:-1]).encode('utf-8')
        md5_calculado = hashlib.md5(conteudo).hexdigest()
        if md5_calculado == md5_arquivo:
            print("[%s] HASH OK!" % arquivo)
        else:
            print ("[%s] !!! ERRO DE HASH !!! ENCONTRADO: %s CALCULADO: %s " \
            % (arquivo, md5_arquivo, md5_calculado))
            print("CONSERTANDO...")
            ultima_linha = "%s%s" % (linhas[-1][:11], md5_calculado)
            linhas_originais[-1] = ultima_linha
            open(os.path.join(pasta_alvo, arquivo), 'w').writelines(linhas_originais)