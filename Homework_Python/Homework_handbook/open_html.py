

def create(data):
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Name: {}  </p>\n'\
        .format(style, data[2])
    html += '    <p {}>Surname: {}  </p>\n'\
        .format(style, data[3])
    html += '    <p {}>phone: {}  </p>\n'\
        .format(style, data[4])
    html += '  </body>\n</html>'
    
    with open('index.html', 'w') as page:
        page.write(html)

    return html