#!/usr/bin/env python
import pyarrow.parquet as pq

def row_to_article_string(row): 
    '''Convert a row that represents an SEP article to a string'''

    article_string = row['title'] + ''.join(row['preamble'])
    
    for section in row['main_text']: 
        article_string += '\n' + section['section_title'] + ''.join(section['main_content'])
        for subsection in section['subsections']:
            article_string += '\n' + subsection['subsection_title'] + ''.join(subsection['content'])

    return article_string

def main(): 
    '''Load the data and output each article as txt to directory'''

    table = pq.read_table("hf_data/hf_sep.parquet")

    for row in table.to_pylist():
        shorturl = row['shorturl']
        article_string = row_to_article_string(row)
        with open(f'hf_data/articles/{shorturl}.txt', 'w') as f: 
            f.write(article_string)
    
if __name__ == "__main__": 
    main()