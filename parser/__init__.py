import pandas as pd
import numpy as np
import os
import collections

from lxml import etree

_NAMESPACE = "http://xml.house.gov/schemas/uslm/1.0"
_NS = {'ns': _NAMESPACE}


def parse(root, ns=_NS, write_to_dir=None):
    '''
    Recursive workhorse function that parses XML representations of U.S. statutes found
    at http://uscode.house.gov/download/download.shtml.
    
    * Arguments
    root (node)       : current node in the xml tree
    ns (dict)         : namespace for searching through `root` using xpath
    write_to_dir (str): specifies parent directory to write to. 
        If None, parse only returns the dictionary
    '''
    out = {}
    
    if write_to_dir:
        assert os.path.exists(write_to_dir)
    
    # check if there's an identifier
    identifier = root.attrib['identifier']
    keys = [key for key in identifier.split("/") if (key and key not in ['us', 'usc'])] # leave out ''
    
    if write_to_dir:
        output_dir = os.path.join(write_to_dir, *keys)
        os.makedirs(output_dir, exist_ok=True)

    # if the provision was repealed, skip
    if root.attrib.get("status") == "repealed":
        out = dict_merge(out, {"status": "repealed"})
        
        # do not write
        return {f"({keys[-1]})": out}
        
    children = root.getchildren()
    
    # if no children, then just return the id
    for node in children:
        # heading are the bolded text leading the substantive law
        # chapeau are the preambles
        if any([tag in node.tag for tag in  ['heading', 'chapeau']]):
            tag = stripns(node.tag)
            body = (node.text or '').strip()
            
            out.update({tag: body})
            
            if write_to_dir:
                with open(os.path.join(output_dir, tag), "w") as fo:
                    fo.write(body + '\n')
            
            
        # special treatment if it's content, which may have various formatting
        if any([tag in node.tag for tag in ['content', 'continuation']]):           
            tag = stripns(node.tag)
            body = '\n'.join(map(writexml, node.getchildren()))
            body = ((node.text or '') + '\n' + body).strip()
            
            out.update({ tag : body })
            
            if write_to_dir:
                with open(os.path.join(output_dir, tag), "w") as fo:
                    fo.write(body + '\n')
            
        if node.attrib.get("identifier"):
            out = dict_merge(out, parse(node, ns, write_to_dir))
    
    return {f"({keys[-1]})": out}
    
    
def parsefile(file, ns=_NS, write_to_dir=None, verbose=False):
    '''
    Wrapper function for `parse`. Pulls all the top level sections
    that need to be parsed.
    '''
    # parsing the file
    fpath = os.path.abspath(os.path.expanduser(file))
    parser = etree.XMLParser(remove_blank_text=True)
    root = etree.parse(fpath, parser).getroot()
    
    # get all the sections that have the @identifier value.
    # sections are the highest level in the hierarchy of provisions
    sections = root.findall(".//ns:section[@identifier]", ns)
    
    for s in sections:
        if verbose:
            print(f"parsing {stripns(s.attrib.get('identifier'))}".center(79, "."))
        parse(s, ns, write_to_dir)
    
def nesteddict(content, keys, outer_first=True):
    '''
    Convenience function for creating a nested dictionary
    
    * Arguments
    content (object)  : inner most value in the nested dictionary
    keys (iterable)   : keys of the nested dictionary, default is proceed through keys from inner outward
    outer_first (bool): if True, keys are nested from left to right with the 
        left most key as the outer-most in the dictionary
    '''
    if outer_first:
        keys = list(reversed(keys))
        
    return reduce(lambda x, y: {y : x}, keys[1:], {keys[0]: content})


def walk(root):
    '''
    Helper function for exploring the XML tree of `root`
    '''
    children = root.getchildren()
    if not children:
        return [root.tag]
    
    return [f"{root.tag}/{tag.split('}')[1]}" for child in children for tag in walk(child)]


def stripns(tag):
    '''
    Helper function for removing the namespace prefix in tags
    '''
    try:
        return tag.split("}")[1]
    except IndexError:
        return tag
        
def dict_merge(dct, merge_dct, add_keys=True, inplace=False):
    """ Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
    ``dct``.

    This version will return a copy of the dictionary and leave the original
    arguments untouched.

    The optional argument ``add_keys``, determines whether keys which are
    present in ``merge_dict`` but not ``dct`` should be included in the
    new dict.

    Args:
        dct (dict) onto which the merge is executed
        merge_dct (dict): dct merged into dct
        add_keys (bool): whether to add new keys

    Returns:
        dict: updated dict
    """
    if not inplace:
        dct = dct.copy()
        
    if not add_keys:
        merge_dct = {
            k: merge_dct[k]
            for k in set(dct).intersection(set(merge_dct))
        }

    for k, v in merge_dct.items():
        if (k in dct and isinstance(dct[k], dict)
                and isinstance(merge_dct[k], collections.Mapping)):
            dct[k] = dict_merge(dct[k], merge_dct[k], add_keys=add_keys)
        else:
            dct[k] = merge_dct[k]

    return dct

def writexml(root):
    return etree.tostring(root, pretty_print=True, encoding="unicode")
