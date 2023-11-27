import math

go=("yes")

while go==("yes"):
    #Acquires values
    rgun=input("What is the name of the weapon: ")
    rdmg=input("What is the damage per shot of the weapon: ")
    rfire=input("What is the fire rate of the weapon: ")
    racc=input("What is the accuracy of the weapon: ")
    rrecoil=input("What is the recoil of the weapon: ")
    rmag=input("What is the magazine size of the weapon: ")
    rmob=input("What is the mobility of the weapon: ")
    rprice=input("What is the price of the weapon: ")
    
    #Converts to desired class and some basic calcs
    check=0
    checkcheck=0
    gun=str(rgun)
    dmg=float(rdmg)
    hdmg=dmg*2
    if dmg>=100:
        dmg=100
    if hdmg>=100:
        hdmg=100
    bkills=math.ceil(100/dmg)
    hkills=math.ceil(100/hdmg)
    while check<100:
        check=check+hdmg
        checkcheck=checkcheck+1
        while check<100:
                check=check+dmg
                checkcheck=checkcheck+1            
    fire=float(rfire)
    firer=1/fire
    dps=dmg*fire
    acc=float(racc)
    recoil=float(rrecoil)
    trecoil=recoil
    if recoil > 15:
        trecoil=15
    mag=float(rmag)
    mob=float(rmag)
    price=float(rprice)


    #Calculates everything
    tbkill=(bkills-1)*firer
    tbkillm=bkills*firer
    thkill=(hkills-1)*firer
    thkillm=hkills*firer
    thbkill=checkcheck*firer

    #Calculates predicted values
    trueacc=(acc+100-trecoil+((-bkills-hkills-checkcheck)*10))-(firer*2)*2
    truetkill=(tbkill+tbkillm+thkill+thkillm+thbkill)/5
    trueweapon=((trueacc*1.4)+(dps/30)+(mag/5)+(mob/10)-(truetkill*1500)+800)
    value=(trueweapon+500-((5000+price)/12))

    print(f"The {gun}'s damage per shot is {dmg}")
    print(f"The {gun}'s headshot damage is {hdmg}")
    print(f"The {gun}'s fire rate is {rfire}")
    print(f"The {gun} fires once per {firer}s")
    print(f"The {gun}'s accuracy is {acc}")
    print(f"The {gun}'s recoil is {recoil}")
    print(f"The {gun}'s magazine size is {mag}")
    print(f"The {gun}'s price is ${price}")
    print(f"The {gun}'s DPS is {dps}")
    print(f"The {gun} takes {bkills} shots to kill with body shots")
    print(f"The {gun} takes {hkills} shots to kill with head shots")
    print(f"The {gun} takes {checkcheck} shots to kill with alternating head and body shots")
    print(f"The {gun} takes {tbkill}s to kill with body shots")
    print(f"The {gun} takes {tbkillm}s to kill with body shots after missing the first shot")
    print(f"The {gun} takes {thkill}s to kill with head shots")
    print(f"The {gun} takes {thkillm}s to kill with head shots after missing the first shot")
    print(f"The {gun} takes {thbkill}s to kill with alternating head and body shots after  missing the fist shot")
    print(f"The {gun}'s True Kill Time is {truetkill}s")
    print(f"The {gun}'s True Accuracy Score is {trueacc}")
    print(f"The {gun}'s True Weapon Score is {trueweapon}")
    print(f"The {gun}'s True Value Score is {value}")





    
    
    
    
    

    

    





