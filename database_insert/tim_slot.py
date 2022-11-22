from MySqlConnect import MufiData

md = MufiData()

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(24):
    for j in range(12):
        code = "0"+string[i]+string[j]
        md.insertdb("insert into time_slot(time_id, hour, min) values('"+code+"', "+str(i)+","+str(j*5)+" )")