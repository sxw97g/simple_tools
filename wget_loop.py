import subprocess
import argparse
 
 
parser = argparse.ArgumentParser()
parser.add_argument('file_a', type=str, help='Input apt_install_list  file' )
args = parser.parse_args()
 
no_found_list = []
while True:
    with open(args.file_a, 'r') as f1:
       lines_a = f1.readlines()
 
    for line1 in lines_a:
        if line1 == '\n':
            continue
        line1 = line1.replace('\n','')
        cmd = 'wget --no-check-certificate https://'+ line1
        print "command is: {}".format(cmd)
        try:
            output = subprocess.check_output(cmd, shell=True).strip('\n')
            print 'commend sent {}'.format(line1)
        except Exception as e:
            print 'failed:  {}'.format(e)
 
