def server_write(num):
    try:
        
        f = open('/home/pi/www/index.html','w')
        
        if(num == 1):
            f.write('''
<!DOCTYPE html>

<html lang="ko">

    <head>

        <meta charset="utf-8" />

        <meta http-equiv="X-UA-Compatible" content="IE=edge" />

        <meta name="viewport" content="width=device-width, initial-scale=1" />

        <title>고고씽</title>

    </head>
    <body bgcolor="#CCFFE5">1
    </body>
</html>
'''
)
            f.close()
        elif (num == 0):
            f.write('''
<!DOCTYPE html>

<html lang="ko">
 
    <head>

        <meta charset="utf-8" />  
        
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />

        <meta name="viewport" content="width=device-width, initial-scale=1" />


        <title>고고씽</title>

    </head>
    <body bgcolor="#CCFFE5">0
    </body>
</html>''')
            f.close()
                
    except KeyboardInterrupt:
        print("\nSTOP")

    # resource return ---------------
    
    return(0)
'''
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
'''
