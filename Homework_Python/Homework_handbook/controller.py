import view
import process
import log
import open_html as oh

def button_click():
    regim = view.inp_mod()
    if regim.lower() == 'импорт':
        sern = view.inp_import()
        res_search = process.search(sern)
        print(res_search)
        if isinstance(res_search, str):
            view.view_import_no()
        else:
            view.view_import(res_search)
    elif regim.lower() == 'экспорт':
        result = view.inp_export()
        print(oh.create(list(result)))
        process.export(result)
        log.log_data(regim, result)
        