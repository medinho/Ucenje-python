print ("Pozdravljeni, sem program, s katerim boste uganili vaso srecno stevilko!")


your_name = raw_input("Najprej bi se ti rad predstavil, ime mi je Programko. Kako je pa tebi ime: ")

print("Pozdravljen/a, %s"  % your_name)

begin_game = raw_input ("A zacneva (da/ne)? ")
if begin_game == "da":
    print ("Odlicno! Ugibal/a bos sevilo med 1 in 50 in imel bos 5 poskusov! Vso sreco!")

if begin_game == "ne":
    print ("Vredu, lep dan se naprej!")


else:
    print ("Prosim odgovori z da ali ne!")

iskano_stevilo = 50
vsi_vnosi = 5

for stevilo_vnosov in range (vsi_vnosi):

    

    ugibano_stevilo = int (raw_input ("Na voljo imas se " + str (vsi_vnosi - stevilo_vnosov) +( " poskusov! Vnesi stevilo: " )))

    if int (ugibano_stevilo) == iskano_stevilo:
        print ("Cestitam! Uganil si stevilo!")
        break
    elif ugibano_stevilo > iskano_stevilo:
        print ("Pravo stevilo je manjse!")
    else:
        print ("Pravo stevilo je vecje!")
    
