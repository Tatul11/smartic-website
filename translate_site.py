import os
import glob
from bs4 import BeautifulSoup, Comment
from deep_translator import GoogleTranslator
import re
import time

def should_translate(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta']:
        # We can translate title and meta later manually or specifically
        return False
    if isinstance(element, Comment):
        return False
    # Avoid translating single characters or just spaces
    text = element.strip()
    if not text:
        return False
    # Avoid translating code blocks or specific classes if needed
    return True

def translate_html(filepath, target_lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Update Asset Paths
    # CSS
    for link in soup.find_all('link', href=True):
        if not link['href'].startswith(('http', 'tel', 'mailto', '#')):
            link['href'] = '../' + link['href']
    # Images
    for img in soup.find_all('img', src=True):
        if not img['src'].startswith(('http', 'data:')):
            img['src'] = '../' + img['src']
    # Links
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href == '#':
            continue
        if not href.startswith(('http', 'tel', 'mailto', '#')):
            # Internal links stay the same (relative to en/ or ru/ folder)
            pass
            
    # Language Switcher
    filename = os.path.basename(filepath)
    # The current switcher is: <span style="color: #222;">HY</span> | <a href="#">EN</a> | <a href="#">RU</a>
    # We will replace it manually as a string after bs4 parsing to make it perfect, or find the div
    lang_div = None
    for div in soup.find_all('div', style=re.compile("font-size: 12px; font-weight: 600; color: #888;")):
        if 'HY' in div.text and 'EN' in div.text and 'RU' in div.text:
            lang_div = div
            break
            
    if lang_div:
        if target_lang == 'en':
            lang_div.clear()
            lang_div.append(BeautifulSoup(f'<a href="../{filename}">HY</a> | <span style="color: #222;">EN</span> | <a href="../ru/{filename}">RU</a>', 'html.parser'))
        elif target_lang == 'ru':
            lang_div.clear()
            lang_div.append(BeautifulSoup(f'<a href="../{filename}">HY</a> | <a href="../en/{filename}">EN</a> | <span style="color: #222;">RU</span>', 'html.parser'))

    # Translate text nodes
    translator = GoogleTranslator(source='hy', target=target_lang)
    texts_to_translate = []
    nodes = []

    for text_node in soup.find_all(string=True):
        if should_translate(text_node):
            text = text_node.strip()
            # If it's mostly english or symbols, skip it
            if not re.search('[Ա-Ֆա-ֆ]', text):
                continue
                
            texts_to_translate.append(text_node.string)
            nodes.append(text_node)

    print(f"[{target_lang}] Translating {len(nodes)} text nodes in {filename}...")
    
    # Translate in chunks to avoid API limits
    for i, node in enumerate(nodes):
        original = str(node)
        clean = original.strip()
        if clean:
            try:
                translated_clean = translator.translate(clean)
                # preserve surrounding whitespace
                new_str = original.replace(clean, translated_clean)
                node.replace_with(new_str)
                time.sleep(0.1) # Be nice to the API
            except Exception as e:
                print(f"Error translating '{clean}': {e}")
                
    # Also translate titles and placeholders
    for title in soup.find_all('title'):
        if title.string and re.search('[Ա-Ֆա-ֆ]', title.string):
            try:
                title.string = translator.translate(title.string)
            except: pass
            
    for input_tag in soup.find_all(['input', 'textarea'], placeholder=True):
        if re.search('[Ա-Ֆա-ֆ]', input_tag['placeholder']):
            try:
                input_tag['placeholder'] = translator.translate(input_tag['placeholder'])
            except: pass
            
    # Form submission button values if any
    for input_tag in soup.find_all('input', type='submit', value=True):
        if re.search('[Ա-Ֆա-ֆ]', input_tag['value']):
            try:
                input_tag['value'] = translator.translate(input_tag['value'])
            except: pass

    # Write the new file
    out_dir = target_lang
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, filename)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"Saved {out_path}")


def update_root_switchers():
    # Update the language switchers in the root (HY) files
    files = glob.glob('*.html')
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        filename = os.path.basename(filepath)
        
        lang_div = None
        for div in soup.find_all('div', style=re.compile("font-size: 12px; font-weight: 600; color: #888;")):
            if 'HY' in div.text and 'EN' in div.text and 'RU' in div.text:
                lang_div = div
                break
                
        if lang_div:
            lang_div.clear()
            lang_div.append(BeautifulSoup(f'<span style="color: #222;">HY</span> | <a href="en/{filename}">EN</a> | <a href="ru/{filename}">RU</a>', 'html.parser'))
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated switcher in root {filename}")


if __name__ == "__main__":
    html_files = [f for f in glob.glob('*.html') if f not in ['index-en.html', 'index-ru.html']]
    
    for file in html_files:
        translate_html(file, 'en')
        translate_html(file, 'ru')
        
    update_root_switchers()
    print("Translation complete!")
