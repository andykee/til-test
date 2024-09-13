import glob
import os
import re
import subprocess
import sys


EXCLUDE_DIRS = ['.github', '__pycache__']

TITLE_PATTERN = re.compile('#(.*)\n')

GIT_DATE_CMD = 'git ls-tree -r --name-only HEAD -z | TZ=UTC xargs -0n1 -I_ git --no-pager log -1 --date=iso-local --format="%ad _" -- _'

def build(inputdir, outputdir):

    subdirs = [f.path for f in os.scandir(inputdir) if f.is_dir()]
    content_dirs = [d for d in subdirs if d.split('/')[-1] not in EXCLUDE_DIRS]

    # clean out output dir
    outfiles = glob.glob(os.path.join(outputdir, '*'))
    for f in outfiles:
        os.remove(f)

    # get dates for all posts
    
    git_dump = subprocess.run(GIT_DATE_CMD)#, capture_output=True, text=True).stdout
    #git_dump
    

    for d in content_dirs:
        infiles = glob.glob(os.path.join(d, '*.md'))
        category = d.split('/')[-1]

        for infile in infiles:
            outfile = os.path.join(outputdir, infile.split('/')[-1])
            
            # get time from commit hash
            # git ls-tree -r --name-only HEAD -z | TZ=UTC xargs -0n1 -I_ git --no-pager log -1 --date=iso-local --format="%ad _" -- _
            date = '2024-09-12'

            with open(infile, 'r') as i:
                # a valid note must have a markdown H1 as its first line
                title = i.readline()
                if title[0:2] != '# ':
                    print('Invalid note! Skipping...')
                else:
                    title = title[2:].rstrip()

                    if os.path.isfile(outfile):
                        outfile = outfile.split('.')
                        outfile = outfile[0] + '-2' + outfile[1]

                    with open(outfile, 'w') as o:

                        o.write(f'Title: {title}\n')
                        o.write(f'Date: {date}\n')
                        o.write(f'Category: {category}\n')

                        for line in i:
                            o.write(line)


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
    


