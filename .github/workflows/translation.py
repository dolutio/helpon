from json import load



translate_use_widgets_list = set()

def translate(en, fr, ru, hy, widget_id=None):
    with open('language.json') as json_data:
        lang = load(json_data)['language']
    if widget_id is not None:
        translate_use_widgets_list.add(widget_id)

    word_base = {}
    
    word_base = {'en': en, 'fr': fr, 'ru': ru, 'hy': hy}

    return word_base[lang]