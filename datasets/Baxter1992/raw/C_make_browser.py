from lingpy import *

wl = Wordlist('baxter-out.tsv', col='shijing', row='stanza')

# first make a link between a character in a section and its occurrence as
# rhyme word
chars = []
for k in wl:

    char = wl[k,'rhyme']
    poem = wl[k,'number']
    stanza = wl[k,'stanza']
    section = wl[k,'line_number']
    ocbs = wl[k,'ocbs']
    pwy = wl[k,'pwy']
    mch = wl[k,'mchascii']
    pin = wl[k,'pinyin']
    gls = wl[k,'och_gloss']
    gsr = wl[k,'gsr']
    

    chars += [[k, char, pin, gls, mch, ocbs, pwy, gsr, poem, stanza, section]]

# now assemble poems under their id
poems = {}
for k in wl:
    
    poem = int(wl[k,'number'])
    name = wl[k,'title']
    block = wl[k,'block'] + '·'+wl[k,'chapter']
    rhyme = wl[k,'rhyme']
    arhyme = wl[k,'wangid']
    section = wl[k,'line']
    stanza = wl[k,'stanza']
    ocbs = wl[k,'ocbs']
    pwy = wl[k,'pwy']
    mch = wl[k,'mch']
    yun = wl[k,'ocbsyun']
    char = wl[k,'character']
    
    try:
        poems[poem]['sections'] += [[stanza, section, rhyme, arhyme, ocbs, pwy,
            mch, yun, char]]
    except KeyError:
        poems[poem] = { "name" : name, "block" : block }
        poems[poem]['sections'] = [[stanza, section, rhyme, arhyme, ocbs, pwy,
            mch, yun, char]]

import json
import os
import shutil

if not os.path.isdir('browser'):
    os.mkdir('browser')
shutil.copyfile('T_main.js', 'browser/main.js')
shutil.copyfile('T_index.html', 'browser/index.html')
shutil.copyfile('T_style.css', 'browser/style.css')
with open('browser/shijing.js', 'w') as f:

    f.write('var POEMS = '+json.dumps(poems,indent=2)+';\n')
    f.write('var CHARS = '+json.dumps(chars,indent=2)+';\n')

