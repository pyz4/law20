import argparse
import os

from . import parsefile

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", dest="output_dir"
        , help="Please specify the output directory for writing the parsed files")
        
    parser.add_argument("-v", nargs="?", const=True, default=False, dest="verbose"
        , help="verbose")
        
    parser.add_argument("file"
        , help="You must give the file path of the XML file to be parsed")
        
    args = parser.parse_args()   
    
    print(args.output_dir)
    
    parsefile(args.file, write_to_dir=args.output_dir, verbose=args.verbose)
    
    
    
