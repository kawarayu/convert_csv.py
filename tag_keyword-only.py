def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    
    if attrs:
        attr_str = ' '.join(f'{attr}="{value}"' for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    
    if content:
         return '\n'.join(f'<{name} {attr_str}>{c}</{name}>' for c in content)
    else:
        return f'<{name} {attr_str} />'

if __name__ == '__main__':
    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', 'world', cls='sidebar'))
    print(tag(content='testing', name='img'))
    my_tag = {'name': 'img', 'title': 'Sunset', 'src': 'sunset.jpg', 'cls': 'flamed'}
    print(tag(**my_tag))