import re

def align_yaml(str, pad=0, aligned_colons=False):
    props = re.findall(r'^\s*[\S]+:', str, re.MULTILINE)
    longest = max([len(i) for i in props]) + pad
    if aligned_colons:
        return ''.join([i+'\n' for i in map(lambda str:
                re.sub(r'^(\s*.+?[^:#]): \s*(.*)', lambda m:
                        m.group(1) + ''.ljust(longest-len(m.group(1))-1-pad) + ':'.ljust(pad+1) + m.group(2),
                    str, re.MULTILINE)
            , str.split('\n'))])
    else:
        return ''.join([i+'\n' for i in map(lambda str:
                re.sub(r'^(\s*.+?[^:#]: )\s*(.*)', lambda m:
                        m.group(1) + ''.ljust(longest-len(m.group(1))+1) + m.group(2),
                    str, re.MULTILINE)
            , str.split('\n'))])
