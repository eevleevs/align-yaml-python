import re

def align(str, pad=0):
    props = re.findall(r'^\s*[\S]+:', str, re.MULTILINE)
    longest = max([len(i) for i in props]) + pad
    return ''.join([i+'\n' for i in map(lambda str:
            re.sub(r'^(\s*.+?[^:#]: )\s*(.*)', lambda m:
                    m.group(1) + ''.ljust(longest - len(m.group(1)) + 1) + m.group(2),
                str, re.MULTILINE)
        , str.split('\n'))])
