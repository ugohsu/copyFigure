# -*- coding: utf-8 -*-

import os, subprocess, tempfile

def getExt(x):
    """ get ext of a figure (svg, png, jpg, ...) """
    return os.path.splitext(x)[1].lstrip('.')

def cf(path):
    """ call xclip """
    try:
        ext = getExt(path)

        ## judge
        if ext in ('svg', 'SVG'):
            trg = 'image/svg+xml'
        elif ext in ('png', 'PNG', 'jpg', 'jpeg', 'JPG', 'JPEG'):
            trg = 'image/png'
        elif ext in ('pdf', 'PDF'):
            trg = 'image/svg+xml'
            fp = tempfile.NamedTemporaryFile()
            subprocess.call(('pdftocairo', '-svg', path, 
                fp.name))
            path = fp.name

        ## call xclip
        subprocess.call(('xclip', '-selection', 'clipboard',
            '-t', trg, '-i', path))

    except:
        print('cf can take only "PNG", "SVG", "JPG", or "PDF" extensions')

def mathpdf(path):
    """convert a tex body file to pdf"""

    basename = os.path.basename(path)
    tmpdir = tempfile.TemporaryDirectory()
    tmptex = os.path.join(tmpdir.name, basename)

    ## read body
    with open(path, 'r', encoding = 'utf-8') as rf:
        body = rf.readlines()

    ## add preamble
    texfile = [
            '\\documentclass[varwidth, crop, uplatex]{standalone}\n',
            '\\usepackage{amsmath, amssymb, amsfonts}\n',
            '\\begin{document}\n',
            '$\\displaystyle\n'
            ]
    texfile.extend(body)
    texfile.extend([
            '$\n',
            '\\end{document}\n'
        ])

    ## write
    with open(tmptex, 'w', encoding = 'utf-8') as wf:
        wf.writelines(texfile)

    ## ptex2pdf
    subprocess.call(('ptex2pdf', '-u', '-l', tmptex))
