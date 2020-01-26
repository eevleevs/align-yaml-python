import re

def align_yaml(str, pad=0, aligned_colons=False):
    props = re.findall(r'^\s*[\S]+:', str, re.MULTILINE)
    longest = max([len(i) for i in props]) + pad
    return ''.join([i+'\n' for i in map(lambda str:
            re.sub(r'^(\s*.+?[^:#]): \s*(.*)' if aligned_colons else r'^(\s*.+?[^:#]: )\s*(.*)', lambda m:
                    m.group(1) + ''.ljust(longest-len(m.group(1))+(-1-pad if aligned_colons else 1)) + (':'.ljust(pad+1) if aligned_colons else '') + m.group(2),
                str, re.MULTILINE)
        , str.split('\n'))])
