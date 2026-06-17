
logins = [
 ("alice", "2024-05-10"),
 ("bob", "2024-05-10"),
 ("alice", "2024-05-10"),
 ("charlie", "2024-05-11"),
 ("alice", "2024-05-11"),
 ("bob", "2024-05-11"),
 ("bob", "2024-05-11")
]

login_counts ={}

for user,login in logins:
    login_counts[(user,login)] = login_counts.get((user,login),0)+1

dup=[ u for u,c in login_counts.items() if c >1]

print(dup)
print("\n")

#using pandas

import pandas as pd

df=pd.DataFrame(logins,columns = ["user","login"])
print(df)

dup_login = df.groupby(["user","login"]).size().reset_index(name="count")
dup_login = dup_login[dup_login["count"]>1]

print(" user login details who logged in more than a time per day \n")
print(dup_login.to_string(index=False))