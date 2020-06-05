import os
import sys
import re
import argparse
import pattern as ptrn
import Debuglogger as dbgl
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


class Sequence:
    def __init__(self):

        self.pat = ptrn.pattern
        self.banner()
        return


    def banner(self):
        bannr = (r"""   

              ___           ___           ___           ___           ___           ___ 
             /  /\         /  /\         /  /\         /  /\         /  /\         /  /\
            /  /::\       /  /::\       /  /::\       /  /:/        /  /::\       /  /:/
           /__/:/\:\     /  /:/\:\     /__/:/\:\     /  /:/        /  /:/\:\     /  /:/ 
          _\_ \:\ \:\   /  /::\ \:\    \  \:\ \:\   /  /:/        /  /::\ \:\   /  /:/  
         /__/\ \:\ \:\ /__/:/\:\ \:\    \  \:\ \:\ /__/:/     /\ /__/:/\:\ \:\ /__/:/   
         \  \:\ \:\_\/ \  \:\ \:\_\/     \  \:\/:/ \  \:\    /:/ \  \:\ \:\_\/ \  \:\   
          \  \:\_\:\    \  \:\ \:\        \__\::/   \  \:\  /:/   \  \:\ \:\    \  \:\  
           \  \:\/:/     \  \:\_\/        /  /:/     \  \:\/:/     \  \:\_\/     \  \:\ 
            \  \::/       \  \:\         /__/:/       \  \::/       \  \:\        \  \:\
             \__\/         \__\/         \__\/         \__\/         \__\/         \__\/

                                              by: tccontre
                                             --------------
     ------------------------------------------------------------------------------------------------------------
    
        """)
        #print(bannr)
        dbgl.logger.info(bannr)
        return

    def param_checker(self, input_scan):

        """
        description: insanity checks for input parameter

        parameters:
            input_scan: file path or folder path you want to scan
            

        """
        if input_scan != None and os.path.isfile(input_scan):
            c = self.file_scan(input_scan)
        elif input_scan != None and os.path.isdir(input_scan):
           self.dir_scan(input_scan)
        else:
            dbgl.logger.info("[-] Failed: Wrong Input!!")
        return


    def read_file(self, file_path):
        with open(file_path, 'r') as f:
            dbgl.logger.debug("*************************************************************************************************************************************\n")
            dbgl.logger.debug("[+] SCAN FILE: {0}".format(file_path))
            lines = f.readlines()
        return lines

    def dir_scan(self, input_scan):
        total_file_det = 0
        for dirs, subdirs, files in os.walk(input_scan):
            print(type(files))
            for file in  files:
                file_path = os.path.join(dirs, file)
                found_flag = self.file_scan(file_path)
                if found_flag:
                    print("detected: {}".format(file))
                    total_file_det+=1
                else:
                    dbgl.logger.info("[-] FILE         : {:80s} --> NOT DETECTED!!!!".format(file_path))
            dbgl.logger.info("[+] TOTAL FILES DETECTED: {0}/{1}".format(total_file_det,len(files)))
                    
        return
    
    def file_scan(self, file_path):
        lines = self.read_file(file_path)
        found_flag = self.scanner(lines, file_path)   
        return found_flag

    def scanner(self, lines, file_path):
        
        ptn_cnt = 0
        for detection_name, pattern_rule in self.pat.items():
            det_flag = False
            line_num = 1
            for line in lines:
                m = re.search(pattern_rule, line)
                if m:
                    dbgl.logger.debug("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    dbgl.logger.info("[+] FILE         : {:80s} --> DETECTED AS [{:30s}]".format(file_path, detection_name))
                    dbgl.logger.debug("[+] DETECTION   : {0}".format(detection_name))
                    dbgl.logger.debug("[+] LINENUM     : {0}".format(line_num))
                    dbgl.logger.debug("[+] CODELINE    : {0}".format(line))
                    dbgl.logger.debug("[+] STR_MATCHED : {0}".format(m.group()))
                    dbgl.logger.debug("[+] PATTERN     : {0}".format(pattern_rule))
                    det_flag = True
                    dbgl.logger.debug("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    break
                else:
                    line_num +=1
   
            if det_flag:
                ptn_cnt +=1         
            else:
                dbgl.logger.debug("[-] STATUS: PATTERN NOT FOUND -> {0}:: {1}".format(detection_name, pattern_rule))
        dbgl.logger.info("[+] TOTAL PATTERN FOUND: {0}\n".format(ptn_cnt))
        
        if ptn_cnt >0:
            return True
        else:
            return False
        
                                      
        

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    return
        
    

def main():
    # clear the screen
    clear_screen()

    # instantiate the class
    sq = Sequence()

    # commandline parameter
    parser = argparse.ArgumentParser(description="possible SQL Injection Finder in HTML, XML and etc...")
    parser.add_argument('-i', '--input_scan', help="the folder or file you want to scan", required=True)


    # assigned parameters to a variable
    
    args = vars(parser.parse_args())
    input_scan = args['input_scan']

    # sanity check for input parameters
    sq.param_checker(input_scan)

    return



if __name__ == "__main__":
    main()
