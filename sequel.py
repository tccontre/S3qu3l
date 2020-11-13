__author__ = "tccontre"
import os
import re
import sys
import argparse
import hashlib
import pattern


class Sequel:
    def __init__(self):

        self.pat = pattern.pattern
        self.banner()
        return

    def input_checker(self, target_folder, target_file):
        self.target_file = target_file
        self.target_folder = target_folder
        if self.target_file:
            self.pattern_scan(self.target_file)
        else:
            self.iterate_files()
        return

    def iterate_files(self):
        for dirs, subdirs, files in os.walk(self.target_folder):
            for file in files:
                file_path = os.path.join(dirs, file)
                self.pattern_scan(file_path)
        return

    def banner(self):
        self.scan_log("----------------------------------------------------------------------------\n")
        self.scan_log("                      LOCAL XML SQL-INJECTION TESTER                        \n")
        self.scan_log("                                   by:                                      \n")
        self.scan_log("                                tccontre                              \n")
        self.scan_log("----------------------------------------------------------------------------\n")
        return

    def scan_log(self, w_string):
        with open("scan.log", 'a') as w:
            w.write(w_string)
        print(w_string)
        return

    def scanner(self, list_lines, file_path):

        for key, val in self.pat.items():
            line_num = 1
            self.scan_log("[+] looking for rule: {0}\n".format(key))
            for line in list_lines:
                pat = self.pat[key]
                m = re.search(pat, line)
                if m:
                    self.scan_log("-------------------------------------------------------\n")
                    self.scan_log("[+] Found possible SQL command!!\n")
                    self.scan_log("[+] file path     : {0}\n".format(file_path))
                    self.scan_log("[+] detection     : {0}\n"
                                  "[+] line number   : {1}\n"
                                  "[+] line of code  : {2}\n"
                                  "[+] string matched: {3}\n"
                                  "[+] pattern       : {4}\n".format(key, \
                                                                    line_num, \
                                                                    line, m.group(), val))
                    self.scan_log("-------------------------------------------------------\n\n")

                else:
                    print("[+] PATTERN NOT FOUND - line of code number :{0}\n".format(line_num))
                line_num += 1
        return

    def pattern_scan(self, file_path):
        with open(file_path, 'r') as f:
            self.scan_log("\n\n[+] file path: {0}\n\n".format(file_path))
            self.scan_log("-------------------------------------------------------\n")
            list_lines = f.readlines()
        self.scanner(list_lines, file_path)
        return


def main():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    sq = Sequel()
    parser = argparse.ArgumentParser(description="possible SQL Injection Finder in HTML, XML and etc...")
    parser.add_argument('-d', '--target_folder', help="the folder files you want to scan", required=True)
    parser.add_argument('-f', '--target_file', help="the file you want to scan", required=False)

    args = vars(parser.parse_args())
    target_file = args['target_file']
    target_folder = args['target_folder']

    sq.input_checker(target_folder, target_file)

    return


if __name__ == "__main__":
    main()
