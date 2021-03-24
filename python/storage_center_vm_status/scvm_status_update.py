#!/usr/bin/env python3

import sys
import argparse
import json
import logging
import os

import subprocess
from subprocess import check_output
from subprocess import call
from ablestack import *

env=os.environ.copy()
env['LANG']="en_US.utf-8"
env['LANGUAGE']="en"

def parseArgs():
    parser = argparse.ArgumentParser(description='Storage Center VM action ',
                                     epilog='copyrightⓒ 2021 All rights reserved by ABLECLOUD™')
    
    parser.add_argument('action', choices=['start', 'stop', 'delete'], help="Storage Center VM action")
    
    # output 민감도 추가(v갯수에 따라 output및 log가 많아짐)
    parser.add_argument("-v", "--verbose", action='count', default=0, help="increase output verbosity")

    # flag 추가(샘플임, 테스트용으로 json이 아닌 plain text로 출력하는 플래그 역할)
    parser.add_argument("-H", "--Human", action='store_const', dest='H', const=True, help="Human readable")

    # Version 추가
    parser.add_argument("-V", "--Version", action='version', version="%(prog)s 1.0")
    
    return parser.parse_args()

#스토리지 VM 시작 
def startStroageVM():

    try:
        rc = call(['virsh start jsdev'], universal_newlines=True, shell=True, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  
        
        if rc == 0: # ok
            retVal = True
            retCode = 200
        elif rc == 1: # not ok
            retVal = False
            retCode = 500

        ret = createReturn(code=retCode, val=retVal, retname='Storage Center VM Start')

    except Exception as e:
        ret = createReturn(code=500, val='virsh start error', retname='Storage Center VM Start Error')
        #print ('EXCEPTION : ',e)
                
    return print(json.dumps(json.loads(ret), indent=4))


#스토리지 VM 정지
def stopStroageVM():  
        
    try:
        rc = call(['virsh shutdown jsdev'], universal_newlines=True, shell=True, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  
        
        if rc == 0: # ok
            retVal = True
            retCode = 200
        elif rc == 1: # not ok
            retVal = False
            retCode = 500
         
        
        ret = createReturn(code=retCode, val=retVal, retname='Storage Center VM Stop')

    except Exception as e:
        ret = createReturn(code=retCode, val='virsh shutdown error', retname='Storage Center VM Stop Error')
        #print ('EXCEPTION : ',e)
    
    return print(json.dumps(json.loads(ret), indent=4))
    
#스토리지 VM 삭제
def deleteStroageVM():   

    try:

        rc = call(['virsh destroy jsdev'], universal_newlines=True, shell=True, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  
        if rc == 0: # 
            rc = call(['virsh undefine jsdev'], universal_newlines=True, shell=True, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)          
            if rc == 0: # ok
                retVal = True
                retCode = 200
            elif rc == 1: # not ok
                retVal = False
                retCode = 500

        elif rc == 1: # not ok
            retVal = False
            retCode = 500

        
        ret = createReturn(code=retCode, val=retVal, retname='Storage Center VM Delete')

    except Exception as e:
        ret = createReturn(code=500, val='virsh destroy, undefine error', retname='Storage Center VM Delete Error')
        #print ('EXCEPTION : ',e)
    
    return print(json.dumps(json.loads(ret), indent=4))


if __name__ == '__main__':

    # parser 생성
    args = parseArgs()
    ##print(args);

    verbose = (5 - args.verbose) * 10

    # 로깅을 위한 logger 생성, 모든 인자에 default 인자가 있음.
    #logger = createLogger(verbosity=logging.CRITICAL, file_log_level=logging.ERROR, log_file='test.log')

    if args.action == 'start':        
        ret = startStroageVM();    
    
    elif args.action == 'stop':
        ret = stopStroageVM();    
    
    elif args.action == 'delete':
        ret = deleteStroageVM();    
        

    #print(ret)
    

